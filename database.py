import streamlit as st
import pandas as pd
import hashlib

def hash_verified_credentials(password_string):
    """Generates strict cryptographic SHA-256 tokens."""
    return hashlib.sha256(password_string.strip().encode()).hexdigest()

def verify_session_handshake(username, password):
    """Bypasses file configuration errors by checking hashes directly in memory."""
    SECURE_USER = "admin@construction.om"
    # Sahi SHA-256 Hash bina kisi zero typo ke
    SECURE_HASH = "6ce8e390c29759d57a9cf719bf3000b91e92025345718dfd0e3ecf5228519e49"
    
    input_hash = hash_verified_credentials(password)
    return username.strip() == SECURE_USER and input_hash == SECURE_HASH

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