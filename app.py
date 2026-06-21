import streamlit as st
import pandas as pd
import os
from database import load_secure_repository, verify_session_handshake

st.set_page_config(page_title="Al Rabhan Operational Vault", layout="wide", page_icon="🔒")

if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
    # Top Bar Header Actions
    head_col1, head_col2 = st.columns([8, 2])
    head_col1.markdown("<h1 style='color: #5ab4ff;'>🏗️ AL RABHAN TRADING - Operations Control Center</h1>", unsafe_allow_html=True)
    if head_col2.button("Terminate Session", type="primary", use_container_width=True):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["📝 Attendance Grid Ledger", "📄 Invoices Grid Ledger", "📊 Monthly & Yearly Report Hub"])
    
    # ---------------- TAB 1: ATTENDANCE MANAGEMENT ----------------
    with tab1:
        st.markdown("### 🗓️ Daily Attendance Matrix Grid")
        
        # Section A: Quick ID Search & Entry (Auto Fill)
        st.markdown("#### ⚡ Quick Dynamic Entry Bar")
        quick_id = st.text_input("Enter Worker Employee ID for Quick Fill:", key="att_quick_search")
        
        matched_worker = st.session_state.master_workers[st.session_state.master_workers["Employee ID"] == quick_id.strip()]
        
        with st.form("quick_attendance_form", clear_on_submit=True):
            col_a, col_b, col_c = st.columns(3)
            q_date = col_a.text_input("Date (DD/MM/YYYY)", value="21/06/2026")
            
            w_name = matched_worker.iloc[0]["Name"] if not matched_worker.empty else ""
            w_comp = matched_worker.iloc[0]["Company"] if not matched_worker.empty else ""
            w_scop = matched_worker.iloc[0]["Scope"] if not matched_worker.empty else ""
            
            q_name = col_b.text_input("Worker Full Name", value=w_name, disabled=not matched_worker.empty)
            q_comp = col_c.text_input("Company Structure", value=w_comp, disabled=not matched_worker.empty)
            
            col_d, col_e = st.columns([2, 1])
            q_scope = col_d.text_input("Scope/Trade Node", value=w_scop, disabled=not matched_worker.empty)
            q_status = col_e.selectbox("Duty Status Signature", ["Present", "N/S", "Absent"])
            
            if st.form_submit_button("⚡ Commit Attendance Record to Grid", type="primary"):
                if quick_id.strip() == "" or q_name.strip() == "":
                    st.error("Validation Halt: Please input valid data or scan proper ID.")
                else:
                    new_rec = pd.DataFrame([{
                        "Date": q_date.strip(), "Employee ID": quick_id.strip(), "Name": q_name.strip(),
                        "Company": q_comp.strip(), "Scope": q_scope.strip(), "Status": q_status
                    }])
                    st.session_state.workforce_matrix = pd.concat([st.session_state.workforce_matrix, new_rec], ignore_index=True)
                    st.success(f"Log updated successfully for {q_name}!")
                    st.rerun()

        # Section B: New Registration Module
        with st.expander("🆕 Register Brand New Worker onto Master Database"):
            with st.form("master_reg_form", clear_on_submit=True):
                r_id = st.text_input("Assign Unique Employee ID *")
                r_name = st.text_input("Worker Full Name *")
                r_comp = st.text_input("Company Affiliation", value="Al Rubhan Trading")
                r_scop = st.text_input("Scope/Trade Specialty", value="Civil")
                if st.form_submit_button("Register to Master Roster"):
                    if r_id.strip() == "" or r_name.strip() == "":
                        st.error("Fields cannot be empty!")
                    else:
                        new_m = pd.DataFrame([{"Employee ID": r_id.strip(), "Name": r_name.strip(), "Company": r_comp.strip(), "Scope": r_scop.strip()}])
                        st.session_state.master_workers = pd.concat([st.session_state.master_workers, new_m], ignore_index=True)
                        st.success("New asset successfully added to lookup engine database.")

        st.markdown("---")
        
        # Section C: Data Table View with Inline Row Deletion
        st.markdown("#### 🔍 Active Spreadsheet Ledger")
        f1, f2 = st.columns(2)
        filter_date = f1.selectbox("Filter Grid Date Range:", ["All Data Ledger", "21/06/2026", "20/06/2026"])
        text_search_w = f2.text_input("Live Spreadsheet text string filter:")
        
        df_w_filtered = st.session_state.workforce_matrix.copy()
        if filter_date != "All Data Ledger":
            df_w_filtered = df_w_filtered[df_w_filtered["Date"] == filter_date]
        if text_search_w.strip() != "":
            df_w_filtered = df_w_filtered[df_w_filtered["Name"].str.contains(text_search_w, case=False) | df_w_filtered["Employee ID"].str.contains(text_search_w, case=False)]
            
        # Displaying with exact Row-by-Row Delete Option
        for idx, row in df_w_filtered.iterrows():
            g_col1, g_col2 = st.columns([12, 1])
            g_col1.info(f"📅 **{row['Date']}** | **ID:** {row['Employee ID']} | **Name:** {row['Name']} | **Company:** {row['Company']} | **Scope:** {row['Scope']} | **Status:** {row['Status']}")
            if g_col2.button("🗑️", key=f"del_w_row_{idx}", help="Wipe this specific worker attendance log"):
                st.session_state.workforce_matrix = st.session_state.workforce_matrix.drop(idx).reset_index(drop=True)
                st.success("Entry removed successfully.")
                st.rerun()

    # ---------------- TAB 2: FINANCIAL LOGS ----------------
    with tab2:
        st.markdown("### 📄 Tax Invoices & Receipts Grid Ledger")
        
        with st.form("invoice_grid_form", clear_on_submit=True):
            fi_1, fi_2, fi_3 = st.columns(3)
            i_date = fi_1.text_input("Invoice Transaction Date", value="21/06/2026")
            i_num = fi_2.text_input("Invoice Reference Code *")
            i_vendor = fi_3.text_input("Vendor Identity *")
            
            fi_4, fi_5 = st.columns(2)
            i_amt = fi_4.number_input("Taxable Base Amount (OMR)", min_value=0.000, step=0.001, format="%.3f")
            i_type = fi_5.selectbox("Tax Setup", ["Tax Invoice", "Cash Memo"])
            
            if st.form_submit_button("💾 Commit Financial Voucher to Table"):
                if i_num.strip() == "" or i_vendor.strip() == "":
                    st.error("Reference tokens cannot be empty!")
                else:
                    calc_vat = i_amt * 0.05 if i_type == "Tax Invoice" else 0.0
                    new_inv = pd.DataFrame([{
                        "Date": i_date.strip(), "Invoice No": i_num.strip(), "Vendor": i_vendor.strip(),
                        "Amount": i_amt, "VAT": calc_vat, "Total": i_amt + calc_vat, "Type": i_type
                    }])
                    st.session_state.invoice_matrix = pd.concat([st.session_state.invoice_matrix, new_inv], ignore_index=True)
                    st.success("Financial ledger matrix updated.")
                    st.rerun()
                    
        st.markdown("---")
        
        # Displaying Invoice Table rows with inline Delete button
        for idx, row in st.session_state.invoice_matrix.iterrows():
            g_col1, g_col2 = st.columns([12, 1])
            g_col1.warning(f"🧾 **{row['Date']}** | **Ref:** {row['Invoice No']} | **Vendor:** {row['Vendor']} | **Base:** {row['Amount']:.3f} OMR | **VAT:** {row['VAT']:.3f} OMR | **Total:** {row['Total']:.3f} OMR | **Type:** {row['Type']}")
            if g_col2.button("🗑️", key=f"del_i_row_{idx}", help="Wipe this specific financial invoice"):
                st.session_state.invoice_matrix = st.session_state.invoice_matrix.drop(idx).reset_index(drop=True)
                st.success("Invoice wiped successfully.")
                st.rerun()

    # ---------------- TAB 3: EXECUTIVE REFORTS (LABOUR & INVOICE MONHTLY/YEARLY) ----------------
    with tab3:
        st.markdown("### 📊 Automated Month-End & Yearly Analytics Dashboard")
        
        # 1. LABOUR SUMMARY (Days, Holidays, Absents calculation)
        st.markdown("#### 👷 Labor Operational Attendance Summary (Monthly/Yearly Calculation)")
        df_att = st.session_state.workforce_matrix.copy()
        
        if not df_att.empty:
            summary_records = []
            unique_workers = df_att["Employee ID"].unique()
            
            for emp_id in unique_workers:
                worker_data = df_att[df_att["Employee ID"] == emp_id]
                name = worker_data.iloc[0]["Name"]
                company = worker_data.iloc[0]["Company"]
                
                total_days = len(worker_data)
                present_days = len(worker_data[worker_data["Status"] == "Present"])
                ns_days = len(worker_data[worker_data["Status"] == "N/S"])
                absent_days = len(worker_data[worker_data["Status"] == "Absent"])
                
                summary_records.append({
                    "Employee ID": emp_id,
                    "Worker Name": name,
                    "Company Structure": company,
                    "Total Logged Days": total_days,
                    "Present Days (Duty)": present_days,
                    "N/S Days (Holidays)": ns_days,
                    "Absent Days": absent_days
                })
                
            summary_df = pd.DataFrame(summary_records)
            st.dataframe(summary_df, use_container_width=True)
            
            st.download_button(
                label="📥 Export Monthly Labor Attendance Report (Spreadsheet Format)",
                data=summary_df.to_csv(index=False).encode('utf-8'),
                file_name='Monthly_Labor_Attendance_Report.csv',
                mime='text/csv'
            )
        else:
            st.info("No workforce records logged yet to compile metrics.")
            
        st.markdown("---")
        
        # 2. INVOICE EXPORT (Monthly/Yearly Summaries)
        st.markdown("#### 💰 Financial Invoices Ledger Breakdown")
        df_inv = st.session_state.invoice_matrix.copy()
        
        if not df_inv.empty:
            total_base = df_inv["Amount"].sum()
            total_vat = df_inv["VAT"].sum()
            total_net = df_inv["Total"].sum()
            
            met_col1, met_col2, met_col3 = st.columns(3)
            met_col1.metric("Total Taxable Base Spend", f"{total_base:.3f} OMR")
            met_col2.metric("Accumulated VAT Asset (5%)", f"{total_vat:.3f} OMR")
            met_col3.metric("Total Consolidated Cost", f"{total_net:.3f} OMR")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.dataframe(df_inv, use_container_width=True)
            
            st.download_button(
                label="📥 Export Monthly/Yearly Financial Invoice Report (Spreadsheet Format)",
                data=df_inv.to_csv(index=False).encode('utf-8'),
                file_name='Monthly_Financial_Invoice_Report.csv',
                mime='text/csv'
            )
        else:
            st.info("No receipts archived for processing.")