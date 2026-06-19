import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Configuration (Must be the very first Streamlit command)
st.set_page_config(page_title="Workforce & Payroll Portal", layout="wide")

# --- CUSTOM SECURITY & CORPORATE THEME (CSS) ---
st.markdown("""
    <style>
    /* Overall Background and Font */
    .stApp {
        background-color: #11141a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Login Card Container */
    .login-box {
        background: linear-gradient(145deg, #1e222b, #151922);
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #2d3545;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 50px;
    }
    
    /* Premium Header Design */
    .main-title {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: 1px;
        text-align: center;
        border-bottom: 2px solid #00E5FF;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }
    
    /* Metric Cards for Dashboard */
    .metric-card {
        background-color: #1e222b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00E5FF;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- SECURE LOGIN SYSTEM ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align: center; color: #00E5FF; margin-bottom: 5px;">Al-Rimal & Rubhan</h2>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #8a99ad; font-size: 14px; margin-bottom: 30px;">PARTNER PORTAL — OMAN FIRM</p>', unsafe_allow_html=True)
        
        username = st.text_input("Corporate ID / Email")
        password = st.text_input("Access Key", type="password")
        
        st.markdown('<br>', unsafe_allow_html=True)
        if st.button("Secure Login", use_container_width=True):
            if username == "admin@construction.om" and password == "Oman#Secure2026":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Authentication Failed. Invalid credentials.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- HARDCODED LABOR DATA (Aapka Asal Data Back!) ---
labor_data = [
    {"Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Rubhan. T"},
    {"Employee ID": "109748895", "Name": "M.Usman", "Company": "Rubhan. T"},
    {"Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Rubhan. T"},
    {"Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL"},
]
df_labor = pd.DataFrame(labor_data)

# --- MAIN PREMIUM PORTAL CONTENT ---
st.markdown('<h1 class="main-title">💼 OVERSEAS WORKFORCE & LIVE PAYROLL SYSTEM</h1>', unsafe_allow_html=True)

# Top Row: Navigation / Tabs
tab1, tab2, tab3 = st.tabs(["📝 Daily Attendance Entry", "📊 Executive Analytics Dashboard", "💰 Month-End Payroll"])

with tab1:
    st.subheader("Enter Attendance From Group Sheets")
    sheet_date = st.date_input("Select Sheet Date", datetime.now())
    
    st.markdown('### Active Labor Roster')
    
    # Loop to generate dynamic attendance checkboxes with data back
    attendance_results = []
    for index, row in df_labor.iterrows():
        col_id, col_name, col_comp, col_status, col_rem = st.columns([1, 2, 1.5, 1, 2.5])
        with col_id:
            st.write(row["Employee ID"])
        with col_name:
            st.write(row["Name"])
        with col_comp:
            st.write(row["Company"])
        with col_status:
            status = st.checkbox("Present", key=f"status_{row['Employee ID']}", value=True)
        with col_rem:
            remarks = st.text_input("", key=f"rem_{row['Employee ID']}", placeholder="Remarks (Optional)")
            
        attendance_results.append({
            "Employee ID": row["Employee ID"],
            "Name": row["Name"],
            "Company": row["Company"],
            "Status": "Present" if status else "Absent",
            "Remarks": remarks
        })

with tab2:
    st.subheader("Oman Operations Overview")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><h4 style="color:#8a99ad;margin:0;">Total Strength</h4><h2 style="color:#fff;margin:5px 0;">148 Crew Members</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card" style="border-left-color:#2ecc71;"><h4 style="color:#8a99ad;margin:0;">Present Today</h4><h2 style="color:#2ecc71;margin:5px 0;">142 Active</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card" style="border-left-color:#e74c3c;"><h4 style="color:#8a99ad;margin:0;">Flagged Absents</h4><h2 style="color:#e74c3c;margin:5px 0;">6 Personnel</h2></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Payroll Summary Generation")
    st.write("Automated Omani Rial (OMR) currency conversions and bank transfer sheets.")