import streamlit as st
import pandas as pd

def verify_session_handshake(username, password):
    SECURE_USER = "admin@construction.om"
    SECURE_PASSWORD = "Oman#Secure2026"
    return username.strip() == SECURE_USER and password.strip() == SECURE_PASSWORD

def load_secure_repository():
    # 1. Master Database of Registered Workers (For Auto-Lookup)
    if 'master_workers' not in st.session_state:
        st.session_state.master_workers = pd.DataFrame([
            {"Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "109748895", "Name": "M.Usman", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil"},
            {"Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed AL", "Scope": "Civil"},
            {"Employee ID": "136025677", "Name": "USAMA IJAZ", "Company": "Sahool Wadi Trading", "Scope": "Civil"},
            {"Employee ID": "135028281", "Name": "M.Usama", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "134607323", "Name": "Shahid Ahmad", "Company": "Abu Hisham Al Riyami Trading", "Scope": "Civil"},
            {"Employee ID": "129149239", "Name": "ANWAR AHMAD", "Company": "Abu Sultan Al Hajri Trading Enterprises LLC", "Scope": "Civil"},
            {"Employee ID": "128565626", "Name": "AKRAMUL HAQUE", "Company": "Al Rubhan Trading", "Scope": "Civil"}
        ])

    # 2. Master Database of Vendors
    if 'master_vendors' not in st.session_state:
        st.session_state.master_vendors = {
            "INV-ALINMA": "Al Inma Materials L.L.C.",
            "INV-LULU": "Lulu Dhofar International LLC"
        }

    # 3. Active Daily Attendance Log
    if 'workforce_matrix' not in st.session_state:
        st.session_state.workforce_matrix = pd.DataFrame([
            {"Date": "20/06/2026", "Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "109748895", "Name": "M.Usman", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "21/06/2026", "Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil", "Status": "Present"},
            {"Date": "21/06/2026", "Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed AL", "Scope": "Civil", "Status": "Present"}
        ])
        
    # 4. Active Invoice Log
    if 'invoice_matrix' not in st.session_state:
        st.session_state.invoice_matrix = pd.DataFrame([
            {"Date": "20/06/2026", "Invoice No": "A204306", "Vendor": "Al Inma Materials L.L.C.", "Amount": 338.600, "VAT": 16.930, "Total": 355.530, "Type": "Tax Invoice"},
            {"Date": "21/06/2026", "Invoice No": "1801", "Vendor": "Lulu Dhofar International LLC", "Amount": 9.600, "VAT": 0.000, "Total": 9.600, "Type": "Cash Memo"}
        ])