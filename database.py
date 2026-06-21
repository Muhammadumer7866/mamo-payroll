import streamlit as st
import pandas as pd

def init_databases():
    # Roster Database Setup (No PPE, 20 June Target Default)
    if 'workforce_db' not in st.session_state:
        st.session_state.workforce_db = pd.DataFrame([
            {"Date": "20/06/2026", "Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "-", "Time Out": "-", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "109748895", "Name": "M.Usman", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "-", "Time Out": "-", "Status": "N/S"},
            {"Date": "20/06/2026", "Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed. AL", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "136025677", "Name": "USAMA IJAZ", "Company": "Sahool Wadi Trading", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "135028261", "Name": "M.Usama", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "134607323", "Name": "Shahid Ahmad", "Company": "Abu Hisham Al Riyami Trading", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "129149239", "Name": "ANWAR AHMAD", "Company": "Abu Sultan Al Hajri Trading Entities LLC", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"},
            {"Date": "20/06/2026", "Employee ID": "128565626", "Name": "AKRAMUL HAQUE", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "Status": "Present"}
        ])

    # Invoice Database Setup
    if 'invoice_db' not in st.session_state:
        st.session_state.invoice_db = pd.DataFrame([
            {"Invoice/Receipt No": "A204306", "Date": "20/06/2026", "Vendor/Supplier": "Al Inma Building Materials L.L.C.", "Description": "Marsbit P 4mm", "Taxable Base (OMR)": 338.600, "VAT Amount (5%)": 16.930, "Gross Total (OMR)": 355.530, "Type": "Tax Invoice"},
            {"Invoice/Receipt No": "Cash Memo", "Date": "20/06/2026", "Vendor/Supplier": "Lulu Dhofar International LLC", "Description": "Safety Pant-Shirt", "Taxable Base (OMR)": 4.800, "VAT Amount (5%)": 0.000, "Gross Total (OMR)": 4.800, "Type": "Cash Purchase"}
        ])