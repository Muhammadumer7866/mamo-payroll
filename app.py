import streamlit as st
import pandas as pd
import os
from database import load_secure_repository, verify_session_handshake

st.set_page_config(page_title="Al Rabhan Operational Vault", layout="wide", page_icon="🔒")

# Load Styles Securely from separate CSS script file
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
        st.markdown("<h2 style='text-align: center; color: #5ab4ff;'>AL RABHAN TRADING</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #a4b0be;'>Secure Operations Gateway Ledger</p>", unsafe_allow_html=True)
        
        with st.form("hardened_login_gateway"):
            input_user = st.text_input("Corporate Access ID")
            input_pass = st.text_input("Cryptographic Access Key", type="password")
            
            if st.form_submit_button("Authenticate Session", type="primary"):
                if verify_session_handshake(input_user, input_pass):
                    st.session_state.auth_token_verified = True
                    st.rerun()
                else:
                    st.error("Authentication Violation: Invalid Signature Keys logged.")

# ==========================================
# APPLICATION CORE
# ==========================================
else:
    st.markdown("<h1 style='color: #5ab4ff;'>🏗️ Control Panel Core</h1>", unsafe_allow_html=True)
    if st.button("Terminate Secure Session"):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    tab1, tab2 = st.tabs(["📝 Workforce Roster Matrix", "📄 Invoices Hub"])
    
    with tab1:
        st.subheader("Field Deployment Data Streams")
        
        # Row Action Engine for exact dynamic target removal
        for idx, row in st.session_state.workforce_matrix.iterrows():
            r_col1, r_col2 = st.columns([9, 1])
            r_col1.info(f"📅 {row['Date']} | ID: {row['Employee ID']} | {row['Name']} | {row['Company']} | Status: {row['Status']}")
            
            # Cursor Target Click Drop
            if r_col2.button("❌", key=f"del_w_{idx}"):
                st.session_state.workforce_matrix = st.session_state.workforce_matrix.drop(idx).reset_index(drop=True)
                st.rerun()
                
    with tab2:
        st.subheader("Financial Ledger Inbound Steaming")
        for idx, row in st.session_state.invoice_matrix.iterrows():
            r_col1, r_col2 = st.columns([9, 1])
            r_col1.warning(f"🧾 {row['Date']} | Ref: {row['Invoice No']} | Vendor: {row['Vendor']} | Total: {row['Total']:.3f} OMR ({row['Type']})")
            
            if r_col2.button("❌", key=f"del_i_{idx}"):
                st.session_state.invoice_matrix = st.session_state.invoice_matrix.drop(idx).reset_index(drop=True)
                st.rerun()