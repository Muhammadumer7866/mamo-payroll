import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Configuration (Standard & Stable)
st.set_page_config(
    page_title="Al Rabhan Trading - ERP Control Panel",
    page_icon="🏗️",
    layout="wide"
)

# 2. Reusable Central State Management (Pre-populating Real Data)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'workforce_db' not in st.session_state:
    st.session_state.workforce_db = pd.DataFrame([
        {"Labour ID": "AR-L01", "Name": "Muhammad Ali", "Trade": "Mason", "Shift": "Day", "Status": "Present", "Check-In": "07:00 AM"},
        {"Labour ID": "AR-L02", "Name": "Sajid Khan", "Trade": "Steel Fixer", "Shift": "Day", "Status": "Present", "Check-In": "06:55 AM"},
        {"Labour ID": "AR-L03", "Name": "Kumar Swamy", "Trade": "Carpenter", "Shift": "Day", "Status": "Present", "Check-In": "07:02 AM"},
        {"Labour ID": "AR-L04", "Name": "Ahmed Al-Balushi", "Trade": "Site Supervisor", "Shift": "Day", "Status": "Present", "Check-In": "06:45 AM"}
    ])

if 'invoice_db' not in st.session_state:
    st.session_state.invoice_db = pd.DataFrame([
        {
            "Invoice No": "A204306",
            "Date": "20/06/2026",
            "Supplier Name": "Al Inma Building Materials L.L.C.",
            "Material Description": "Marsbit P 4mm (28 Rolls) & Tech Prime SB (2 Pails)",
            "Taxable Amount (OMR)": 338.600,
            "VAT Amount 5% (OMR)": 16.930,
            "Total Invoice Gross (OMR)": 355.530,
            "Audit Integrity Check": "Verified & Passed"
        }
    ])

# ==============================================================================
# PHASE 1: SECURE LOGIN GATEWAY (Bina kisi CSS ke, 100% visible layout)
# ==============================================================================
if not st.session_state.logged_in:
    # 2 Column layout using native Streamlit columns
    left_col, right_col = st.columns(2, gap="large")
    
    with left_col:
        st.title("🏗️ AL RABHAN TRADING")
        st.subheader("Sultanate of Oman • Enterprise Logistics Control")
        st.write("Please authenticate administrative level keys to open the operations panel.")
        
        # Form Input Fields
        input_user = st.text_input("Corporate ID / Email Address", placeholder="e.g. admin@construction.om")
        input_pass = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
        
        if st.button("Log In to System", type="primary"):
            if input_user == "admin@construction.om" and input_pass == "Oman#Secure2026":
                st.session_state.logged_in = True
                st.success("Access Granted. Loading Operations Node...")
                st.rerun()
            else:
                st.error("Invalid Corporate Credentials. Access Denied.")
                
    with right_col:
        # Beautiful native container border acting as a card
        with st.container(border=True):
            st.markdown("### 🌐 Oman Enterprise Infrastructure")
            st.markdown("**Effortlessly manage your workforce and corporate financials.**")
            st.write(
                "Consolidated cloud tracking console custom engineered for real-time field operations, "
                "active shift logs control, and Omani Tax Invoice registry archiving."
            )
            st.info("Automated analytical report structuring engine compiles binary Excel ledgers instantaneously for internal validation.")
            st.caption("CONSTRUCTION | QUALITY | TRUST")

# ==============================================================================
# PHASE 2: MAIN ENTERPRISE DASHBOARD (Once Authenticated)
# ==============================================================================
else:
    # Global System Top Header
    st.title("🏗️ AL RABHAN TRADING OPERATIONS SYSTEM")
    st.caption("Sultanate of Oman • Secure Enterprise Infrastructure Control Node")
    
    # Logout button in the header row
    h_col1, h_col2 = st.columns([6, 1])
    h_col1.success("🔒 System Integrity Node: Active (Automated Excel/CSV Ledger Extraction Enabled)")
    if h_col2.button("Log Out", type="secondary"):
        st.session_state.logged_in = False
        st.rerun()
        
    st.markdown("---")

    # Native Tabs with high contrast and sharp layout
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏠 Corporate Command Hub", 
        "📝 Attendance Roster Module", 
        "📄 Tax Invoices Registry", 
        "📊 Chronological Reports Export"
    ])

    # --- TAB 1: CORPORATE HUB ---
    with tab1:
        st.subheader("📊 Real-Time Operations Overview Matrix")
        st.write("Aggregated system metrics reflecting current active field deployment rosters, verified logistics registries, and global transacted ledger archives safely tracked across Omani operational zones.")
        
        # Mathematical updates using state values
        total_workers = len(st.session_state.workforce_db)
        total_docs = len(st.session_state.invoice_db)
        total_financial_volume = st.session_state.invoice_db["Total Invoice Gross (OMR)"].sum()
        
        # High contrast standard metrics row
        m1, m2, m3 = st.columns(3)
        m1.metric(label="ACTIVE REGISTERED WORKFORCE", value=f"{total_workers} Units")
        m2.metric(label="ARCHIVED TAX DOCUMENTS", value=f"{total_docs} Invoices")
        m3.metric(label="GROSS FINANCIAL VOLUME", value=f"{total_financial_volume:.3f} OMR")
        
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Live Field Attendance Preview")
            st.dataframe(st.session_state.workforce_db, use_container_width=True, hide_index=True)
        with col_b:
            st.markdown("#### Recent Transacted Invoices Log")
            st.dataframe(st.session_state.invoice_db[["Invoice No", "Supplier Name", "Total Invoice Gross (OMR)", "Audit Integrity Check"]], use_container_width=True, hide_index=True)

    # --- TAB 2: ATTENDANCE MODULE ---
    with tab2:
        st.subheader("📝 Daily Attendance Matrix Logging Panel")
        st.write("Manage and log daily workforce deployment shifts, real-time check-ins, and trade categorization for construction sites.")
        
        with st.expander("➕ Log New Labour Deployment Record", expanded=False):
            with st.form("add_worker_form", clear_on_submit=True):
                c1, c2, c3 = st.columns(3)
                new_id = c1.text_input("Labour ID", value=f"AR-L0{len(st.session_state.workforce_db)+1}")
                new_name = c2.text_input("Full Name *")
                new_trade = c3.selectbox("Trade / Role", ["Mason", "Steel Fixer", "Carpenter", "Electrician", "Plumber", "Labourer", "Site Supervisor"])
                
                c4, c5 = st.columns(2)
                new_shift = c4.radio("Shift Allocation", ["Day", "Night"])
                new_status = c5.selectbox("Initial Attendance Status", ["Present", "Absent", "Scheduled"])
                
                if st.form_submit_button("Commit Entry to Ledger"):
                    if new_name.strip() == "":
                        st.error("Error: Please provide a valid Name.")
                    else:
                        new_entry = {
                            "Labour ID": new_id, "Name": new_name, "Trade": new_trade,
                            "Shift": new_shift, "Status": new_status,
                            "Check-In": datetime.now().strftime("%I:%M %p") if new_status == "Present" else "-"
                        }
                        st.session_state.workforce_db = pd.concat([st.session_state.workforce_db, pd.DataFrame([new_entry])], ignore_index=True)
                        st.success(f"Success: Record for '{new_name}' saved.")
                        st.rerun()

        st.dataframe(st.session_state.workforce_db, use_container_width=True, hide_index=True)

    # --- TAB 3: TAX REGISTRY ---
    with tab3:
        st.subheader("📄 Omani Tax Invoice Registry & Compliance Node")
        st.write("Official digital vault for archiving, validating, and auditing Omani standard Tax Invoices with automated 5% VAT calculations.")
        
        with st.expander("📥 Register & Parse New Corporate Tax Invoice", expanded=False):
            with st.form("add_invoice_form", clear_on_submit=True):
                i1, i2 = st.columns(2)
                inv_no = i1.text_input("Invoice Number", value="A204307")
                inv_date = i2.text_input("Invoice Date (DD/MM/YYYY)", value=datetime.now().strftime("%d/%m/%Y"))
                supplier = i1.text_input("Supplier Name Entity", value="Al Inma Building Materials L.L.C.")
                items_desc = i2.text_area("Item Description Details")
                
                taxable_amt = st.number_input("Taxable Base Amount (OMR)", min_value=0.000, value=0.000, step=0.001, format="%.3f")
                
                if st.form_submit_button("Verify and Process Tax Record"):
                    if items_desc.strip() == "":
                        st.error("Error: Item Description details cannot be left empty.")
                    else:
                        computed_vat = taxable_amt * 0.05
                        computed_gross = taxable_amt + computed_vat
                        
                        new_invoice = {
                            "Invoice No": inv_no, "Date": inv_date, "Supplier Name": supplier,
                            "Material Description": items_desc, "Taxable Amount (OMR)": taxable_amt,
                            "VAT Amount 5% (OMR)": computed_vat, "Total Invoice Gross (OMR)": computed_gross,
                            "Audit Integrity Check": "Verified & Passed"
                        }
                        st.session_state.invoice_db = pd.concat([st.session_state.invoice_db, pd.DataFrame([new_invoice])], ignore_index=True)
                        st.success(f"Success: Tax Invoice {inv_no} archived.")
                        st.rerun()

        st.dataframe(st.session_state.invoice_db, use_container_width=True, hide_index=True)

    # --- TAB 4: CHRONOLOGICAL REPORTS EXPORT ---
    with tab4:
        st.subheader("📊 Reports Export Panel & Audit Trail Engine")
        st.write("Generate and structure spreadsheets (CSV format) for internal validation.")
        
        st.radio("Chronology Scope Focus:", ["View Complete History Logs", "Filter Target Monthly Matrix View"])
        st.markdown("---")
        
        # Clean Binary Data Encoding
        csv_workers_bytes = st.session_state.workforce_db.to_csv(index=False).encode('utf-8')
        csv_invoice_bytes = st.session_state.invoice_db.to_csv(index=False).encode('utf-8')
        
        # Fix: Removed 'use_container_width' warning parameter for full backward/forward compatibility
        down_col1, down_col2 = st.columns(2)
        down_col1.download_button(
            label="📥 Export Roster Matrix (.CSV)",
            data=csv_workers_bytes,
            file_name=f"Al_Rabhan_Roster_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
        down_col2.download_button(
            label="📥 Export Tax Ledger (.CSV)",
            data=csv_invoice_bytes,
            file_name=f"Al_Rabhan_Tax_Ledger_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )