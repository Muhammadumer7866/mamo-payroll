import streamlit as st
import pandas as pd
from datetime import datetime
import io

# Page Configuration for Premium Layout
st.set_page_config(page_title="Al Rabhan Trading - Enterprise Portal", layout="wide", initial_sidebar_state="expanded")

# --- ADVANCED PREMIUM CORPORATE THEME (CSS) ---
st.markdown("""
    <style>
    /* Full App Deep Dark Luxury Background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #141923 0%, #0b0d13 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #e2e8f0;
    }
    
    /* Executive Glassmorphism Containers */
    .premium-card {
        background: rgba(30, 41, 59, 0.45);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
    }
    
    /* Login Box Cinematic Design */
    .login-container {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(0, 229, 255, 0.2);
        box-shadow: 0px 0px 40px rgba(0, 229, 255, 0.15);
        padding: 45px;
        border-radius: 24px;
        margin-top: 10%;
    }
    
    /* Glowing Neon Sub-headers */
    .gold-glow {
        color: #FFD700;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
        font-weight: 600;
    }
    .cyan-glow {
        color: #00E5FF;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.3);
        font-weight: 600;
    }
    
    /* Elegant Clean Metrics */
    .metric-val {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SECURE SESSION MANAGERS ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'master_labor_pool' not in st.session_state:
    st.session_state['master_labor_pool'] = []
if 'attendance_database' not in st.session_state:
    st.session_state['attendance_database'] = []
if 'daily_active_roster' not in st.session_state:
    st.session_state['daily_active_roster'] = []
if 'invoice_database' not in st.session_state:
    st.session_state['invoice_database'] = []

# --- CINEMATIC LOGIN GATEWAY ---
if not st.session_state['logged_in']:
    _, central_col, _ = st.columns([1, 1.8, 1])
    with central_col:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<h1 style="text-align: center; color: #ffffff; font-size: 28px; margin-bottom: 5px; letter-spacing:1px;">AL RABHAN TRADING</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #00E5FF; font-size: 12px; letter-spacing: 3px; margin-bottom: 35px;">SULTANATE OF OMAN • ENTERPRISE ERP</p>', unsafe_allow_html=True)
        
        user_id = st.text_input("Corporate ID / Email Address")
        user_key = st.text_input("Security Access Key", type="password")
        
        st.markdown('<br>', unsafe_allow_html=True)
        if st.button("Authenticate Session", use_container_width=True):
            if user_id == "admin@construction.om" and user_key == "Oman#Secure2026":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Access Denied. Cryptographic keys or ID verified as mismatch.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- HELPER DOWNLOAD FUNCTION ---
def convert_df_to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Report')
    return output.getvalue()

# --- PREMIUM HEADER & NAVIGATION ---
st.markdown('<div style="text-align:center; padding: 20px 0;"><h1 style="color:#ffffff; margin-bottom:0; font-weight:800; font-size:36px; letter-spacing: 1.5px;">🏢 AL RABHAN TRADING OPERATIONS SYSTEM</h1><p style="color:#8a99ad; font-size:14px; letter-spacing:2px; margin-top:5px;">MANAGEMENT, WORKFORCE & INVOICE CONTROL HUB — OMAN</p></div>', unsafe_allow_html=True)

tab_home, tab_attendance, tab_invoices, tab_analytics = st.tabs([
    "🏠 Corporate Home", 
    "📝 Daily Attendance Entry", 
    "🧾 Tax Invoices Registry", 
    "📊 Executive Reports & Analytics"
])

# --- TAB 1: CORPORATE HOME PAGE ---
with tab_home:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown("### <span class='cyan-glow'>Welcome back, Administrator</span>", unsafe_allow_html=True)
    st.write("Al Rabhan Trading centralized ecosystem tracks cross-border operations, active industrial field workforce metrics, and procurement financial logs seamlessly.")
    
    col_h1, col_h2, col_h3 = st.columns(3)
    with col_h1:
        st.markdown(f'<div style="background:rgba(0,229,255,0.05); padding:20px; border-radius:12px; border-left:4px solid #00E5FF;"><h4>Total Field Workforce</h4><div class="metric-val">{len(st.session_state["master_labor_pool"])} Registered</div></div>', unsafe_allow_html=True)
    with col_h2:
        st.markdown(f'<div style="background:rgba(255,215,0,0.05); padding:20px; border-radius:12px; border-left:4px solid #FFD700;"><h4>Invoices Logged</h4><div class="metric-val">{len(st.session_state["invoice_database"])} Records</div></div>', unsafe_allow_html=True)
    with col_h3:
        total_omr = sum(float(inv['Total Amount']) for inv in st.session_state['invoice_database']) if st.session_state['invoice_database'] else 0.0
        st.markdown(f'<div style="background:rgba(46,204,113,0.05); padding:20px; border-radius:12px; border-left:4px solid #2ecc71;"><h4>Total Gross Volume</h4><div class="metric-val">{total_omr:.3f} OMR</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: ATTENDANCE ENTRY ---
with tab_attendance:
    st.subheader("Daily Roster Control")
    sheet_date = st.date_input("Select Active Sheet Date", datetime.now(), key="att_date")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("<h4>🔍 Add Worker from Master Registry</h4>", unsafe_allow_html=True)
        search_query = st.text_input("Query by Full Name or Unique ID", placeholder="Search fields...")
        
        if search_query:
            if not st.session_state['master_labor_pool']:
                st.warning("The primary infrastructure database contains no personnel records.")
            else:
                matches = [w for w in st.session_state['master_labor_pool'] if search_query.lower() in w['Name'].lower() or search_query in w['Employee ID']]
                if matches:
                    for matched_worker in matches:
                        if st.button(f"Deploy {matched_worker['Name']} ({matched_worker['Employee ID']})", key=f"match_{matched_worker['Employee ID']}"):
                            if any(w['Employee ID'] == matched_worker['Employee ID'] for w in st.session_state['daily_active_roster']):
                                st.warning("Target worker record is already active inside today's roster frame.")
                            else:
                                st.session_state['daily_active_roster'].append({
                                    "Employee ID": matched_worker["Employee ID"], "Name": matched_worker["Name"],
                                    "Company": matched_worker["Company"], "Remarks": ""
                                })
                                st.success(f"Successfully staged {matched_worker['Name']}.")
                                st.rerun()
                else:
                    st.error("No record matches found.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("<h4>➕ First-Time Personnel Registration</h4>", unsafe_allow_html=True)
        new_id = st.text_input("New Employee ID Number")
        new_name = st.text_input("Worker Legal Full Name")
        new_comp = st.text_input("Subcontractor/Company Affiliation")
        
        if st.button("Execute Registration Flow", use_container_width=True):
            if new_id and new_name and new_comp:
                if any(w['Employee ID'] == new_id for w in st.session_state['master_labor_pool']):
                    st.error("System violation. Unique Employee ID already claims ownership inside records.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": new_id, "Name": new_name, "Company": new_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": new_id, "Name": new_name, "Company": new_comp, "Remarks": ""})
                    st.success("New personnel successfully provisioned.")
                    st.rerun()
            else:
                st.warning("All input blocks are non-optional.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📋 Staged Field Deployments")
    if not st.session_state['daily_active_roster']:
        st.info("No active personnel staged for deployment today.")
    else:
        to_remove = None
        for idx, worker in enumerate(st.session_state['daily_active_roster']):
            c_id, c_name, c_comp, c_rem, c_act = st.columns([1, 2, 1.5, 3, 1])
            c_id.write(worker["Employee ID"])
            c_name.write(worker["Name"])
            c_comp.write(worker["Company"])
            st.session_state['daily_active_roster'][idx]["Remarks"] = c_rem.text_input("Remarks Log", key=f"rem_{idx}", value=worker["Remarks"], label_visibility="collapsed")
            if c_act.button("❌ Remove", key=f"del_{idx}"):
                to_remove = idx
                
        if to_remove is not None:
            st.session_state['daily_active_roster'].pop(to_remove)
            st.rerun()
            
        if st.button("💾 Finalize & Commit Daily Attendance Logs", type="primary", use_container_width=True):
            for item in st.session_state['daily_active_roster']:
                st.session_state['attendance_database'].append({
                    "Date": str(sheet_date), "Employee ID": item["Employee ID"],
                    "Name": item["Name"], "Company": item["Company"],
                    "Status": "Present", "Remarks": item["Remarks"]
                })
            st.success("Session closed. Daily data committed to corporate logs.")
            st.session_state['daily_active_roster'] = []
            st.rerun()

# --- TAB 3: TAX INVOICES REGISTRY ---
with tab_invoices:
    st.subheader("Procurement & Sales Invoices Control")
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown("<h4>📥 Add New Tax Invoice Entry</h4>", unsafe_allow_html=True)
    inv_col1, inv_col2 = st.columns(2)
    with inv_col1:
        inv_date = st.date_input("Invoice Issue Date", datetime.now())
        inv_num = st.text_input("Invoice Number (e.g. A204306)")
    with inv_col2:
        inv_total = st.number_input("Total Invoice Amount (Gross OMR)", min_value=0.000, format="%.3f")
        inv_vat = st.number_input("VAT Component Amount (5% OMR)", min_value=0.000, format="%.3f")
        
    if st.button("🔒 Securely Log Invoice Record", type="primary"):
        if inv_num and inv_total > 0:
            st.session_state['invoice_database'].append({
                "Date": str(inv_date),
                "Invoice Number": inv_num,
                "Total Amount": f"{inv_total:.3f}",
                "VAT Amount": f"{inv_vat:.3f}",
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"Invoice {inv_num} registered successfully under Al Rabhan Trading registries.")
            st.rerun()
        else:
            st.error("Validation error. Provide valid non-zero values.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Logged Commercial Invoices")
    if st.session_state['invoice_database']:
        df_inv = pd.DataFrame(st.session_state['invoice_database'])
        st.dataframe(df_inv, use_container_width=True)
    else:
        st.info("No invoice metrics have been archived inside system nodes yet.")

# --- TAB 4: EXECUTIVE REPORTS & ANALYTICS ---
with tab_analytics:
    st.subheader("Global Filter, Metrics Consolidation & Export Panels")
    
    # Global Search / Filter Block
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    filter_type = st.radio("Choose Reporting Timeline View Filter:", ["All Records", "Monthly Aggregation View", "Yearly Aggregation View"], horizontal=True)
    
    target_month = datetime.now().strftime("%m")
    target_year = datetime.now().strftime("%Y")
    
    if filter_type == "Monthly Aggregation View":
        c_m, c_y = st.columns(2)
        target_month = c_m.selectbox("Select Target Month", [f"{i:02d}" for i in range(1, 13)], index=int(datetime.now().month)-1)
        target_year = c_y.selectbox("Select Target Year", [str(y) for y in range(2025, 2030)], key="m_year")
    elif filter_type == "Yearly Aggregation View":
        target_year = st.selectbox("Select Target Year", [str(y) for y in range(2025, 2030)], key="y_year")
    st.markdown('</div>', unsafe_allow_html=True)

    # PROCESS & DISPLAY FILTERS
    col_rep1, col_rep2 = st.columns(2)
    
    with col_rep1:
        st.markdown("### 📊 Filtered Attendance Metrics")
        if st.session_state['attendance_database']:
            df_att_master = pd.DataFrame(st.session_state['attendance_database'])
            df_att_master['ParsedDate'] = pd.to_datetime(df_att_master['Date'])
            
            # Apply Filter Logic
            if filter_type == "Monthly Aggregation View":
                filtered_att = df_att_master[(df_att_master['ParsedDate'].dt.strftime('%m') == target_month) & (df_att_master['ParsedDate'].dt.strftime('%Y') == target_year)]
            elif filter_type == "Yearly Aggregation View":
                filtered_att = df_att_master[df_att_master['ParsedDate'].dt.strftime('%Y') == target_year]
            else:
                filtered_att = df_att_master
                
            if not filtered_att.empty:
                summary_att = filtered_att.groupby(["Employee ID", "Name", "Company"]).size().reset_index(name="Total Shifts Worked")
                st.dataframe(summary_att, use_container_width=True)
                
                # Excel Download Logic
                xlsx_data = convert_df_to_excel(summary_att)
                st.download_button(label="📥 Download Attendance Report (Excel)", data=xlsx_data, file_name=f"Attendance_Report_{target_year}_{filter_type.replace(' ', '')}.xlsx", mime="application/vnd.ms-excel")
            else:
                st.info("No matching records found inside the specified timeline criteria.")
        else:
            st.info("Attendance databases are blank.")

    with col_rep2:
        st.markdown("### 💰 Filtered Invoice Balance Ledger")
        if st.session_state['invoice_database']:
            df_inv_master = pd.DataFrame(st.session_state['invoice_database'])
            df_inv_master['ParsedDate'] = pd.to_datetime(df_inv_master['Date'])
            
            if filter_type == "Monthly Aggregation View":
                filtered_inv = df_inv_master[(df_inv_master['ParsedDate'].dt.strftime('%m') == target_month) & (df_inv_master['ParsedDate'].dt.strftime('%Y') == target_year)]
            elif filter_type == "Yearly Aggregation View":
                filtered_inv = df_inv_master[df_inv_master['ParsedDate'].dt.strftime('%Y') == target_year]
            else:
                filtered_inv = df_inv_master
                
            if not filtered_inv.empty:
                display_inv = filtered_inv[["Date", "Invoice Number", "Total Amount", "VAT Amount"]]
                st.dataframe(display_inv, use_container_width=True)
                
                # Excel Download Logic
                xlsx_inv_data = convert_df_to_excel(display_inv)
                st.download_button(label="📥 Download Invoice Ledger (Excel)", data=xlsx_inv_data, file_name=f"Invoice_Ledger_{target_year}_{filter_type.replace(' ', '')}.xlsx", mime="application/vnd.ms-excel")
            else:
                st.info("No invoice transactions verified for this matching timeline context.")
        else:
            st.info("No financial invoice streams available.")