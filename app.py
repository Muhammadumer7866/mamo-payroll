import streamlit as st
import pandas as pd
import os
from database import load_secure_repository, verify_session_handshake

st.set_page_config(page_title="Al Rabhan Operational Vault", layout="wide", page_icon="🔒")

# UI Custom Layout Clean style
st.markdown("""
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    h1, h2, h3 {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
    </style>
""", unsafe_allow_html=True)

load_secure_repository()

if "auth_token_verified" not in st.session_state:
    st.session_state.auth_token_verified = False

if not st.session_state.auth_token_verified:
    _, center_box, _ = st.columns([1, 2, 1])
    with center_box:
        st.markdown("<h2 style='text-align: center; color: #5ab4ff; margin-top: 50px;'>AL RABHAN TRADING</h2>", unsafe_allow_html=True)
        with st.form("hardened_login_gateway"):
            input_user = st.text_input("Corporate ID / Email Address")
            input_pass = st.text_input("Security Access Key", type="password")
            if st.form_submit_button("Log In to System", type="primary"):
                if verify_session_handshake(input_user, input_pass):
                    st.session_state.auth_token_verified = True
                    st.rerun()
                else:
                    st.error("Authentication Violation: Invalid Keys logged.")
else:
    # Header Control
    head_col1, head_col2 = st.columns([8, 2])
    head_col1.markdown("<h2 style='color: #5ab4ff;'>🏗️ AL RABHAN TRADING - Sheet Ledger Panel</h2>", unsafe_allow_html=True)
    if head_col2.button("Log Out Session", type="primary", use_container_width=True):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["📝 Attendance Sheet View", "📄 Invoices Sheet View", "📊 Reports Summary Engine"])
    
    # ---------------- TAB 1: ATTENDANCE REAL SPREADSHEET ----------------
    with tab1:
        st.markdown("### 📊 Labour Attendance Spreadsheet Grid")
        
        # Fast input entries bar
        st.markdown("##### ⚡ Quick Input Lookup Row")
        quick_id = st.text_input("Type Employee ID & press Enter to Auto-populate matching details:", key="att_quick_search")
        matched_worker = st.session_state.master_workers[st.session_state.master_workers["Employee ID"] == quick_id.strip()]
        
        c_date = st.text_input("Set Current Date for Entry:", value="21/06/2026")
        
        # Interactive single-row table builder for clean presentation
        new_row_template = {
            "Date": c_date,
            "Employee ID": quick_id.strip() if quick_id.strip() != "" else "",
            "Name": matched_worker.iloc[0]["Name"] if not matched_worker.empty else "",
            "Company": matched_worker.iloc[0]["Company"] if not matched_worker.empty else "Al Rubhan Trading",
            "Scope": matched_worker.iloc[0]["Scope"] if not matched_worker.empty else "Civil",
            "Status": "Present"
        }
        
        st.markdown("##### ➕ Fill / Review Row Details then click Add button:")
        input_df = pd.DataFrame([new_row_template])
        edited_input = st.data_editor(input_df, key="single_entry_editor", use_container_width=True)
        
        if st.button("➕ Add Above Row to Main Sheet Table", type="primary"):
            st.session_state.workforce_matrix = pd.concat([st.session_state.workforce_matrix, edited_input], ignore_index=True)
            st.success("Row successfully appended to the sheet table!")
            st.rerun()
            
        st.markdown("---")
        
        # Main Sheet display area with dynamic built-in rows deletion 
        st.markdown("##### 🔍 Main Attendance Sheet (To delete an entry: click the row header block and press 'Delete' key on keyboard)")
        
        f1, f2 = st.columns(2)
        f_date = f1.selectbox("Filter Date View:", ["All Records", "21/06/2026", "20/06/2026"])
        f_search = f2.text_input("Live filter sheet by Name/ID text:")
        
        view_w_df = st.session_state.workforce_matrix.copy()
        if f_date != "All Records":
            view_w_df = view_w_df[view_w_df["Date"] == f_date]
        if f_search.strip() != "":
            view_w_df = view_w_df[view_w_df["Name"].str.contains(f_search, case=False) | view_w_df["Employee ID"].str.contains(f_search, case=False)]
            
        # REAL SPREADSHEET VIEW WITH ROW ADD/REMOVE CAPABILITY
        final_edited_w = st.data_editor(view_w_df, num_rows="dynamic", use_container_width=True, key="main_sheet_workforce")
        if len(final_edited_w) != len(view_w_df):
            st.session_state.workforce_matrix = final_edited_w
            st.rerun()

    # ---------------- TAB 2: INVOICES REAL SPREADSHEET ----------------
    with tab2:
        st.markdown("### 📄 Financial Invoices Spreadsheet Grid")
        
        st.markdown("##### ➕ Enter New Voucher Row Parameters:")
        inv_template = pd.DataFrame([{
            "Date": "21/06/2026", "Invoice No": "", "Vendor": "", "Amount": 0.000, "VAT": 0.000, "Total": 0.000, "Type": "Tax Invoice"
        }])
        edited_inv_input = st.data_editor(inv_template, key="single_inv_editor", use_container_width=True)
        
        if st.button("💾 Append Invoice Row to Sheet", type="primary"):
            row_data = edited_inv_input.iloc[0].to_dict()
            # Calculate VAT on the fly if needed
            if row_data["Type"] == "Tax Invoice" and row_data["VAT"] == 0:
                row_data["VAT"] = row_data["Amount"] * 0.05
            row_data["Total"] = row_data["Amount"] + row_data["VAT"]
            
            st.session_state.invoice_matrix = pd.concat([st.session_state.invoice_matrix, pd.DataFrame([row_data])], ignore_index=True)
            st.success("Invoice row committed successfully!")
            st.rerun()
            
        st.markdown("---")
        st.markdown("##### 🔍 Main Financial Invoice Sheet (Select full row & press Delete key to clear mistakes)")
        
        final_edited_i = st.data_editor(st.session_state.invoice_matrix, num_rows="dynamic", use_container_width=True, key="main_sheet_invoice")
        if len(final_edited_i) != len(st.session_state.invoice_matrix):
            st.session_state.invoice_matrix = final_edited_i
            st.rerun()

    # ---------------- TAB 3: MONTHLY & YEARLY CALCULATED REPORTS ----------------
    with tab3:
        st.markdown("### 📊 Automated Calculations & Report Compilations")
        
        # Labor metrics accumulation logic
        st.markdown("#### 👷 Master Worker Summary (Calculates Present Days / Holidays dynamically)")
        df_att = st.session_state.workforce_matrix.copy()
        
        if not df_att.empty:
            summary_records = []
            for emp_id in df_att["Employee ID"].unique():
                if str(emp_id).strip() == "": continue
                worker_data = df_att[df_att["Employee ID"] == emp_id]
                summary_records.append({
                    "Employee ID": emp_id,
                    "Worker Name": worker_data.iloc[0]["Name"],
                    "Company Structure": worker_data.iloc[0]["Company"],
                    "Total Logged Days": len(worker_data),
                    "Present Days (Duty)": len(worker_data[worker_data["Status"] == "Present"]),
                    "N/S Days (Holidays)": len(worker_data[worker_data["Status"] == "N/S"]),
                    "Absent Days": len(worker_data[worker_data["Status"] == "Absent"])
                })
            summary_df = pd.DataFrame(summary_records)
            st.dataframe(summary_df, use_container_width=True)
            st.download_button("📥 Download Monthly Labor Attendance Report (Excel .CSV)", data=summary_df.to_csv(index=False).encode('utf-8'), file_name='Monthly_Labor_Report.csv', mime='text/csv')
        else:
            st.info("No records loaded to process data matrices.")
            
        st.markdown("---")
        
        # Financial summary metrics accumulation logic
        st.markdown("#### 💰 Financial Invoices Combined Summary Ledger")
        df_inv = st.session_state.invoice_matrix.copy()
        
        if not df_inv.empty:
            m1, m2, m3 = st.columns(3)
            m1.metric("Consolidated Base Cost", f"{df_inv['Amount'].sum():.3f} OMR")
            m2.metric("Total Input VAT Amount", f"{df_inv['VAT'].sum():.3f} OMR")
            m3.metric("Total Net Financial Capital Spend", f"{df_inv['Total'].sum():.3f} OMR")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.dataframe(df_inv, use_container_width=True)
            st.download_button("📥 Download Financial Report Summary (Excel .CSV)", data=df_inv.to_csv(index=False).encode('utf-8'), file_name='Monthly_Financial_Report.csv', mime='text/csv')
        else:
            st.info("Invoice sheet is empty.")