import streamlit as st

# --- LOGIN SYSTEM ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔒 Secure Partner Portal")
    st.subheader("Mamo Construction Firm - Oman")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Yahan aap apna pasandeda username aur password rakh sakte hain
        if username == "admin@construction.om" and password == "Mufms6858@#":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Ghalat Username ya Password! Dobara koshish karein.")
    st.stop() # Agar login nahi hua toh baqi niche wala code nahi chalega

# -------------------------------------------------------------
# AAPKA PURANA CODE IS LINE KE NICHE AISE HI REHNA CHAHIYE:
# -------------------------------------------------------------
st.title("💼 Workforce Management & Live Payroll System")
# ... baqi sara code niche chalne do
import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Workforce & Payroll Portal", layout="wide")
st.title("💼 Workforce Management & Live Payroll System")
st.markdown("---")

# ---- PARAMETERS ----
DAILY_RATE = 10  # Isko aap baad me mamo ke mutabiq change kar sakte hain
DB_FILE = "attendance_db.csv"

# "image_907122.jpg" ke mutabiq permanent labor list
LABOR_MASTER = [
    {"id": "92476849", "name": "Mohammad Shahid", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "109748895", "name": "M.Usman", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "136299814", "name": "Jahanzeb Afzal", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "79705332", "name": "Abdul khaliq", "company": "Rimal. AL", "scope": "Civil"},
    {"id": "91385487", "name": "Murtuza", "company": "Ahmed AL", "scope": "Civil"},
    {"id": "136025677", "name": "USAMA IJAZ", "company": "Sahool Wadi Trading", "scope": "Civil"},
    {"id": "135028261", "name": "M.Usama", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "134607323", "name": "Shahid Ahmad", "company": "Abu Hisham Al Riyami Trading", "scope": "Civil"},
    {"id": "129149239", "name": "ANWAR AHMAD", "company": "Abu Sultan Al Hajri Trading", "scope": "Civil"},
    {"id": "128565626", "name": "AKRAMUL HAQUE", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "99092783", "name": "IJAZ AHMAD", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "100018149", "name": "JAVED BOOTA", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "137686123", "name": "AZID ALI", "company": "MillenniumBuildingTrading", "scope": "Civil"},
    {"id": "135028223", "name": "MUHAMMAD NAVEED", "company": "Rubhan. T", "scope": "Civil"},
    {"id": "136138983", "name": "GHULAM MOHI UD DIN", "company": "AtSafaDistinguishedProject", "scope": "Civil"},
    {"id": "131430865", "name": "MUHAMMAD WASEEM", "company": "Al-AhramAlMutajaddidaLLC", "scope": "Civil"},
    {"id": "126755181", "name": "AHSAN LI", "company": "RizwanAliTrading&Contracting", "scope": "Civil"}
]

# ---- BACKEND DATABASE SETUP ----
if not os.path.exists(DB_FILE):
    df_empty = pd.DataFrame(columns=["Date", "Employee_ID", "Name", "Company", "Status", "Remarks"])
    df_empty.to_csv(DB_FILE, index=False)

def load_data():
    return pd.read_csv(DB_FILE)

def save_attendance(date_str, attendance_dict, remarks_dict):
    df = load_data()
    df = df[df["Date"] != date_str]
    
    new_entries = []
    for emp in LABOR_MASTER:
        emp_id = emp["id"]
        status = "Present" if attendance_dict[emp_id] else "Absent"
        rem = remarks_dict.get(emp_id, "")
        new_entries.append({
            "Date": date_str,
            "Employee_ID": emp_id,
            "Name": emp["name"],
            "Company": emp["company"],
            "Status": status,
            "Remarks": rem
        })
    
    df_new = pd.DataFrame(new_entries)
    df_combined = pd.concat([df, df_new], ignore_index=True)
    df_combined.to_csv(DB_FILE, index=False)

# ---- FRONTEND TABS ----
tab1, tab2, tab3 = st.tabs(["📝 Daily Attendance Entry", "📊 Live Dashboard", "💰 Month-End Payroll"])

with tab1:
    st.subheader("Enter Attendance From Group Sheets")
    selected_date = st.date_input("Select Sheet Date", datetime.now())
    date_str = selected_date.strftime("%Y-%m-%d")
    
    st.markdown("### Labor List")
    
    auth_dict = {}
    rem_dict = {}
    
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 2])
    col1.markdown("**Employee ID**")
    col2.markdown("**Name**")
    col3.markdown("**Company**")
    col4.markdown("**Status**")
    col5.markdown("**Remarks (Optional)**")
    
    for emp in LABOR_MASTER:
        c1, c2, c3, c4, c5 = st.columns([1, 2, 2, 1, 2])
        c1.text(emp["id"])
        c2.text(emp["name"])
        c3.text(emp["company"])
        auth_dict[emp["id"]] = c4.checkbox("Present", value=True, key=f"p_{emp['id']}")
        rem_dict[emp["id"]] = c5.text_input("N/S, Leave etc.", key=f"r_{emp['id']}", label_visibility="collapsed")
        
    if st.button("💾 Save & Sync Data", type="primary"):
        save_attendance(date_str, auth_dict, rem_dict)
        st.success(f"Data successfully synced for {date_str}!")

with tab2:
    st.subheader("Real-Time Analytics")
    df_dash = load_data()
    
    if not df_dash.empty:
        total_days_tracked = df_dash["Date"].nunique()
        total_presents = len(df_dash[df_dash["Status"] == "Present"])
        total_payout = total_presents * DAILY_RATE
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Days Recorded", total_days_tracked)
        m2.metric("Total Attendance Hits", total_presents)
        m3.metric("Estimated Running Payout", f"{total_payout} OMR")
        
        st.markdown("### Raw History View")
        st.dataframe(df_dash, use_container_width=True)
    else:
        st.info("No attendance data found. Start entering from Tab 1.")

with tab3:
    st.subheader("Automated Monthly Payroll Engine")
    df_pay = load_data()
    
    if not df_pay.empty:
        df_present_only = df_pay[df_pay["Status"] == "Present"]
        if not df_present_only.empty:
            summary = df_present_only.groupby(["Employee_ID", "Name", "Company"]).size().reset_index(name="Days_Present")
            summary["Daily_Rate"] = DAILY_RATE
            summary["Total_Salary_Due"] = summary["Days_Present"] * summary["Daily_Rate"]
            
            st.markdown("### Final Monthly Salary Statement")
            st.dataframe(summary, use_container_width=True)
            
            csv_data = summary.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Payroll Report (Excel/CSV)",
                data=csv_data,
                file_name=f"payroll_report_{datetime.now().strftime('%B_%Y')}.csv",
                mime="text/csv",
            )
        else:
            st.info("No 'Present' data recorded yet to calculate payroll.")
    else:
        st.info("No data available to calculate salary yet.")