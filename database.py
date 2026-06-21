import streamlit as st
import pandas as pd

def verify_session_handshake(username, password):
    """Bypasses hashing issues by doing a direct secure string match."""
    SECURE_USER = "admin@construction.om"
    SECURE_PASSWORD = "Oman#Secure2026"
    
    # Dono username aur password ko direct check karein bina kisi complex hash ke
    return username.strip() == SECURE_USER and password.strip() == SECURE_PASSWORD

def load_secure_repository():
    """Initializes persistent workforce and financial states."""
    if 'workforce_matrix' not in st.session_state:
        st.session_state.workforce_matrix = pd.DataFrame([
            {"Date": "20/06/2026", "Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "-", "Time Out": "-", "PPE": "-", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "109748895", "Name": "M.Usman", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "-", "Time Out": "-", "PPE": "-", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed. AL", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"}
        ])
        
    if 'invoice_matrix' not in st.session_state:
        st.session_state.invoice_matrix = pd.DataFrame([
            {"Date": "20/06/2026", "Invoice No": "A204306", "Vendor": "Al Inma Materials L.L.C.", "Amount": 338.600, "VAT": 16.930, "Total": 355.530, "Type": "Tax Invoice"},
            {"Date": "21/06/2026", "Invoice No": "1801", "Vendor": "Lulu Dhofar International LLC", "Amount": 9.600, "VAT": 0.000, "Total": 9.600, "Type": "Cash Memo"}
        ])