import streamlit as st
import pandas as pd
import os
from database import load_secure_repository, verify_session_handshake

st.set_page_config(page_title="Al Rabhan Operational Vault", layout="wide", page_icon="🔒")

# Load CSS Styles dynamically from script file
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_secure_repository()

if "auth_token_verified" not in st.session_state:
    st.session_state.auth_token_verified = False

# Check if secrets configuration file exists to prevent server runtime panic crashes
try:
    _ = st.secrets["ADMIN_USER"]
    secrets_configured = True
except KeyError:
    secrets_configured = False

# ==========================================
# GATEWAY SCREEN (Hardened Cryptographic Login)
# ==========================================
if not st.session_state.auth_token_verified:
    _, center_box, _ = st.columns([1, 2, 1])
    with center_box:
        st.markdown("<h2 style='text-align: center; color: #5ab4ff; margin-top: 50px;'>AL RABHAN TRADING</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #a4b0be;'>Secure Operations Gateway Ledger</p>", unsafe_allow_html=True)
        
        with st.form("hardened_login_gateway"):
            input_user = st.text_input("Corporate ID / Email Address")
            input_pass = st.text_input("Security Access Key", type="password")
            submit_btn = st.form_submit_button("Log In to System", type="primary")
            
            if submit_btn:
                if not secrets_configured:
                    st.error("Configuration Error: Server runtime secret tokens not configured inside .streamlit/secrets.toml")
                elif verify_session_handshake(input_user, input_pass):
                    st.session_state.auth_token_verified = True
                    st.rerun()
                else:
                    st.error("Authentication Violation: Invalid Signature Keys logged.")

# ==========================================
# APPLICATION CORE (Authenticated State Layer)
# ==========================================
else:
    # Main Dashboard Header Panel
    head_col1, head_col2 = st.columns([8, 2])
    head_col1.markdown("<h1 style='color: #5ab4ff;'>🏗️ AL RABHAN TRADING - Control Center</h1>", unsafe_allow_html=True)
    if head_col2.button("Terminate Secure Session", type="primary", use_container_width=True):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    tab1, tab2 = st.tabs(["📝 Daily Attendance Matrix Logging Panel", "📄 Tax Invoices & Receipts Hub"])
    
    # ---------------- TAB 1: WORKFORCE MATRIX (Row-Specific Action Click Deletion) ----------------
    with tab1:
        st.markdown("### Active Workforce Roster")
        
        with st.expander("➕ Add New Field Worker Entry", expanded=False):
            with st.form("insert_worker_node", clear_on_submit=True):
                r1, r2, r3 = st.columns(3)
                w_date = r1.text_input("Date", value="21/06/2026")
                w_id = r2.text_input("Employee ID *")
                w_name = r3.text_input("Worker Full Name *")
                
                r4, r5, r6 = st.columns(3)
                w_comp = r4.text_input("Company Name", value="Rubhan. T")
                w_scope = r5.selectbox("Scope/Trade", ["Civil", "Mechanical", "Electrical"])
                w_stat = r6.selectbox("Duty Status", ["Present", "N/S", "Absent"])
                
                if st.form_submit_button("Commit Node Entry to Database"):
                    if w_id.strip() == "" or w_name.strip() == "":
                        st.error("Validation Error: Employee ID and Name are strict requirements.")
                    else:
                        new_row = pd.DataFrame([{
                            "Date": w_date, "Employee ID": w_id, "Name": w_name,
                            "Company": w_comp, "Scope": w_scope,
                            "Time In": "7:00 AM" if w_stat == "Present" else "-",
                            "Time Out": "5:00 PM" if w_stat == "Present" else "-",
                            "PPE": "Verified" if w_stat == "Present" else "-",
                            "Status": w_stat
                        }])
                        st.session_state.workforce_matrix = pd.concat([st.session_state.workforce_matrix, new_row], ignore_index=True)
                        st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Cursor Row UI Container Engine for Row-Level targeting
        for idx, row in st.session_state.workforce_matrix.iterrows():
            grid_col1, grid_col2 = st.columns([12, 1])
            
            # Formatted text line presenting full metrics for granular analysis
            grid_col1.info(f"📅 **{row['Date']}** | **ID:** {row['Employee ID']} | **Name:** {row['Name']} | **Company:** {row['Company']} | **Scope:** {row['Scope']} | **PPE:** {row['PPE']} | **Status:** {row['Status']}")
            
            # The Target cursor delete switch mapped exactly to pandas row index
            if grid_col2.button("🗑️", key=f"del_w_{idx}", help="Click to permanently wipe this entry"):
                st.session_state.workforce_matrix = st.session_state.workforce_matrix.drop(idx).reset_index(drop=True)
                st.rerun()

    # ---------------- TAB 2: FINANCIAL LOGS (Row-Specific Action Click Deletion) ----------------
    with tab2:
        st.markdown("### Corporate Receipts Ledger (Omani 5% VAT System)")
        
        with st.expander("📥 Archive New Financial Asset Voucher / Memo", expanded=False):
            with st.form("insert_invoice_node", clear_on_submit=True):
                f1, f2 = st.columns(2)
                v_date = f1.text_input("Transaction Date", value="21/06/2026")
                v_no = f2.text_input("Invoice / Cash Memo Code *")
                v_vendor = f1.text_input("Vendor Full Identity *")
                v_amt = f2.number_input("Taxable Base Amount (OMR)", min_value=0.000, step=0.001, format="%.3f")
                v_type = st.selectbox("Document Classification Node", ["Tax Invoice", "Cash Memo"])
                
                if st.form_submit_button("Commit Financial Node"):
                    if v_no.strip() == "" or v_vendor.strip() == "":
                        st.error("Validation Error: Identity parameters required.")
                    else:
                        calc_vat = v_amt * 0.05 if v_type == "Tax Invoice" else 0.0
                        new_inv = pd.DataFrame([{
                            "Date": v_date, "Invoice No": v_no, "Vendor": v_vendor,
                            "Amount": v_amt, "VAT": calc_vat, "Total": v_amt + calc_vat, "Type": v_type
                        }])
                        st.session_state.invoice_matrix = pd.concat([st.session_state.invoice_matrix, new_inv], ignore_index=True)
                        st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        
        for idx, row in st.session_state.invoice_matrix.iterrows():
            grid_col1, grid_col2 = st.columns([12, 1])
            grid_col1.warning(f"🧾 **{row['Date']}** | **Ref:** {row['Invoice No']} | **Vendor:** {row['Vendor']} | **Base:** {row['Amount']:.3f} OMR | **VAT:** {row['VAT']:.3f} OMR | **Total:** {row['Total']:.3f} OMR | **Type:** {row['Type']}")
            
            if grid_col2.button("🗑️", key=f"del_i_{idx}", help="Click to permanently wipe this financial record"):
                st.session_state.invoice_matrix = st.session_state.invoice_matrix.drop(idx).reset_index(drop=True)
                st.rerun()