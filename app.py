import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Workforce Tracking Portal", layout="wide")

# --- CUSTOM CORPORATE THEME (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #11141a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .login-box {
        background: linear-gradient(145deg, #1e222b, #151922);
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #2d3545;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 50px;
    }
    .main-title {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: 1px;
        text-align: center;
        border-bottom: 2px solid #00E5FF;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }
    .metric-card {
        background-color: #1e222b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00E5FF;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-box {
        background-color: #1e222b;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #2d3545;
        margin-bottom: 20px;
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
            if username == "admin@construction.om" and password == "Mufms6858@#":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Authentication Failed. Invalid credentials.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- DATABASE PERSISTENCE INITIALIZATION ---
if 'master_labor_pool' not in st.session_state:
    st.session_state['master_labor_pool'] = [
        {"Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Rubhan. T"},
        {"Employee ID": "109748895", "Name": "M.Usman", "Company": "Rubhan. T"},
        {"Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Rubhan. T"},
        {"Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL"},
    ]

# Historical saved database entries
if 'attendance_database' not in st.session_state:
    st.session_state['attendance_database'] = []

# Current session workspace
if 'daily_active_roster' not in st.session_state:
    st.session_state['daily_active_roster'] = []

# --- MAIN APP INTERFACE ---
st.markdown('<h1 class="main-title">💼 OVERSEAS WORKFORCE & TRACKING SYSTEM</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📝 Daily Attendance Entry", "📊 Executive Analytics Dashboard", "📅 Month-End Attendance Report"])

with tab1:
    st.subheader("Daily Roster Management")
    sheet_date = st.date_input("Select Sheet Date", datetime.now())
    
    col_left, col_right = st.columns(2)
    
    # PANEL 1: SEARCH & AUTO-FILL PREVIOUS LABOR
    with col_left:
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #00E5FF; margin-top:0;'>🔍 Add Worker from Previous Records</h4>", unsafe_allow_html=True)
        
        search_query = st.text_input("Search by Name or ID Number", placeholder="Type name or ID and hit Enter...")
        
        if search_query:
            # Filter master database matching criteria
            matches = [w for w in st.session_state['master_labor_pool'] if search_query.lower() in w['Name'].lower() or search_query in w['Employee ID']]
            
            if matches:
                st.markdown("<p style='color: #2ecc71; font-size: 13px;'>Matches found:</p>", unsafe_allow_html=True)
                for matched_worker in matches:
                    if st.button(f"Add {matched_worker['Name']} ({matched_worker['Employee ID']})", key=f"match_{matched_worker['Employee ID']}"):
                        if any(w['Employee ID'] == matched_worker['Employee ID'] for w in st.session_state['daily_active_roster']):
                            st.warning("Worker is already added to today's active roster list.")
                        else:
                            st.session_state['daily_active_roster'].append({
                                "Employee ID": matched_worker["Employee ID"],
                                "Name": matched_worker["Name"],
                                "Company": matched_worker["Company"],
                                "Remarks": ""
                            })
                            st.success(f"Added {matched_worker['Name']} to today's list.")
                            st.rerun()
            else:
                st.error("No worker matching this criteria found in historical records.")
        st.markdown('</div>', unsafe_allow_html=True)

    # PANEL 2: ADD BRAND NEW LABOR
    with col_right:
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #2ecc71; margin-top:0;'>➕ Register Brand New Labor</h4>", unsafe_allow_html=True)
        
        new_id = st.text_input("New Employee ID", placeholder="e.g. 55667788")
        new_name = st.text_input("Full Name", placeholder="e.g. Zahid Ahmed")
        new_comp = st.text_input("Company Name", placeholder="e.g. Rubhan. T")
        
        if st.button("Register & Add to Sheet", use_container_width=True):
            if new_id and new_name and new_comp:
                if any(w['Employee ID'] == new_id for w in st.session_state['master_labor_pool']):
                    st.error("Registration failed. This Employee ID already exists in the system database.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": new_id, "Name": new_name, "Company": new_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": new_id, "Name": new_name, "Company": new_comp, "Remarks": ""})
                    st.success("New worker successfully registered and deployed to active roster.")
                    st.rerun()
            else:
                st.warning("Please fill out all missing worker validation data blocks.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #2d3545;'>", unsafe_allow_html=True)
    
    # DISPLAY AREA WITH REMOVE OPTION
    st.markdown('### 📋 Current Active Roster List')
    
    if not st.session_state['daily_active_roster']:
        st.info("Today's roster sheet is empty. Add active field labor using the search or registration blocks above.")
    else:
        h_id, h_name, h_comp, h_status, h_rem, h_action = st.columns([1, 2, 1.5, 1, 2, 1])
        h_id.markdown("**ID**")
        h_name.markdown("**Name**")
        h_comp.markdown("**Company**")
        h_status.markdown("**Status**")
        h_rem.markdown("**Remarks**")
        h_action.markdown("**Action**")
        
        to_remove = None
        for idx, worker in enumerate(st.session_state['daily_active_roster']):
            col_id, col_name, col_comp, col_status, col_rem, col_action = st.columns([1, 2, 1.5, 1, 2, 1])
            with col_id:
                st.write(worker["Employee ID"])
            with col_name:
                st.write(worker["Name"])
            with col_comp:
                st.write(worker["Company"])
            with col_status:
                st.markdown("<span style='color:#2ecc71; font-weight:bold;'>✔ Present</span>", unsafe_allow_html=True)
            with col_rem:
                st.session_state['daily_active_roster'][idx]["Remarks"] = st.text_input(
                    "", key=f"rem_{worker['Employee ID']}_{idx}", 
                    value=worker["Remarks"], placeholder="Remarks (Optional)", label_visibility="collapsed"
                )
            with col_action:
                if st.button("❌ Remove", key=f"del_{worker['Employee ID']}_{idx}"):
                    to_remove = idx
                    
        if to_remove is not None:
            st.session_state['daily_active_roster'].pop(to_remove)
            st.rerun()
                
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Finalize & Lock Daily Attendance Report", type="primary", use_container_width=True):
            # Save the currently prepared roster to persistent history log
            for item in st.session_state['daily_active_roster']:
                st.session_state['attendance_database'].append({
                    "Date": str(sheet_date),
                    "Employee ID": item["Employee ID"],
                    "Name": item["Name"],
                    "Company": item["Company"],
                    "Status": "Present",
                    "Remarks": item["Remarks"]
                })
            st.success(f"Successfully committed logs for {sheet_date}. Data flushed to database registries.")
            st.session_state['daily_active_roster'] = []  # Clear workspace for next data session
            st.rerun()

with tab2:
    st.subheader("Oman Operations Overview")
    
    # Filter today's entry out of database log for display metrics
    today_str = str(sheet_date)
    today_records = [r for r in st.session_state['attendance_database'] if r["Date"] == today_str]
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="metric-card"><h4 style="color:#8a99ad;margin:0;">Master Pool Size</h4><h2 style="color:#fff;margin:5px 0;">{len(st.session_state["master_labor_pool"])} Registered Workers</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card" style="border-left-color:#2ecc71;"><h4 style="color:#8a99ad;margin:0;">Workers Present on {today_str}</h4><h2 style="color:#2ecc71;margin:5px 0;">{len(today_records)} Active Personnel</h2></div>', unsafe_allow_html=True)
        
    st.markdown("<br>### 📅 Daily Historical Attendance Logs", unsafe_allow_html=True)
    if st.session_state['attendance_database']:
        df_logs = pd.DataFrame(st.session_state['attendance_database'])
        st.dataframe(df_logs, use_container_width=True)
    else:
        st.info("No saved data streams found in the historical system registries.")

with tab3:
    st.subheader("Monthly Attendance Aggregation Report")
    st.write("Aggregated calculation showing total shift metrics for individual employees inside the active operational period:")
    
    if st.session_state['attendance_database']:
        df_all = pd.DataFrame(st.session_state['attendance_database'])
        # Group data to count total work days for each person
        summary_df = df_all.groupby(["Employee ID", "Name", "Company"]).size().reset_index(name="Total Days Worked")
        st.dataframe(summary_df, use_container_width=True)
    else:
        st.info("System aggregation matrices are blank. Total day tallies will populate as soon as records are submitted.")