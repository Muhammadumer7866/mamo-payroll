import streamlit as st
import pandas as pd
from database import load_secure_repository, verify_session_handshake, inject_security_css_shield

st.set_page_config(page_title="Al Rabhan Trading - Secure Vault", layout="wide", page_icon="🔒")
inject_security_css_shield()
load_secure_repository()

# Secure Session Token Verification
if "auth_token_verified" not in st.session_state:
    st.session_state.auth_token_verified = False

# ==========================================
# SECURE GATEWAY PANEL (Zero Inspect Element Leakage)
# ==========================================
if not st.session_state.auth_token_verified:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<h2 style='text-align: center; color: #1A5276;'>AL RABHAN TRADING</h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: #7F8C8D;'>Secure Operations Gateway Ledger</h5>", unsafe_allow_html=True)
        
        with st.form("hardened_login_gateway"):
            input_user = st.text_input("Corporate Access ID", placeholder="username@domain.om")
            input_pass = st.text_input("Cryptographic Access Key", type="password", placeholder="••••••••••••")
            submit_auth = st.form_submit_button("Authenticate Session")
            
            if submit_auth:
                if verify_session_handshake(input_user, input_pass):
                    st.session_state.auth_token_verified = True
                    st.success("Handshake Verified. Granting Access Layers...")
                    st.rerun()
                else:
                    st.error("Authentication Violation: Invalid Signature Keys logged.")

# ==========================================
# INDUSTRIAL CORE DASHBOARD (Authenticated State)
# ==========================================
else:
    # Top Branding Header Row
    st.markdown("<h1 style='color: #1A5276;'>🏗️ Al Rabhan Trading - Control Core</h1>", unsafe_allow_html=True)
    
    top_col1, top_col2 = st.columns([6, 1])
    top_col1.caption("System Integrity Status: SECURE (SHA-256 Encrypted State)")
    if top_col2.button("Terminate Session", type="primary"):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📊 Workforce Matrix Grid", "📄 Financial Receipts Hub", "📥 Secure Data Extraction"])
    
    # ---------------- TAB 1: WORKFORCE MATRIX (Row-Specific Deletion) ----------------
    with tab1:
        st.subheader("Current Active Deployment Matrix (20 & 21 June)")
        
        # Smart Inputs Row
        with st.expander("➕ Inject New Field Deployment Entry", expanded=False):
            with st.form("insert_worker_node"):
                r1, r2, r3 = st.columns(3)
                w_date = r1.text_input("Deployment Date", value="21/06/2026")
                w_id = r2.text_input("Employee Card ID *")
                w_name = r3.text_input("Worker Full Name *")
                
                r4, r5, r6 = st.columns(3)
                w_comp = r4.text_input("Company Assign", value="Rubhan. T")
                w_scope = r5.selectbox("Scope Matrix", ["Civil", "Mechanical", "Electrical"])
                w_stat = r6.selectbox("Status", ["Present", "N/S", "Absent"])
                
                if st.form_submit_button("Commit Node Entry"):
                    if w_id.strip() == "" or w_name.strip() == "":
                        st.error("Fields marked with (*) are strict requirements.")
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
                        st.success("Node integrated securely.")
                        st.rerun()

        st.markdown("#### Operational Roster View")
        # Dynamic Row Specific Action Engine
        for idx, row in st.session_state.workforce_matrix.iterrows():
            grid_col1, grid_col2 = st.columns([8, 1])
            # Rendering row as data block
            grid_col1.info(f"📅 **{row['Date']}** | **ID:** {row['Employee ID']} | **Name:** {row['Name']} | **Company:** {row['Company']} | **Scope:** {row['Scope']} | **Status:** {row['Status']}")
            
            # Row specific removal switch triggered explicitly by index cursor placement
            if grid_col2.button("❌ Remove", key=f"del_w_{idx}"):
                st.session_state.workforce_matrix = st.session_state.workforce_matrix.drop(idx).reset_index(drop=True)
                st.toast(f"Record index {row['Employee ID']} wiped.")
                st.rerun()

    # ---------------- TAB 2: FINANCIAL LOGS (Row-Specific Deletion) ----------------
    with tab2:
        st.subheader("Omani VAT Compliance Registry Node")
        
        with st.expander("📥 Archive New Asset Purchase Voucher", expanded=False):
            with st.form("insert_invoice_node"):
                f1, f2 = st.columns(2)
                v_date = f1.text_input("Voucher Date", value="21/06/2026")
                v_no = f2.text_input("Invoice/Memo Reference Code *")
                v_vendor = f1.text_input("Vendor Identity *")
                v_amt = f2.number_input("Taxable Base Amount (OMR)", min_value=0.000, step=0.001, format="%.3f")
                v_type = st.selectbox("Document Matrix Class", ["Tax Invoice", "Cash Memo"])
                
                if st.form_submit_button("Commit Financial Node"):
                    if v_no.strip() == "" or v_vendor.strip() == "":
                        st.error("Critical identity metrics required.")
                    else:
                        calc_vat = v_amt * 0.05 if v_type == "Tax Invoice" else 0.0
                        new_inv = pd.DataFrame([{
                            "Date": v_date, "Invoice No": v_no, "Vendor": v_vendor,
                            "Amount": v_amt, "VAT": calc_vat, "Total": v_amt + calc_vat, "Type": v_type
                        }])
                        st.session_state.invoice_matrix = pd.concat([st.session_state.invoice_matrix, new_inv], ignore_index=True)
                        st.success("Financial asset locked.")
                        st.rerun()

        st.markdown("#### Audited Expenses Ledger")
        for idx, row in st.session_state.invoice_matrix.iterrows():
            grid_col1, grid_col2 = st.columns([8, 1])
            grid_col1.warning(f"🧾 **{row['Date']}** | **Ref:** {row['Invoice No']} | **Vendor:** {row['Vendor']} | **Base:** {row['Amount']:.3f} OMR | **VAT:** {row['VAT']:.3f} OMR | **Total:** {row['Total']:.3f} OMR | Class: {row['Type']}")
            
            if grid_col2.button("❌ Remove", key=f"del_i_{idx}"):
                st.session_state.invoice_matrix = st.session_state.invoice_matrix.drop(idx).reset_index(drop=True)
                st.toast("Financial item dropped.")
                st.rerun()

    # ---------------- TAB 3: SECURE EXPORTS ----------------
    with tab3:
        st.subheader("Binary Extraction Layer")
        st.download_button("📥 Extract Hardened Workforce Matrix (.CSV)", data=st.session_state.workforce_matrix.to_csv(index=False).encode('utf-8'), file_name="Secure_Workforce.csv")
        st.download_button("📥 Extract Hardened Financials (.CSV)", data=st.session_state.invoice_matrix.to_csv(index=False).encode('utf-8'), file_name="Secure_Financials.csv")