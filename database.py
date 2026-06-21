import streamlit as st
import pandas as pd

def verify_session_handshake(username, password):
    SECURE_USER = "admin@construction.om"
    SECURE_PASSWORD = "Oman#Secure2026"
    return username.strip() == SECURE_USER and password.strip() == SECURE_PASSWORD

def load_secure_repository():
    # 1. Master lookup database for dynamic search
    if 'master_workers' not in st.session_state:
        st.session_state.master_workers = pd.DataFrame([
            {"Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil"},
            {"Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed AL", "Scope": "Civil"},
            {"Employee ID": "136025677", "Name": "USAMA IJAZ", "Company": "Sahool Wadi Trading", "Scope": "Civil"},
            {"Employee ID": "135028281", "Name": "M.Usama", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "134607323", "Name": "Shahid Ahmad", "Company": "Abu Hisham Al Riyami Trading", "Scope": "Civil"},
            {"Employee ID": "129149239", "Name": "ANWAR AHMAD", "Company": "Abu Sultan Al Hajri Trading Enterprises LLC", "Scope": "Civil"},
            {"Employee ID": "128565626", "Name": "AKRAMUL HAQUE", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "99092783", "Name": "IJAZ AHMAD", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "100018149", "Name": "JAVED BOOTA", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "137686123", "Name": "AZID ALI", "Company": "MillenniumBuildingTrading&ContractingLLC", "Scope": "Civil"},
            {"Employee ID": "135028223", "Name": "MUHAMMAD NAVEED", "Company": "Al Rubhan Trading", "Scope": "Civil"},
            {"Employee ID": "136138983", "Name": "GHULAM MOHI UD DIN", "Company": "AlSafaDistinguishedProject", "Scope": "Civil"},
            {"Employee ID": "131430865", "Name": "MUHAMMAD WASEEM", "Company": "Al-AhramAlMutajaddidaLLC", "Scope": "Civil"},
            {"Employee ID": "126755181", "Name": "AHSAN ALI", "Company": "RizwanAliTrading&ContractingLLC", "Scope": "Civil"},
            {"Employee ID": "111562542", "Name": "Mohamed Ayub", "Company": "THE MODERN GOLDEN RAY", "Scope": "Civil"},
            {"Employee ID": "107776911", "Name": "Emarat Khalasi", "Company": "The Mahmoud Amer Al Alawi Trading Co", "Scope": "Civil"},
            {"Employee ID": "124816435", "Name": "MOHAMMED SAYMON", "Company": "THE JALAAN AL-ALAMIYA TRADING", "Scope": "Civil"},
            {"Employee ID": "Moza_Khan", "Name": "Moza Khan", "Company": "Al Rubhan Trading", "Scope": "Civil"}
        ])

    # 2. Main Attendance Data Matrix (20 & 21 June Logs Complete Form)
    if 'workforce_matrix' not in st.session_state:
        st.session_state.workforce_matrix = pd.DataFrame([
            # 20-06-2026 Sheet
            {"Date": "20/06/2026", "Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "109748895", "Name": "M.Usman", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed AL", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "136025677", "Name": "USAMA IJAZ", "Company": "Sahool Wadi Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "135028281", "Name": "M.Usama", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "134607323", "Name": "Shahid Ahmad", "Company": "Abu Hisham Al Riyami Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "129149239", "Name": "ANWAR AHMAD", "Company": "Abu Sultan Al Hajri Trading Enterprises LLC", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "128565626", "Name": "AKRAMUL HAQUE", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "99092783", "Name": "IJAZ AHMAD", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "100018149", "Name": "JAVED BOOTA", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "137686123", "Name": "AZID ALI", "Company": "MillenniumBuildingTrading&ContractingLLC", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "135028223", "Name": "MUHAMMAD NAVEED", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "136138983", "Name": "GHULAM MOHI UD DIN", "Company": "AlSafaDistinguishedProject", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "131430865", "Name": "MUHAMMAD WASEEM", "Company": "Al-AhramAlMutajaddidaLLC", "Scope": "Civil", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "126755181", "Name": "AHSAN ALI", "Company": "RizwanAliTrading&ContractingLLC", "Scope": "Civil", "Status": "Present"},
            
            # 21-06-2026 Sheet
            {"Date": "21/06/2026", "Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "N/S"},
            {"Date": "21/06/2026", "Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"},
            {"Date": "21/06/2026", "Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil", "Status": "Present"},
            {"Date": "21/06/2026", "Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed AL", "Scope": "Civil", "Status": "Present"},
            {"Date": "21/06/2026", "Employee ID": "99092783", "Name": "IJAZ AHMAD", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "N/S"},
            {"Date": "21/06/2026", "Employee ID": "Moza_Khan", "Name": "Moza Khan", "Company": "Al Rubhan Trading", "Scope": "Civil", "Status": "Present"}
        ])
        
    if 'invoice_matrix' not in st.session_state:
        st.session_state.invoice_matrix = pd.DataFrame([
            {"Date": "20/06/2026", "Invoice No": "A204306", "Vendor": "Al Inma Materials L.L.C.", "Amount": 338.600, "VAT": 16.930, "Total": 355.530, "Type": "Tax Invoice"},
            {"Date": "21/06/2026", "Invoice No": "1801", "Vendor": "Lulu Dhofar International LLC", "Amount": 9.600, "VAT": 0.000, "Total": 9.600, "Type": "Cash Memo"}
        ])