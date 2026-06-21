import streamlit as st
import pandas as pd
import os
from database import load_secure_repository, verify_session_handshake

st.set_page_config(page_title="Al Rabhan Operational Vault", layout="wide", page_icon="🔒")

# Inject Custom UI Theme
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_secure_repository()

if "auth_token_verified" not in st.session_state:
    st.session_state.auth_token_verified = False

# ==========================================
# GATEWAY SCREEN (Direct Logic Validation)
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
                # Directly calling memory-mapped verification mechanism
                if verify_session_handshake(input_user, input_pass):
                    st.session_state.auth_token_verified = True
                    st.rerun()
                else:
                    st.error("Authentication Violation: Invalid Signature Keys logged.")

# ==========================================
# APPLICATION CORE
# ==========================================
else:
    head_col1, head_col2 = st.columns([8, 2])
    head_col1.markdown("<h1 style='color: #5ab4ff;'>🏗️ AL RABHAN TRADING - Control Center</h1>", unsafe_allow_html=True)
    if head_col2.button("Terminate Secure Session", type="primary", use_container_width=True):
        st.session_state.auth_token_verified = False
        st.rerun()
        
    st.markdown("---")
    tab1, tab2 = st.tabs(["📝 Daily Attendance Matrix Logging Panel", "📄 Tax Invoices & Receipts Hub"])
    
    with tab1:
        st.markdown("### Active Workforce Roster")
        for idx, row in st.session_state.workforce_matrix.iterrows():
            grid_col1, grid_col2 = st.columns([12, 1])
            grid_col1.info(f"📅 **{row['Date']}** | **ID:** {row['Employee ID']} | **Name:** {row['Name']} | **Company:** {row['Company']} | **Status:** {row['Status']}")
            if grid_col2.button("🗑️", key=f"del_w_{idx}"):
                st.session_state.workforce_matrix = st.session_state.workforce_matrix.drop(idx).reset_index(drop=True)
                st.rerun()

    with tab2:
        st.markdown("### Corporate Receipts Ledger")
        for idx, row in st.session_state.invoice_matrix.iterrows():
            grid_col1, grid_col2 = st.columns([12, 1])
            grid_col1.warning(f"🧾 **{row['Date']}** | **Ref:** {row['Invoice No']} | **Vendor:** {row['Vendor']} | **Total:** {row['Total']:.3f} OMR")
            if grid_col2.button("🗑️", key=f"del_i_{idx}"):
                st.session_state.invoice_matrix = st.session_state.invoice_matrix.drop(idx).reset_index(drop=True)
                st.rerun()