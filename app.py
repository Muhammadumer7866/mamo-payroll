import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Workforce & Payroll Portal", layout="wide")

# --- CUSTOM SECURITY & CORPORATE THEME (CSS) ---
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
            if username == "admin@construction.om" and password == "Oman#Secure2026":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Authentication Failed. Invalid credentials.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- MASTER DATABASE (Humesha Ka Previous Record) ---
if 'master_labor_pool' not in st.session_state:
    st.session_state['master_labor_pool'] = [
        {"Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Rubhan. T"},
        {"Employee ID": "109748895", "Name": "M.Usman", "Company": "Rubhan. T"},
        {"Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Rubhan. T"},
        {"Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL"},
    ]

# Aaj ki temporary active list (Roz subah/fresh khalne par empty hogi)
if 'daily_active_roster' not in st.session_state:
    st.session_state['daily_active_roster'] = []

if 'dashboard_presents' not in st.session_state:
    st.session_state['dashboard_presents'] = 0

# --- MAIN PREMIUM PORTAL CONTENT ---
st.markdown('<h1 class="main-title">💼 OVERSEAS WORKFORCE & LIVE PAYROLL SYSTEM</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📝 Daily Attendance Entry", "📊 Executive Analytics Dashboard", "💰 Month-End Payroll"])

with tab1:
    st.subheader("Daily Sheet Configuration")
    sheet_date = st.date_input("Select Sheet Date", datetime.now())
    
    if st.button("🔄 Start New Clean Sheet (Reset Today's List)"):
        st.session_state['daily_active_roster'] = []
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Do columns banaye hain: Ek purane worker ko dhoodhne ke liye, ek bilkul naye ke liye
    col_left, col_right = st.columns(2)
    
    # -------------------------------------------------------------
    # PANEL 1: 🔍 PURANI LABOR KO ADDD KARNE KE LIYE (SEARCH & ADD)
    # -------------------------------------------------------------
    with col_left:
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #00E5FF; margin-top:0;'>🔍 Add Existing Worker (Previous Record)</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #8a99ad; font-size:13px;'>Kal ya pichle dino aaye hue worker ko select karein:</p>", unsafe_allow_html=True)
        
        # Dropdown with all registered workers
        pool_df = pd.DataFrame(st.session_state['master_labor_pool'])
        options_list = [f"{row['Name']} (ID: {row['Employee ID']}) - {row['Company']}" for _, row in pool_df.iterrows()]
        
        selected_existing = st.selectbox("Search by Name or ID number:", options_list, key="search_exist")
        
        if st.button("✅ Add to Today's Sheet", use_container_width=True):
            # Extract ID from text string safely
            extracted_id = selected_existing.split("(ID: ")[1].split(")")[0]
            worker_details = next(w for w in st.session_state['master_labor_pool'] if w["Employee ID"] == extracted_id)
            
            # Check duplicate entry for today
            if any(w['Employee ID'] == extracted_id for w in st.session_state['daily_active_roster']):
                st.warning("⚠️ Yeh worker pehle se aaj ki sheet me add ho chuka hai!")
            else:
                st.session_state['daily_active_roster'].append({
                    "Employee ID": worker_details["Employee ID"],
                    "Name": worker_details["Name"],
                    "Company": worker_details["Company"],
                    "Remarks": ""
                })
                st.success(f"✔ {worker_details['Name']} aaj ki list me add ho gaye.")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------------------
    # PANEL 2: ➕ NAYI LABOR REGISTER KARNE KE LIYE (+ NEW LABOR)
    # -------------------------------------------------------------
    with col_right:
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #2ecc71; margin-top:0;'>➕ Register & Add Brand New Labor</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #8a99ad; font-size:13px;'>Agar koi naya banda pehli dafa site par aaya hai:</p>", unsafe_allow_html=True)
        
        new_id = st.text_input("Enter New Employee ID", placeholder="e.g. 123456")
        new_name = st.text_input("Enter Full Name", placeholder="e.g. Imran Khan")
        new_comp = st.text_input("Enter Company Name", placeholder="e.g. Rubhan. T")
        
        if st.button("➕ Register & Add to Today's Sheet", use_container_width=True):
            if new_id and new_name and new_comp:
                # Check duplicate in master pool
                id_exists = any(w['Employee ID'] == new_id for w in st.session_state['master_labor_pool'])
                if id_exists:
                    st.error("❌ Yeh ID pehle se registered hai! Left side wale box se search karein.")
                else:
                    # 1. Master database me hamesha ke liye save karo
                    st.session_state['master_labor_pool'].append({"Employee ID": new_id, "Name": new_name, "Company": new_comp})
                    # 2. Aaj ki active roster list me bhi dalo
                    st.session_state['daily_active_roster'].append({"Employee ID": new_id, "Name": new_name, "Company": new_comp, "Remarks": ""})
                    st.success(f"🚀 {new_name} register bhi ho gaye aur aaj ki list me bhi add ho gaye!")
                    st.rerun()
            else:
                st.warning("⚠️ Meharbani karke naye worker ki saari details fill karein!")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #2d3545;'>", unsafe_allow_html=True)
    
    # -------------------------------------------------------------
    # 📋 TODAY'S ACTIVE PRESENT SHEET (DISPLAY AREA)
    # -------------------------------------------------------------
    st.markdown('### 📋 Today\'s Active Attendance List')
    
    if not st.session_state['daily_active_roster']:
        st.info("ℹ Aaj ki sheet khali hai. Jo jo labor aaj kaam par aayi hai, unhe upar se add karein.")
    else:
        h_id, h_name, h_comp, h_status, h_rem = st.columns([1, 2, 1.5, 1, 2.5])
        h_id.markdown("**ID**")
        h_name.markdown("**Name**")
        h_comp.markdown("**Company**")
        h_status.markdown("**Status**")
        h_rem.markdown("**Remarks**")
        
        for idx, worker in enumerate(st.session_state['daily_active_roster']):
            col_id, col_name, col_comp, col_status, col_rem = st.columns([1, 2, 1.5, 1, 2.5])
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
                
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Lock & Save Today's Report", type="primary", use_container_width=True):
            st.session_state['dashboard_presents'] = len(st.session_state['daily_active_roster'])
            st.success(f"🎉 Live Database Updated! Total {st.session_state['dashboard_presents']} active workers saved for {sheet_date}.")

with tab2:
    st.subheader("Oman Operations Overview")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="metric-card"><h4 style="color:#8a99ad;margin:0;">Master Pool (Total Registered)</h4><h2 style="color:#fff;margin:5px 0;">{len(st.session_state["master_labor_pool"])} Workers</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card" style="border-left-color:#2ecc71;"><h4 style="color:#8a99ad;margin:0;">Present Today</h4><h2 style="color:#2ecc71;margin:5px 0;">{st.session_state["dashboard_presents"]} Active</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card" style="border-left-color:#e74c3c;"><h4 style="color:#8a99ad;margin:0;">Roster Status</h4><h2 style="color:#e74c3c;margin:5px 0;">Clean Slate Operational</h2></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Payroll Summary Generation")
    st.write("Automated Omani Rial (OMR) currency conversions and bank transfer sheets.")