import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- ENHANCED EXECUTIVE THEME CONFIGURATION ---
st.set_page_config(page_title="Al Rabhan Trading - Portal", layout="wide", initial_sidebar_state="collapsed")

# --- PREMIUM MODERN CSS INJECTION ---
st.markdown("""
    <style>
    /* Global Background Styling */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* Subtle Watermark Background for Logged-In Pages */
    .watermark-bg {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 9vw;
        font-weight: 900;
        color: rgba(15, 23, 42, 0.02);
        z-index: 0;
        pointer-events: none;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 10px;
        white-space: nowrap;
    }

    /* --- SPLIT LOGIN CONTAINER (Matches image_af17ca.jpg Layout) --- */
    .login-wrapper {
        display: flex;
        min-height: 85vh;
        background: #ffffff;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.06);
        overflow: hidden;
        margin-top: 20px;
    }
    .login-left {
        flex: 1;
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .login-right {
        flex: 1.1;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        color: #ffffff;
        position: relative;
    }
    .login-right::before {
        content: "";
        position: absolute;
        width: 150%;
        height: 150%;
        top: -25%;
        left: -25%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
        pointer-events: none;
    }
    
    /* Dashboard Modern Interface Cards */
    .dashboard-card {
        background: #ffffff;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        z-index: 1;
        position: relative;
    }
    .stat-val {
        font-size: 2.25rem;
        font-weight: 700;
        color: #1e3a8a;
    }
    
    /* Clean Tab Headers */
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #64748b;
        padding: 12px 24px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #2563eb;
        border-bottom-color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# --- SYSTEM STATE INITIALIZATION ---
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

# --- EXTENDED MODERN SPLIT LOGIN GATEWAY ---
if not st.session_state['logged_in']:
    # Main split container markup structure
    st.markdown("""
        <div class="login-wrapper">
            <div class="login-left">
                <div style="display: flex; align-items: center; margin-bottom: 40px;">
                    <div style="background: #2563eb; width: 12px; height: 24px; border-radius: 4px; margin-right: 10px;"></div>
                    <span style="font-weight: 700; font-size: 20px; color: #0f172a; letter-spacing: 0.5px;">Al Rabhan Trading</span>
                </div>
                <h2 style="color: #0f172a; font-weight: 700; margin-bottom: 5px; font-size: 32px;">Welcome Back</h2>
                <p style="color: #64748b; font-size: 14px; margin-bottom: 35px;">Enter your administrative security credentials to access the ERP cloud platform.</p>
            </div>
            <div class="login-right">
                <h2 style="font-weight: 700; font-size: 36px; margin-bottom: 15px; line-height: 1.2;">Effortlessly manage your workforce and corporate financials.</h2>
                <p style="color: rgba(255,255,255,0.85); font-size: 15px; margin-bottom: 40px; line-height: 1.6;">
                    Consolidated operational tracking window engineered specifically for field roster logging and secure Omani Tax Invoice registry management.
                </p>
                <div style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.15); padding: 20px; border-radius: 12px; backdrop-filter: blur(10px);">
                    <span style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: #93c5fd;">System Integrity Node</span>
                    <p style="margin: 5px 0 0 0; font-size: 13px; color: rgba(255,255,255,0.9);">Secure multi-tenant data structures with automated Excel and CSV ledger extraction rules compilation enabled.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render interactive input boxes over the left panel layout area
    with st.container():
        # Fine positioning adjustments using column anchors 
        col_space, col_form = st.columns([1, 1])
        with col_space:
            # Overlays precisely onto the HTML login-left structure 
            st.markdown('<div style="position: relative; margin-top: -380px; padding-left: 45px; max-width: 440px;">', unsafe_allow_html=True)
            input_user = st.text_input("Corporate ID / Email Address", placeholder="e.g. admin@construction.om")
            input_key = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
            
            st.markdown('<div style="margin-top: 25px;">', unsafe_allow_html=True)
            if st.button("Log In to System", type="primary", use_container_width=True):
                if input_user == "admin@construction.om" and input_key == "Oman#Secure2026":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Authentication check failed. Invalid ID or Access Key match parameters.")
            st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

# --- BACKGROUND WATERMARK PRINT ---
st.markdown('<div class="watermark-bg">AL RABHAN TRADING</div>', unsafe_allow_html=True)

# --- APPLICATION HEADER FRAME ---
st.markdown("""
    <div style="background: #ffffff; padding: 20px 30px; border-bottom: 1px solid #e2e8f0; margin: -50px -50px 30px -50px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="font-size: 24px; font-weight: 700; color: #0f172a; margin: 0;">AL RABHAN TRADING HUB</h1>
            <p style="font-size: 12px; color: #64748b; margin: 2px 0 0 0; font-weight: 500; text-transform: uppercase; letter-spacing: 1px;">Sultanate of Oman • Management Console</p>
        </div>
        <div style="background: #f1f5f9; padding: 8px 16px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <span style="font-size: 13px; font-weight: 600; color: #334155;">🔒 Active Session Secured</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- DATA EXPORT COMPILER UTILITY ---
def convert_to_excel_buffer(df):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Data_Export_Sheet')
    return buffer.getvalue()

# --- MAIN WORKSPACE MULTI-TAB ARCHITECTURE ---
tab_portal_home, tab_field_entry, tab_tax_invoice, tab_reporting = st.tabs([
    "🏠 Corporate Overview", 
    "📝 Daily Attendance Matrix", 
    "🧾 Tax Invoices Registry", 
    "📊 Granular Ledger Exports"
])

# 1. CORPORATE HOME PAGE PANEL
with tab_portal_home:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #0f172a; font-weight: 700; margin-top:0;'>Operational Command Console</h3>", unsafe_allow_html=True)
    st.write("Integrated data management array executing personnel attendance monitoring alongside commercial ledger audits.")
    
    col_st1, col_st2, col_st3 = st.columns(3)
    with col_st1:
        st.markdown(f'<div style="background:#eff6ff; padding:20px; border-radius:12px; border:1px solid #bfdbfe;"><h4>Total Registered Workforce</h4><div class="stat-val">{len(st.session_state["master_labor_pool"])} Personnel</div></div>', unsafe_allow_html=True)
    with col_st2:
        st.markdown(f'<div style="background:#fef3c7; padding:20px; border-radius:12px; border:1px solid #fde68a;"><h4>Archived Invoice Trackers</h4><div class="stat-val">{len(st.session_state["invoice_database"])} Transactions</div></div>', unsafe_allow_html=True)
    with col_st3:
        gross_omr_sum = sum(float(x['Total Amount']) for x in st.session_state['invoice_database']) if st.session_state['invoice_database'] else 0.0
        st.markdown(f'<div style="background:#f0fdf4; padding:20px; border-radius:12px; border:1px solid #bbf7d0;"><h4>Gross Volume Logged</h4><div class="stat-val">{gross_omr_sum:.3f} OMR</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. DAILY ATTENDANCE ENTRY PANEL
with tab_field_entry:
    st.subheader("Field Deployment Roster Logs")
    active_calendar_date = st.date_input("Target Calendar Date Focus", datetime.now(), key="main_cal")
    
    col_m_left, col_m_right = st.columns(2)
    with col_m_left:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4>🔍 Quick Search Registered Pool</h4>", unsafe_allow_html=True)
        query_str = st.text_input("Filter via Name or Employee ID Sequence", placeholder="Type parameters here...")
        
        if query_str:
            if not st.session_state['master_labor_pool']:
                st.warning("Master operational registries contain zero records currently.")
            else:
                matches_found = [m for m in st.session_state['master_labor_pool'] if query_str.lower() in m['Name'].lower() or query_str in m['Employee ID']]
                if matches_found:
                    for wrk in matches_found:
                        if st.button(f"Stage Deployment: {wrk['Name']} ({wrk['Employee ID']})", key=f"stg_{wrk['Employee ID']}"):
                            if any(z['Employee ID'] == wrk['Employee ID'] for z in st.session_state['daily_active_roster']):
                                st.error("Personnel record already verified inside current active staging queue.")
                            else:
                                st.session_state['daily_active_roster'].append({
                                    "Employee ID": wrk["Employee ID"], "Name": wrk["Name"],
                                    "Company": wrk["Company"], "Remarks": ""
                                })
                                st.success(f"Staged {wrk['Name']}.")
                                st.rerun()
                else:
                    st.info("No master record indicators match specified metrics query.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_m_right:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4>➕ First-Time Workforce Provisioning</h4>", unsafe_allow_html=True)
        reg_id = st.text_input("Assign Unique Employee ID")
        reg_name = st.text_input("Legal Individual Full Name")
        reg_comp = st.text_input("Corporate Vendor Entity (e.g. Al Rabhan Trading)")
        
        if st.button("Commit Registration Record", use_container_width=True):
            if reg_id and reg_name and reg_comp:
                if any(k['Employee ID'] == reg_id for k in st.session_state['master_labor_pool']):
                    st.error("Data conflict exception. Input Employee ID code already occupies allocation slots.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": reg_id, "Name": reg_name, "Company": reg_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": reg_id, "Name": reg_name, "Company": reg_comp, "Remarks": ""})
                    st.success("New structural personnel matrix built.")
                    st.rerun()
            else:
                st.warning("Execution halted. All structural text inputs remain mandatory.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📋 Staged Attendance Matrix Deployment Queue")
    if not st.session_state['daily_active_roster']:
        st.info("Staging workspace contains zero active worker units presently.")
    else:
        pop_target = None
        for r_idx, r_item in enumerate(st.session_state['daily_active_roster']):
            gx1, gx2, gx3, gx4, gx5 = st.columns([1.5, 2, 2, 3, 1])
            gx1.write(f"**ID:** {r_item['Employee ID']}")
            gx2.write(f"**Name:** {r_item['Name']}")
            gx3.write(f"**Company:** {r_item['Company']}")
            st.session_state['daily_active_roster'][r_idx]["Remarks"] = gx4.text_input("Remarks", key=f"tbl_rem_{r_idx}", value=r_item["Remarks"], label_visibility="collapsed")
            if gx5.button("❌ Drop", key=f"drop_{r_idx}"):
                pop_target = r_idx
                
        if pop_target != None:
            st.session_state['daily_active_roster'].pop(pop_target)
            st.rerun()
            
        if st.button("🔒 Finalize Daily Report Tally Sheets", type="primary", use_container_width=True):
            for entry in st.session_state['daily_active_roster']:
                st.session_state['attendance_database'].append({
                    "Date": str(active_calendar_date), "Employee ID": entry["Employee ID"],
                    "Name": entry["Name"], "Company": entry["Company"],
                    "Status": "Present", "Remarks": entry["Remarks"]
                })
            st.success("Tally sheets archived securely.")
            st.session_state['daily_active_roster'] = []
            st.rerun()

# 3. TAX INVOICE TRACKING REGISTRY PANEL
with tab_tax_invoice:
    st.subheader("Commercial Transaction & Invoice Audit Controls")
    
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("<h4>📥 Archive Tax Invoice Metrics</h4>", unsafe_allow_html=True)
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        in_date = st.date_input("Tax Invoice Document Date", datetime.now(), key="inv_entry_date")
        in_num = st.text_input("Tax Invoice Number (Serial)", placeholder="e.g. A204306")
    with f_col2:
        in_amt = st.number_input("Invoice Total Gross Sum (OMR)", min_value=0.000, step=0.001, format="%.3f")
        in_vat = st.number_input("Calculated Tax Deductible Component Value (5% VAT OMR)", min_value=0.000, step=0.001, format="%.3f")
        
    if st.button("🔒 Commit Financial Record Entry", type="primary"):
        if in_num and in_amt > 0:
            st.session_state['invoice_database'].append({
                "Date": str(in_date),
                "Invoice Number": in_num,
                "Total Amount": f"{in_amt:.3f}",
                "VAT Amount": f"{in_vat:.3f}",
                "System Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"Commercial transaction invoice line item [{in_num}] logged safely.")
            st.rerun()
        else:
            st.error("Data verification criteria mismatch. Enter accurate transaction figures.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Logged Commercial Invoices")
    if st.session_state['invoice_database']:
        st.dataframe(pd.DataFrame(st.session_state['invoice_database']), use_container_width=True)
    else:
        st.info("System ledger arrays hold zero commercial transaction files currently.")

# 4. EXPORT AND REPORT GENERATION PANEL
with tab_reporting:
    st.subheader("Timeline Report Compilers & Binary Downloads")
    
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    time_scope = st.radio("Specify Analytical Report Target Chronology Scope:", ["View All Records", "Filter Specific Month Window", "Filter Specific Year Window"], horizontal=True)
    
    cur_m = datetime.now().strftime("%m")
    cur_y = datetime.now().strftime("%Y")
    
    if time_scope == "Filter Specific Month Window":
        mx1, mx2 = st.columns(2)
        cur_m = mx1.selectbox("Month Frame Anchor", [f"{s:02d}" for s in range(1, 13)], index=int(datetime.now().month)-1)
        cur_y = mx2.selectbox("Year Frame Anchor", [str(y) for y in range(2025, 2031)], key="month_anchor_yr")
    elif time_scope == "Filter Specific Year Window":
        cur_y = st.selectbox("Year Frame Anchor", [str(y) for y in range(2025, 2031)], key="year_anchor_yr")
    st.markdown('</div>', unsafe_allow_html=True)

    rep_col_left, rep_col_right = st.columns(2)
    
    with rep_col_left:
        st.markdown("#### 📊 Filtered Workforce Attendance Ledgers")
        if st.session_state['attendance_database']:
            df_att_run = pd.DataFrame(st.session_state['attendance_database'])
            df_att_run['D_Obj'] = pd.to_datetime(df_att_run['Date'])
            
            if time_scope == "Filter Specific Month Window":
                df_filtered_att = df_att_run[(df_att_run['D_Obj'].dt.strftime('%m') == cur_m) & (df_att_run['D_Obj'].dt.strftime('%Y') == cur_y)]
            elif time_scope == "Filter Specific Year Window":
                df_filtered_att = df_att_run[df_att_run['D_Obj'].dt.strftime('%Y') == cur_y]
            else:
                df_filtered_att = df_att_run
                
            if not df_filtered_att.empty:
                compiled_sheet_att = df_filtered_att.groupby(["Employee ID", "Name", "Company"]).size().reset_index(name="Aggregated Total Shifts Claimed")
                st.dataframe(compiled_sheet_att, use_container_width=True)
                
                bin_excel_att = convert_to_excel_buffer(compiled_sheet_att)
                st.download_button(label="📥 Download Aggregated Attendance Ledger (.xlsx)", data=bin_excel_att, file_name=f"Workforce_Report_{cur_y}_{cur_m}.xlsx", mime="application/vnd.ms-excel", key="dl_att")
            else:
                st.info("No workforce operational data logs match targeted sorting frames.")
        else:
            st.info("Workforce attendance tracking records remain blank.")

    with rep_col_right:
        st.markdown("#### 🧾 Filtered Commercial Revenue Ledgers")
        if st.session_state['invoice_database']:
            df_inv_run = pd.DataFrame(st.session_state['invoice_database'])
            df_inv_run['D_Obj'] = pd.to_datetime(df_inv_run['Date'])
            
            if time_scope == "Filter Specific Month Window":
                df_filtered_inv = df_inv_run[(df_inv_run['D_Obj'].dt.strftime('%m') == cur_m) & (df_inv_run['D_Obj'].dt.strftime('%Y') == cur_y)]
            elif time_scope == "Filter Specific Year Window":
                df_filtered_inv = df_inv_run[df_inv_run['D_Obj'].dt.strftime('%Y') == cur_y]
            else:
                df_filtered_inv = df_inv_run
                
            if not df_filtered_inv.empty:
                compiled_sheet_inv = df_filtered_inv[["Date", "Invoice Number", "Total Amount", "VAT Amount"]]
                st.dataframe(compiled_sheet_inv, use_container_width=True)
                
                bin_excel_inv = convert_to_excel_buffer(compiled_sheet_inv)
                st.download_button(label="📥 Download Transaction Invoice Ledger (.xlsx)", data=bin_excel_inv, file_name=f"Financial_Ledger_Report_{cur_y}_{cur_m}.xlsx", mime="application/vnd.ms-excel", key="dl_inv")
            else:
                st.info("No transaction matching markers identified inside targeted query scope.")
        else:
            st.info("Financial transaction matrices contain zero archived records.")