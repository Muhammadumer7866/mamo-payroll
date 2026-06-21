import streamlit as st
import pandas as pd
import os
import base64
from database import init_databases

# Page Configuration
st.set_page_config(page_title="Al Rabhan Trading", page_icon="🏗️", layout="wide")

# Initialize Databases from Module
init_databases()

# Load External CSS Portion
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Image Base64 Injection Logic
def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f: return base64.b64encode(f.read()).decode()
    return None

logo_main_file = "ChatGPT Image Jun 20, 2026, 02_56_40 PM.png"
logo_bg_file = "image_436736.png"
bg_b64 = get_b64(logo_bg_file)

if bg_b64:
    st.markdown(f'<style>.stApp {{ background-image: linear-gradient(rgba(14,17,23,0.94), rgba(14,17,23,0.94)), url("data:image/png;base64,{bg_b64}"); }}</style>', unsafe_allow_html=True)

# Auth Validation State
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ==========================================
# GATEWAY PORTION
# ==========================================
if not st.session_state.logged_in:
    main_logo_b64 = get_b64(logo_main_file)
    if main_logo_b64:
        st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{main_logo_b64}" style="width: 400px;"></div>', unsafe_allow_html=True)
    
    st.subheader("System Authentication Gate")
    u = st.text_input("User ID", value="admin@construction.om")
    p = st.text_input("Password", type="password", value="Oman#Secure2026")
    if st.button("Log In", type="primary"):
        if u == "admin@construction.om" and p == "Oman#Secure2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Access Denied.")

# ==========================================
# CORE DASHBOARD SYSTEM PORTION
# ==========================================
else:
    st.title("AL RABHAN TRADING OPERATIONS SYSTEM")
    st.info("📅 Selected Ledger Target Focus: 20/06/2026")
    
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

    tab1, tab2, tab3, tab4 = st.tabs([
        "🏠 Corporate Command Hub", 
        "📝 Daily Attendance Matrix", 
        "📄 Tax Invoices Registry", 
        "📊 Corporate Reports Export"
    ])

    # --- PORTION 1: HUB OVERVIEW ---
    with tab1:
        st.subheader("📊 Real-Time Matrix Summary")
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Workforce On Log", f"{len(st.session_state.workforce_db)} Men")
        m2.metric("Active Tax Invoices", f"{len(st.session_state.invoice_db)} Receipts")
        m3.metric("Gross Logged Vol (OMR)", f"{st.session_state.invoice_db['Gross Total (OMR)'].sum():.3f} OMR")

    # --- PORTION 2: ATTENDANCE & LOOKUP SMART PORTION ---
    with tab2:
        st.subheader("📝 Attendance Registration Panel")
        
        # Smart Autocomplete Engine
        search_id = st.text_input("🔍 Quick Auto-Fill Link: Type Employee ID:")
        auto_name, auto_comp, auto_scope = "", "Rubhan. T", "Civil"
        
        if search_id.strip():
            match = st.session_state.workforce_db[st.session_state.workforce_db["Employee ID"] == search_id.strip()]
            if not match.empty:
                auto_name = match.iloc[-1]["Name"]
                auto_comp = match.iloc[-1]["Company"]
                auto_scope = match.iloc[-1]["Scope"]
                st.toast("🎯 Auto-Fill Data Pre-loaded Successfully!")

        with st.form("worker_add_form"):
            col1, col2, col3 = st.columns(3)
            f_date = col1.text_input("Date", value="20/06/2026")
            f_id = col2.text_input("Employee ID *", value=search_id)
            f_name = col3.text_input("Worker Name *", value=auto_name)
            
            col4, col5, col6 = st.columns(3)
            f_comp = col4.text_input("Company/Subcontractor", value=auto_comp)
            f_scope = col5.selectbox("Scope", ["Civil", "Mechanical", "Electrical"], index=0)
            f_stat = col6.selectbox("Status", ["Present", "N/S", "Absent"])
            
            if st.form_submit_button("Save Entry"):
                if f_id.strip() and f_name.strip():
                    new_w = {"Date": f_date, "Employee ID": f_id.strip(), "Name": f_name.strip(), "Company": f_comp, "Scope": f_scope, "Time In": "7:00 AM" if f_stat=="Present" else "-", "Time Out": "5:00 PM" if f_stat=="Present" else "-", "Status": f_stat}
                    st.session_state.workforce_db = pd.concat([st.session_state.workforce_db, pd.DataFrame([new_w])], ignore_index=True)
                    st.rerun()

        # DELETE PORTION (Worker Cleanup Row)
        st.markdown('<div class="delete-box"><h4>⚠️ Danger Zone: Remove Mistake/Wrong Worker Entry</h4></div>', unsafe_allow_html=True)
        if not st.session_state.workforce_db.empty:
            w_options = st.session_state.workforce_db.apply(lambda x: f"{x['Date']} | ID: {x['Employee ID']} | {x['Name']}", axis=1).tolist()
            to_delete_w = st.selectbox("Select wrong entry to delete permanently:", w_options)
            if st.button("🗑️ Delete Selected Worker Record", type="secondary"):
                idx = w_options.index(to_delete_w)
                st.session_state.workforce_db = st.session_state.workforce_db.drop(st.session_state.workforce_db.index[idx]).reset_index(drop=True)
                st.success("Entry removed successfully.")
                st.rerun()

        st.dataframe(st.session_state.workforce_db, use_container_width=True, hide_index=True)

    # --- PORTION 3: TAX INVOICES & REMOVAL PORTION ---
    with tab3:
        st.subheader("📄 Invoice Registry Hub")
        with st.form("invoice_add_form"):
            i1, i2 = st.columns(2)
            inv_no = i1.text_input("Invoice/Receipt Number *")
            inv_date = i2.text_input("Date", value="20/06/2026")
            inv_supp = i1.text_input("Supplier *")
            inv_base = i2.number_input("Base Amount (OMR)", min_value=0.0, format="%.3f")
            inv_type = st.selectbox("Classification", ["Tax Invoice", "Cash Purchase"])
            
            if st.form_submit_button("Commit Financial Record"):
                if inv_no.strip() and inv_supp.strip():
                    vat = inv_base * 0.05 if inv_type == "Tax Invoice" else 0.0
                    new_i = {"Invoice/Receipt No": inv_no, "Date": inv_date, "Vendor/Supplier": inv_supp, "Description": "Added Expense Material", "Taxable Base (OMR)": inv_base, "VAT Amount (5%)": vat, "Gross Total (OMR)": inv_base + vat, "Type": inv_type}
                    st.session_state.invoice_db = pd.concat([st.session_state.invoice_db, pd.DataFrame([new_i])], ignore_index=True)
                    st.rerun()

        # DELETE PORTION (Invoice Cleanup Row)
        st.markdown('<div class="delete-box"><h4>⚠️ Danger Zone: Remove Wrong Invoice Slip</h4></div>', unsafe_allow_html=True)
        if not st.session_state.invoice_db.empty:
            i_options = st.session_state.invoice_db.apply(lambda x: f"No: {x['Invoice/Receipt No']} | {x['Vendor/Supplier']} ({x['Gross Total (OMR)']} OMR)", axis=1).tolist()
            to_delete_i = st.selectbox("Select wrong receipt to clear:", i_options)
            if st.button("🗑️ Delete Selected Invoice Record", type="secondary"):
                idx_i = i_options.index(to_delete_i)
                st.session_state.invoice_db = st.session_state.invoice_db.drop(st.session_state.invoice_db.index[idx_i]).reset_index(drop=True)
                st.success("Invoice removed clean.")
                st.rerun()

        st.dataframe(st.session_state.invoice_db, use_container_width=True, hide_index=True)

    # --- PORTION 4: EXPORTS DOWNLOAD ---
    with tab4:
        st.subheader("📊 Secure Data Extraction")
        st.download_button("Export Roster CSV", data=st.session_state.workforce_db.to_csv(index=False).encode('utf-8'), file_name="Roster.csv", mime="text/csv")
        st.download_button("Export Financials CSV", data=st.session_state.invoice_db.to_csv(index=False).encode('utf-8'), file_name="Expenses.csv", mime="text/csv")