import streamlit as st
import pandas as pd
import os
from database import load_secure_repository, verify_session_handshake

st.set_page_config(page_title="Al Rabhan Operational Vault", layout="wide", page_icon="🔒")

# UI Styling Hub
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_secure_repository()

if "auth_token_verified" not in st.session_state:
    st.session_state.auth_token_verified = False

# ==========================================
# GATEWAY SCREEN
# ==========================================
if not st.session_state.auth_token_verified:
    _, center_box, _ = st.columns([1, 2, 1])
    with center_box:
        st.markdown("<h2 style='text-align: center; color: #5ab4ff; margin-top: 50px;'>AL RABHAN TRADING</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #a4b0be;'>Secure Operations Gateway Ledger</p>", unsafe_allow_html=True)
        
        with st.form("hardened_login_gateway"):
            input_user = st.text_input("Corporate ID / Email Address")
            input_pass = st.text_input("Security Access Key", type="password")
            if st.form_submit_button("Log In to System", type="primary"):
                if verify_session_handshake(input_user, input_pass):
                    st.session_state.auth_token_verified = True
                    st.rerun()
                else:
                    st.error("Authentication Violation: Invalid Signature Keys logged.")

# ==========================================
# CORE CONTROL PANEL
# ==========================================
else:
    head_col1, head_col2 = st.columns([8, 2])
    head_col1.markdown("<h1 style='color: #5ab4ff;'>🏗️ AL RABHAN TRADING - Control Center</h1>", unsafe_allow_html=True)
    if head_col2.button("Terminate Secure Session", type="primary", use_container_width=True):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    tab1, tab2 = st.tabs(["📝 Daily Attendance Matrix Logging Panel", "📄 Tax Invoices & Receipts Hub"])
    
    # ---------------- TAB 1: WORKFORCE ATTENDANCE ----------------
    with tab1:
        st.markdown("### Active Workforce Roster")
        
        # 1. New Entry Insertion Form
        with st.expander("➕ Add New Field Worker Node", expanded=False):
            with st.form("add_worker_form", clear_on_submit=True):
                c1, c2, c3 = st.columns(3)
                ins_date = c1.text_input("Date (DD/MM/YYYY)", value="21/06/2026")
                ins_id = c2.text_input("Employee ID *")
                ins_name = c3.text_input("Worker Full Name *")
                
                c4, c5, c6 = st.columns(3)
                ins_company = c4.text_input("Company", value="Rubhan. T")
                ins_scope = c5.text_input("Scope/Trade", value="Civil")
                ins_status = c6.selectbox("Status", ["Present", "N/S", "Absent"])
                
                if st.form_submit_button("Save Worker to Database"):
                    if ins_id.strip() == "" or ins_name.strip() == "":
                        st.error("ID and Name are strictly required fields!")
                    else:
                        new_worker = pd.DataFrame([{
                            "Date": ins_date.strip(), "Employee ID": ins_id.strip(), "Name": ins_name.strip(),
                            "Company": ins_company.strip(), "Scope": ins_scope.strip(),
                            "Time In": "7:00 AM" if ins_status == "Present" else "-",
                            "Time Out": "5:00 PM" if ins_status == "Present" else "-",
                            "PPE": "Verified" if ins_status == "Present" else "-",
                            "Status": ins_status
                        }])
                        st.session_state.workforce_matrix = pd.concat([st.session_state.workforce_matrix, new_worker], ignore_index=True)
                        st.success("Worker node successfully committed!")
                        st.rerun()

        st.markdown("---")
        
        # 2. Advanced Search & Report Filter Utilities
        st.markdown("#### 🔍 Filter & Report Generation Engine")
        f_col1, f_col2, f_col3 = st.columns([2, 2, 4])
        
        search_date = f_col1.selectbox("Select Target Date:", ["All Dates", "Today (21/06/2026)", "Yesterday (20/06/2026)"])
        search_month_year = f_col2.text_input("Filter Monthly/Yearly (e.g., /06/2026)", value="")
        text_search = f_col3.text_input("Dynamic Text Query Search (Type ID, Name or Company to filter live):")
        
        # Apply Filters
        df_w = st.session_state.workforce_matrix.copy()
        if search_date == "Today (21/06/2026)":
            df_w = df_w[df_w['Date'] == "21/06/2026"]
        elif search_date == "Yesterday (20/06/2026)":
            df_w = df_w[df_w['Date'] == "20/06/2026"]
            
        if search_month_year.strip() != "":
            df_w = df_w[df_w['Date'].str.contains(search_month_year)]
            
        if text_search.strip() != "":
            df_w = df_w[df_w['Employee ID'].str.contains(text_search, case=False) | 
                        df_w['Name'].str.contains(text_search, case=False) | 
                        df_w['Company'].str.contains(text_search, case=False)]

        # 3. Download Reports Node
        csv_data_w = df_w.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Attendance Report (Excel / Word Ready Spreadsheet)",
            data=csv_data_w,
            file_name='Attendance_Filtered_Report.csv',
            mime='text/csv',
        )

        st.markdown("<br>", unsafe_allow_html=True)
        
        # 4. Data Node Display
        for idx, row in df_w.iterrows():
            grid_col1, grid_col2 = st.columns([12, 1])
            grid_col1.info(f"📅 **{row['Date']}** | **ID:** {row['Employee ID']} | **Name:** {row['Name']} | **Company:** {row['Company']} | **Scope:** {row['Scope']} | **Status:** {row['Status']}")
            if grid_col2.button("🗑️", key=f"del_w_{idx}"):
                st.session_state.workforce_matrix = st.session_state.workforce_matrix.drop(idx).reset_index(drop=True)
                st.rerun()

    # ---------------- TAB 2: FINANCIAL LOGS ----------------
    with tab2:
        st.markdown("### Corporate Receipts Ledger")
        
        # 1. New Invoice Insertion Form
        with st.expander("➕ Archive New Financial Voucher/Memo", expanded=False):
            with st.form("add_invoice_form", clear_on_submit=True):
                i1, i2 = st.columns(2)
                inv_date = i1.text_input("Transaction Date (DD/MM/YYYY)", value="21/06/2026")
                inv_code = i2.text_input("Invoice / Cash Memo Code *")
                inv_vendor = i1.text_input("Vendor Identity *")
                inv_amount = i2.number_input("Taxable Base Amount (OMR)", min_value=0.000, step=0.001, format="%.3f")
                inv_type = st.selectbox("Classification Node", ["Tax Invoice", "Cash Memo"])
                
                if st.form_submit_button("Commit Financial Node"):
                    if inv_code.strip() == "" or inv_vendor.strip() == "":
                        st.error("Reference fields are strict requirements!")
                    else:
                        calc_vat = inv_amount * 0.05 if inv_type == "Tax Invoice" else 0.0
                        new_inv = pd.DataFrame([{
                            "Date": inv_date.strip(), "Invoice No": inv_code.strip(), "Vendor": inv_vendor.strip(),
                            "Amount": inv_amount, "VAT": calc_vat, "Total": inv_amount + calc_vat, "Type": inv_type
                        }])
                        st.session_state.invoice_matrix = pd.concat([st.session_state.invoice_matrix, new_inv], ignore_index=True)
                        st.success("Financial node successfully logged!")
                        st.rerun()

        st.markdown("---")
        
        # 2. Advanced Invoice Search Utilities
        st.markdown("#### 🔍 Filter & Financial Report Generation Engine")
        fi_col1, fi_col2, fi_col3 = st.columns([2, 2, 4])
        
        inv_search_date = fi_col1.selectbox("Select Target Invoice Date:", ["All Dates", "Today (21/06/2026)", "Yesterday (20/06/2026)"])
        inv_search_month = fi_col2.text_input("Filter Invoices Monthly/Yearly (e.g., /06/2026)", value="")
        inv_text_search = fi_col3.text_input("Dynamic Text Search (Type Invoice No or Vendor to filter live):")
        
        df_i = st.session_state.invoice_matrix.copy()
        if inv_search_date == "Today (21/06/2026)":
            df_i = df_i[df_i['Date'] == "21/06/2026"]
        elif inv_search_date == "Yesterday (20/06/2026)":
            df_i = df_i[df_i['Date'] == "20/06/2026"]
            
        if inv_search_month.strip() != "":
            df_i = df_i[df_i['Date'].str.contains(inv_search_month)]
            
        if inv_text_search.strip() != "":
            df_i = df_i[df_i['Invoice No'].str.contains(inv_text_search, case=False) | 
                        df_i['Vendor'].str.contains(inv_text_search, case=False)]

        # 3. Download Financial Reports Node
        csv_data_i = df_i.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Financial Ledger",
            data=csv_data_i,
            file_name='Financial_Filtered_Report.csv',
            mime='text/csv',
        )

        st.markdown("<br>", unsafe_allow_html=True)
        
        # 4. Display Financial Logs
        for idx, row in df_i.iterrows():
            grid_col1, grid_col2 = st.columns([12, 1])
            grid_col1.warning(f"🧾 **{row['Date']}** | **Ref:** {row['Invoice No']} | **Vendor:** {row['Vendor']} | **Total:** {row['Total']:.3f} OMR | **Type:** {row['Type']}")
            if grid_col2.button("🗑️", key=f"del_i_{idx}"):
                st.session_state.invoice_matrix = st.session_state.invoice_matrix.drop(idx).reset_index(drop=True)
                st.rerun()