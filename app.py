import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- ULTRA-PREMIUM ULTIMATE CORE CONFIGURATION ---
st.set_page_config(page_title="Al Rabhan Trading - Corporate Portal", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM ADVANCED EXECUTIVE STYLING ENGINE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Application Canvas */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #0f172a;
    }
    
    /* --- SYSTEM WIDE KEYFRAME ANIMATIONS (DYNAMIC MOVEMENT) --- */
    @keyframes entranceSlideUp {
        0% { opacity: 0; transform: translateY(50px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes persistentPulseLogo {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 0.02; }
        50% { transform: translate(-50%, -50%) scale(1.03); opacity: 0.05; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 0.02; }
    }

    /* Giant Background Brand Watermark Overlay */
    .premium-watermark-bg {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 10vw;
        font-weight: 800;
        color: #ca8a04;
        opacity: 0.03;
        z-index: 0;
        pointer-events: none;
        text-align: center;
        letter-spacing: 12px;
        white-space: nowrap;
        user-select: none;
        animation: persistentPulseLogo 10s ease-in-out infinite;
    }

    /* --- PREMIUM SPLIT INTERFACE FRAMEWORK --- */
    .ultimate-split-wrapper {
        display: flex;
        min-height: 85vh;
        background: #ffffff;
        border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.08);
        border: 1px solid #e2e8f0;
        overflow: hidden;
        margin-top: 30px;
        animation: entranceSlideUp 1s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    /* Left Corporate Interaction Form Panel */
    .split-panel-left {
        flex: 1;
        padding: 60px 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: #ffffff;
    }

    /* Right Abstract Construction Branding Panel */
    .split-panel-right {
        flex: 1.1;
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        padding: 80px 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        color: #ffffff;
        position: relative;
        border-left: 1px solid #e2e8f0;
    }
    
    /* --- REALISTIC BRAND LOGO SHAPES (Inspired by ChatGPT Image Jun 20, 2026, 02_56_40 PM.png) --- */
    .logo-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 25px;
    }
    
    /* Dynamic Vector Towers Construction */
    .logo-graphic-box {
        display: flex;
        align-items: flex-end;
        gap: 4px;
        height: 65px;
        margin-bottom: 12px;
        padding-left: 10px;
    }
    
    .tower-gold-left {
        width: 14px;
        height: 35px;
        background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%);
        clip-path: polygon(100% 0, 0 40%, 0 100%, 100% 100%);
        border-radius: 1px;
    }
    
    .tower-dark-center {
        width: 16px;
        height: 60px;
        background: linear-gradient(135deg, #334155 0%, #0f172a 100%);
        clip-path: polygon(50% 0, 0 15%, 0 100%, 100% 100%, 100% 15%);
        border-radius: 1px;
    }
    
    .tower-gold-right {
        width: 12px;
        height: 45px;
        background: linear-gradient(135deg, #fef08a 0%, #eab308 100%);
        clip-path: polygon(0 0, 100% 30%, 100% 100%, 0 100%);
        border-radius: 1px;
    }

    .logo-text-title {
        font-size: 24px;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: 2px;
        margin: 0;
        text-transform: uppercase;
    }
    
    .logo-text-subtitle {
        font-size: 13px;
        font-weight: 600;
        color: #ca8a04;
        letter-spacing: 6px;
        margin: 2px 0 0 0;
        text-transform: uppercase;
    }
    
    .logo-tagline {
        font-size: 7px;
        font-weight: 500;
        color: #64748b;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 5px;
        border-top: 1px solid #e2e8f0;
        padding-top: 4px;
        width: 100%;
        max-width: 220px;
    }
    
    /* Branding Gold Accent Elements */
    .gold-brand-line {
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #eab308 0%, #ca8a04 100%);
        border-radius: 2px;
        margin-bottom: 25px;
    }
    
    .gold-pill-accent {
        background: rgba(234, 179, 8, 0.1);
        border: 1px solid rgba(234, 179, 8, 0.2);
        color: #fef08a;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        display: inline-block;
        margin-bottom: 20px;
    }

    /* Modern Post-Login Dashboard Component Architecture */
    .executive-card-node {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        z-index: 1;
    }
    .executive-card-node:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05);
        border-color: #eab308;
    }
    
    .giant-stat-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -1px;
    }
    
    div[data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- APPLICATION STATE MANAGEMENT ---
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

# --- MULTI-TENANT SPLIT SECURE GATEWAY ---
if not st.session_state['logged_in']:
    st.markdown("""
        <div class="ultimate-split-wrapper">
            <!-- Left Wing (Now features the corporate logo matching the image blueprint) -->
            <div class="split-panel-left">
                <div class="logo-container">
                    <div class="logo-graphic-box">
                        <div class="tower-gold-left"></div>
                        <div class="tower-dark-center"></div>
                        <div class="tower-gold-right"></div>
                    </div>
                    <div class="logo-text-title">Al Rabhan</div>
                    <div class="logo-text-subtitle">Trading</div>
                    <div class="logo-tagline">Construction | Quality | Trust</div>
                </div>
                <h2 style="color: #0f172a; font-weight: 800; font-size: 28px; margin-bottom: 6px; letter-spacing: -0.5px;">Welcome Back</h2>
                <p style="color: #64748b; font-size: 13px; margin-bottom: 35px;">Please authenticate administrative level keys to open the operations panel.</p>
            </div>
            <!-- Right Wing -->
            <div class="split-panel-right">
                <div>
                    <span class="gold-pill-accent">Oman Enterprise Infrastructure</span>
                    <h1 style="color: #ffffff; font-size: 40px; font-weight: 800; line-height: 1.2; margin-bottom: 20px; letter-spacing: -0.5px;">
                        Effortlessly manage your workforce and corporate financials.
                    </h1>
                    <div class="gold-brand-line"></div>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6; margin-bottom: 35px; max-width: 480px;">
                        Consolidated cloud tracking console custom engineered for real-time field operations, active shift logs control, and Omani Tax Invoice registry archiving.
                    </p>
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 20px; border-radius: 14px; max-width: 480px;">
                        <span style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: #eab308; letter-spacing: 1px;">CONSTRUCTION | QUALITY | TRUST</span>
                        <p style="margin: 6px 0 0 0; font-size: 13px; color: #cbd5e1; line-height: 1.5;">Automated analytical report structuring engine compiles binary Excel ledgers instantaneously for internal validation.</p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Inputs Overlay perfectly positioned under the graphic logo block
    with st.container():
        col_form_landing, col_void_space = st.columns([1, 1.1])
        with col_form_landing:
            st.markdown('<div style="position: relative; margin-top: -460px; padding: 0 60px; max-width: 500px;">', unsafe_allow_html=True)
            gate_id = st.text_input("Corporate ID / Email Address", placeholder="e.g. admin@construction.om")
            gate_key = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
            st.markdown('<div style="margin-top: 25px;">', unsafe_allow_html=True)
            if st.button("Log In to System", type="primary", use_container_width=True):
                if gate_id == "admin@construction.om" and gate_key == "Oman#Secure2026":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Access Refused. Security parameters failed evaluation.")
            st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

# --- ACTIVE PERSISTENT BACKGROUND WATERMARK ---
st.markdown('<div class="premium-watermark-bg">AL RABHAN TRADING</div>', unsafe_allow_html=True)

# --- MAIN POST-LOGIN INTERSIDEBAR NAVIGATION HEADER ---
st.markdown("""
    <div style="background: #ffffff; padding: 20px 40px; border-bottom: 1px solid #e2e8f0; margin: -50px -50px 35px -50px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
        <div style="display:flex; align-items:center; gap:12px;">
            <div style="width: 4px; height: 28px; background: #ca8a04; border-radius: 2px;"></div>
            <div>
                <h1 style="font-size: 20px; font-weight: 800; color: #0f172a; margin: 0; letter-spacing:-0.5px;">AL RABHAN TRADING OPERATIONS SYSTEM</h1>
                <p style="font-size: 11px; color: #64748b; margin: 0; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Sultanate of Oman • Enterprise Control Node</p>
            </div>
        </div>
        <div style="background: #f1f5f9; padding: 6px 14px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <span style="font-size: 12px; font-weight: 600; color: #334155;">🔒 Security Token Verified</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- BINARY FILE COMPILE PIPELINE ---
def generate_excel_stream(target_df):
    mem_buffer = io.BytesIO()
    with pd.ExcelWriter(mem_buffer, engine='xlsxwriter') as b_writer:
        target_df.to_excel(b_writer, index=False, sheet_name='Operations_Export')
    return mem_buffer.getvalue()

# --- MANAGEMENT INTERFACE CONTROL MATRIX ---
t_overview, t_attendance, t_invoices, t_reporting = st.tabs([
    "🏠 Corporate Overview", 
    "📝 Daily Attendance Matrix", 
    "🧾 Tax Invoices Registry", 
    "📊 Chronological Reports Export"
])

# 1. MANAGEMENT OVERVIEW
with t_overview:
    st.markdown('<div class="executive-card-node" style="margin-bottom: 25px;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #0f172a; font-weight: 800; margin-top:0; letter-spacing:-0.5px;'>Command Operations Matrix</h3>", unsafe_allow_html=True)
    st.write("Real-time aggregated corporate performance indicators tracking cross-border human capital alongside archived transactions.")
    
    st1, st2, st3 = st.columns(3)
    with st1:
        st.markdown(f'<div style="background:#f8fafc; padding:20px; border-radius:12px; border:1px solid #e2e8f0;"><span style="font-size:12px; font-weight:700; color:#64748b; text-transform:uppercase;">Master Active Workforce</span><div class="giant-stat-value">{len(st.session_state["master_labor_pool"])} <span style="font-size:14px; color:#94a3b8; font-weight:400;">Units</span></div></div>', unsafe_allow_html=True)
    with st2:
        st.markdown(f'<div style="background:#f8fafc; padding:20px; border-radius:12px; border:1px solid #e2e8f0;"><span style="font-size:12px; font-weight:700; color:#64748b; text-transform:uppercase;">Archived Invoices Volume</span><div class="giant-stat-value">{len(st.session_state["invoice_database"])} <span style="font-size:14px; color:#94a3b8; font-weight:400;">Records</span></div></div>', unsafe_allow_html=True)
    with st3:
        gross_sum_value = sum(float(i['Total Amount']) for i in st.session_state['invoice_database']) if st.session_state['invoice_database'] else 0.0
        st.markdown(f'<div style="background:rgba(234,179,8,0.02); padding:20px; border-radius:12px; border:1px solid rgba(234,179,8,0.15);"><span style="font-size:12px; font-weight:700; color:#ca8a04; text-transform:uppercase;">Gross Value Transacted</span><div class="giant-stat-value" style="color:#ca8a04;">{gross_sum_value:.3f} <span style="font-size:14px; font-weight:600;">OMR</span></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. DAILY ATTENDANCE MATRIX
with t_attendance:
    st.subheader("Field Deployment Roster Logs")
    target_date_context = st.date_input("Target Calendar Date Focus Frame", datetime.now(), key="work_date_context")
    
    col_w_l, col_w_r = st.columns(2)
    with col_w_l:
        st.markdown('<div class="executive-card-node">', unsafe_allow_html=True)
        st.markdown("<h4>🔍 Query Master Workforce Pools</h4>", unsafe_allow_html=True)
        search_filter_string = st.text_input("Filter via Identity Code / Worker Full Name", placeholder="Scan system tracks...")
        
        if search_filter_string:
            if not st.session_state['master_labor_pool']:
                st.warning("Master tracking database arrays contain zero current profiles.")
            else:
                matches = [w for w in st.session_state['master_labor_pool'] if search_filter_string.lower() in w['Name'].lower() or search_filter_string in w['Employee ID']]
                if matches:
                    for entry_item in matches:
                        if st.button(f"Deploy Unit: {entry_item['Name']} ({entry_item['Employee ID']})", key=f"dpl_{entry_item['Employee ID']}"):
                            if any(q['Employee ID'] == entry_item['Employee ID'] for q in st.session_state['daily_active_roster']):
                                st.error("Target employee unit already active inside today's open staging frame queue.")
                            else:
                                st.session_state['daily_active_roster'].append({
                                    "Employee ID": entry_item["Employee ID"], "Name": entry_item["Name"],
                                    "Company": entry_item["Company"], "Remarks": ""
                                })
                                st.success(f"Staged {entry_item['Name']}.")
                                st.rerun()
                else:
                    st.info("No structural personnel records correlate with query filters.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_w_r:
        st.markdown('<div class="executive-card-node">', unsafe_allow_html=True)
        st.markdown("<h4>➕ First-Time Individual Registration Flow</h4>", unsafe_allow_html=True)
        sub_id = st.text_input("Assign Unique Employee ID")
        sub_name = st.text_input("Legal Individual Full Name")
        sub_comp = st.text_input("Corporate Vendor Affiliation / Company Entity")
        
        if st.button("Commit Profile Creation", use_container_width=True):
            if sub_id and sub_name and sub_comp:
                if any(k['Employee ID'] == sub_id for k in st.session_state['master_labor_pool']):
                    st.error("Data tracking conflict. Assigned Employee ID code already holds valid master assignment profile.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": sub_id, "Name": sub_name, "Company": sub_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": sub_id, "Name": sub_name, "Company": sub_comp, "Remarks": ""})
                    st.success("New operational vector built successfully.")
                    st.rerun()
            else:
                st.warning("Execution paused. All data parameter inputs remain mandatory.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📋 Staged Attendance Matrix Deployment Queue")
    if not st.session_state['daily_active_roster']:
        st.info("Staging vectors hold zero deployment entries presently.")
    else:
        index_drop_target = None
        for i_idx, i_worker in enumerate(st.session_state['daily_active_roster']):
            ln1, ln2, ln3, ln4, ln5 = st.columns([1.5, 2, 2, 3, 1])
            ln1.write(f"**ID Code:** {i_worker['Employee ID']}")
            ln2.write(f"**Name:** {i_worker['Name']}")
            ln3.write(f"**Company:** {i_worker['Company']}")
            st.session_state['daily_active_roster'][i_idx]["Remarks"] = ln4.text_input("Operational Notes", key=f"m_rem_{i_idx}", value=i_worker["Remarks"], label_visibility="collapsed")
            if ln5.button("❌ Drop", key=f"m_drop_{i_idx}"):
                index_drop_target = i_idx
                
        if index_drop_target is not None:
            st.session_state['daily_active_roster'].pop(index_drop_target)
            st.rerun()
            
        if st.button("💾 Finalize & Commit Daily Attendance Sheets", type="primary", use_container_width=True):
            for log_row in st.session_state['daily_active_roster']:
                st.session_state['attendance_database'].append({
                    "Date": str(target_date_context), "Employee ID": log_row["Employee ID"],
                    "Name": log_row["Name"], "Company": log_row["Company"],
                    "Status": "Present", "Remarks": log_row["Remarks"]
                })
            st.success("Log sheets archived securely inside core repositories.")
            st.session_state['daily_active_roster'] = []
            st.rerun()

# 3. TAX INVOICES REGISTRY
with t_invoices:
    st.subheader("Commercial Transaction & Invoice Audit Controls")
    
    st.markdown('<div class="executive-card-node">', unsafe_allow_html=True)
    st.markdown("<h4>📥 Archive Tax Invoice Document Parameters</h4>", unsafe_allow_html=True)
    iv_c1, iv_c2 = st.columns(2)
    with iv_c1:
        f_inv_date = st.date_input("Document Legal Date of Issue", datetime.now(), key="f_inv_date_cal")
        f_inv_num = st.text_input("Document Serial Number Focus (Invoice No.)", placeholder="e.g. A204306")
    with iv_c2:
        f_inv_total = st.number_input("Invoice Total Gross Financial Valuation (OMR)", min_value=0.000, step=0.001, format="%.3f")
        f_inv_vat = st.number_input("Calculated Tax Value Component (5% VAT OMR)", min_value=0.000, step=0.001, format="%.3f")
        
    if st.button("🔒 Archive Transaction Metadata Into Secure Ledgers", type="primary"):
        if f_inv_num and f_inv_total > 0:
            st.session_state['invoice_database'].append({
                "Date": str(f_inv_date),
                "Invoice Number": f_inv_num,
                "Total Amount": f"{f_inv_total:.3f}",
                "VAT Amount": f"{f_inv_vat:.3f}",
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"Commercial purchase transaction line item [{f_inv_num}] logged under Al Rabhan Trading registries.")
            st.rerun()
        else:
            st.error("Input validation exception. Please provide valid transaction parameters.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Logged Commercial Invoices")
    if st.session_state['invoice_database']:
        st.dataframe(pd.DataFrame(st.session_state['invoice_database']), use_container_width=True)
    else:
        st.info("System ledger arrays hold zero commercial transaction files currently.")

# 4. CHRONOLOGICAL REPORTS EXPORT
with t_reporting:
    st.subheader("Chronological Filter Systems & Binary Ledger Compilation Panels")
    
    st.markdown('<div class="executive-card-node">', unsafe_allow_html=True)
    sorting_scope = st.radio("Specify Analytical Report Target Chronology Scope Focus:", ["View Complete History Logs", "Filter Target Monthly Matrix View", "Filter Target Yearly Matrix View"], horizontal=True)
    
    var_m = datetime.now().strftime("%m")
    var_y = datetime.now().strftime("%Y")
    
    if sorting_scope == "Filter Target Monthly Matrix View":
        bx1, bx2 = st.columns(2)
        var_m = bx1.selectbox("Filter Target Month Focus Block", [f"{n:02d}" for n in range(1, 13)], index=int(datetime.now().month)-1)
        var_y = bx2.selectbox("Filter Target Year Focus Block", [str(y) for y in range(2025, 2032)], key="rep_m_yr")
    elif sorting_scope == "Filter Target Yearly Matrix View":
        var_y = st.selectbox("Filter Target Year Focus Block", [str(y) for y in range(2025, 2032)], key="rep_y_yr")
    st.markdown('</div>', unsafe_allow_html=True)

    col_out_l, col_out_r = st.columns(2)
    
    with col_out_l:
        st.markdown("#### 📊 Filtered Workforce Shift Matrix Ledgers")
        if st.session_state['attendance_database']:
            df_att_master = pd.DataFrame(st.session_state['attendance_database'])
            df_att_master['D_Obj'] = pd.to_datetime(df_att_master['Date'])
            
            if sorting_scope == "Filter Target Monthly Matrix View":
                df_res_att = df_att_master[(df_att_master['D_Obj'].dt.strftime('%m') == var_m) & (df_att_master['D_Obj'].dt.strftime('%Y') == var_y)]
            elif sorting_scope == "Filter Target Yearly Matrix View":
                df_res_att = df_att_master[df_att_master['D_Obj'].dt.strftime('%Y') == var_y]
            else:
                df_res_att = df_att_master
                
            if not df_res_att.empty:
                tally_summary_att = df_res_att.groupby(["Employee ID", "Name", "Company"]).size().reset_index(name="Aggregated Total Shifts Worked")
                st.dataframe(tally_summary_att, use_container_width=True)
                
                bin_excel_workforce = generate_excel_stream(tally_summary_att)
                st.download_button(label="📥 Download Workforce Summary (.xlsx)", data=bin_excel_workforce, file_name=f"Workforce_Operations_Report_{var_y}_{var_m}.xlsx", mime="application/vnd.ms-excel", key="down_att_excel")
            else:
                st.info("No workforce operational data logs match targeted sorting frames.")
        else:
            st.info("Workforce shift databases hold zero data logs currently.")

    with col_out_r:
        st.markdown("#### 🧾 Filtered Commercial Revenue Ledgers")
        if st.session_state['invoice_database']:
            df_inv_master = pd.DataFrame(st.session_state['invoice_database'])
            df_inv_master['D_Obj'] = pd.to_datetime(df_inv_master['Date'])
            
            if sorting_scope == "Filter Target Monthly Matrix View":
                df_res_inv = df_inv_master[(df_inv_master['D_Obj'].dt.strftime('%m') == var_m) & (df_inv_master['D_Obj'].dt.strftime('%Y') == var_y)]
            elif sorting_scope == "Filter Target Yearly Matrix View":
                df_res_inv = df_inv_master[df_inv_master['D_Obj'].dt.strftime('%Y') == var_y]
            else:
                df_res_inv = df_inv_master
                
            if not df_res_inv.empty:
                tally_summary_inv = df_res_inv[["Date", "Invoice Number", "Total Amount", "VAT Amount"]]
                st.dataframe(tally_summary_inv, use_container_width=True)
                
                bin_excel_financial = generate_excel_stream(tally_summary_inv)
                st.download_button(label="📥 Download Commercial Ledger Report (.xlsx)", data=bin_excel_financial, file_name=f"Financial_Ledger_Report_{var_y}_{var_m}.xlsx", mime="application/vnd.ms-excel", key="down_inv_excel")
            else:
                st.info("No corporate transaction line items map inside specified filter windows.")
        else:
            st.info("Financial ledger records contain zero transactional metrics.")