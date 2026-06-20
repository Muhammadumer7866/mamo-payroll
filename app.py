import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- ULTRA-PREMIUM EXECUTIVE CONFIGURATION ---
st.set_page_config(page_title="Al Rabhan Trading - ERP", layout="wide", initial_sidebar_state="collapsed")

# --- HIGH-END CINEMATIC GRAPHICS ENGINE (CSS) ---
st.markdown("""
    <style>
    /* Global smooth fonts and deep luxury corporate tone */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    .stApp {
        background-color: #0b0f19;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #f1f5f9;
        overflow-x: hidden;
    }

    /* --- ANIMATION KEYFRAMES (THE MOVEMENT) --- */
    @keyframes premiumFadeUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes smoothPulse {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 0.02; }
        50% { transform: translate(-50%, -50%) scale(1.05); opacity: 0.05; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 0.02; }
    }
    @keyframes floatGraphic {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    /* Dynamic Luxury Bold Watermark Logo */
    .bold-watermark {
        position: fixed;
        top: 55%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 13vw;
        font-weight: 800;
        letter-spacing: 15px;
        background: linear-gradient(135deg, #ca8a04 0%, #1e40af 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        opacity: 0.03;
        z-index: 0;
        pointer-events: none;
        text-align: center;
        user-select: none;
        animation: smoothPulse 8s ease-in-out infinite;
    }

    /* --- PREMIUM SPLIT INTERFACE SCREEN --- */
    .luxury-login-container {
        display: flex;
        min-height: 88vh;
        margin: 20px auto;
        max-width: 1200px;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 28px;
        backdrop-filter: blur(20px);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        overflow: hidden;
        animation: premiumFadeUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    .panel-left {
        flex: 1.1;
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: #0f172a;
    }

    .panel-right {
        flex: 1.2;
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-left: 1px solid rgba(255, 255, 255, 0.05);
        position: relative;
    }

    /* Luxury Corporate CSS Branding Logo */
    .art-logo-box {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 30px;
    }
    .art-logo-icon {
        background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%);
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        color: #0f172a;
        font-size: 18px;
        box-shadow: 0 4px 14px rgba(234, 179, 8, 0.3);
    }
    .art-logo-text {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 0.5px;
    }

    /* Interactive UI Blocks for Right Sidebar Banner */
    .premium-showcase-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.07);
        padding: 24px;
        border-radius: 18px;
        margin-top: 30px;
        animation: floatGraphic 6s ease-in-out infinite;
    }

    /* Post-Login Dashboard Custom Design Elements */
    .modern-dashboard-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    .modern-dashboard-card:hover {
        transform: translateY(-5px);
        border-color: rgba(234, 179, 8, 0.3);
    }
    .accent-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP SYSTEM STATE RETENTION ---
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

# --- RENDER IMMERSIVE LOGGING PORTAL ---
if not st.session_state['logged_in']:
    # Pure structured layout injection
    st.markdown("""
        <div class="luxury-login-container">
            <!-- Left Interaction Form Column -->
            <div class="panel-left">
                <div class="art-logo-box">
                    <div class="art-logo-icon">A</div>
                    <div class="art-logo-text">Al Rabhan Trading</div>
                </div>
                <h2 style="color: #ffffff; font-weight: 700; font-size: 32px; margin-bottom: 8px;">Portal Authentication</h2>
                <p style="color: #94a3b8; font-size: 14px; margin-bottom: 40px; line-height: 1.5;">
                    Please input your enterprise identity credentials below to request full database entry validation.
                </p>
            </div>
            <!-- Right Corporate Aesthetics Banner Column -->
            <div class="panel-right">
                <span style="color: #eab308; text-transform: uppercase; font-size: 11px; font-weight: 700; letter-spacing: 2px;">Sultanate of Oman ERP System</span>
                <h1 style="color: #ffffff; font-size: 38px; font-weight: 800; line-height: 1.25; margin: 15px 0 20px 0;">
                    Optimized Control For Modern Trade & Labor Operations.
                </h1>
                <p style="color: #cbd5e1; font-size: 15px; line-height: 1.6; margin: 0;">
                    A highly responsive workspace developed exclusively for Al Rabhan Trading to seamlessly map personnel deployment histories alongside real-time VAT tax invoice metrics archiving.
                </p>
                <div class="premium-showcase-card">
                    <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                        <span style="color:#eab308; font-weight:700; font-size:14px;">⚡ Real-time Compiled Dashboards</span>
                    </div>
                    <p style="color:#94a3b8; font-size:13px; margin:0; line-height:1.5;">
                        Features single-click automated binary Excel report compiling for direct internal accounting submission and daily shift rosters analytics extraction.
                    </p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Injecting the input fields clean and native overlaying over panel-left perfectly 
    with st.container():
        c_left_form, c_right_void = st.columns([1, 1.1])
        with c_left_form:
            st.markdown('<div style="position: relative; margin-top: -510px; padding: 0 60px; max-width: 520px;">', unsafe_allow_html=True)
            auth_email = st.text_input("Corporate Email Address", placeholder="e.g. admin@construction.om")
            auth_password = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
            
            st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
            if st.button("Verify & Authenticate Node Connection", type="primary", use_container_width=True):
                if auth_email == "admin@construction.om" and auth_password == "Oman#Secure2026":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Access Refused. Security string parameters failed validation protocols.")
            st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

# --- BACKDROP DYNAMIC MOTION WATERMARK ---
st.markdown('<div class="bold-watermark">AL RABHAN</div>', unsafe_allow_html=True)

# --- INTERNAL SECURE SYSTEM HEADER DISPLAY ---
st.markdown("""
    <div style="background: rgba(15,23,42,0.8); backdrop-filter:blur(10px); padding: 20px 40px; border-bottom: 1px solid rgba(255,255,255,0.06); margin: -50px -50px 35px -50px; display: flex; justify-content: space-between; align-items: center; animation: premiumFadeUp 0.8s ease out;">
        <div style="display:flex; align-items:center; gap:15px;">
            <div style="background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%); width:36px; height:36px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-weight:800; color:#0f172a; font-size:16px;">A</div>
            <div>
                <h1 style="font-size: 22px; font-weight: 700; color: #ffffff; margin: 0; letter-spacing:-0.5px;">Al Rabhan Trading</h1>
                <p style="font-size: 11px; color: #94a3b8; margin: 0; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px;">Corporate Core ERP Operations Node</p>
            </div>
        </div>
        <div style="background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.2); padding: 6px 14px; border-radius: 20px; display:flex; align-items:center; gap:8px;">
            <div style="width:8px; height:8px; background:#22c55e; border-radius:50%;"></div>
            <span style="font-size: 12px; font-weight: 600; color: #4ade80; letter-spacing:0.5px;">SYSTEM LIVE</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- GENERAL EXCEL LEDGER COMPILER UNIT ---
def compile_excel_ledger(target_dataframe):
    io_stream = io.BytesIO()
    with pd.ExcelWriter(io_stream, engine='xlsxwriter') as workbook_writer:
        target_dataframe.to_excel(workbook_writer, index=False, sheet_name='ERP_Export_Master')
    return io_stream.getvalue()

# --- WORKSPACE TABS INITIALIZATION ---
tab_home, tab_workforce, tab_invoices, tab_reports = st.tabs([
    "🏠 Management Overview", 
    "📝 Daily Attendance Matrix", 
    "🧾 Tax Invoices Registry", 
    "📊 Granular Report Compilers"
])

# --- 1. CORPORATE SUMMARY PANEL ---
with tab_home:
    st.markdown('<div class="modern-dashboard-card" style="margin-bottom: 25px;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ffffff; font-weight: 700; margin-top:0;'>Operational Command Console</h3>", unsafe_allow_html=True)
    st.write("Central tracking arrays mapping cross-border field operations, logistics workforces shift logs, and commercial sales invoice records.")
    
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.markdown(f'<div style="background:rgba(255,255,255,0.02); padding:20px; border-radius:14px; border:1px solid rgba(255,255,255,0.05);"><h5>Active Master Personnel</h5><div class="accent-number">{len(st.session_state["master_labor_pool"])} <span style="font-size:14px; color:#64748b;">Registered</span></div></div>', unsafe_allow_html=True)
    with col_d2:
        st.markdown(f'<div style="background:rgba(255,255,255,0.02); padding:20px; border-radius:14px; border:1px solid rgba(255,255,255,0.05);"><h5>Logged Commercial Invoices</h5><div class="accent-number">{len(st.session_state["invoice_database"])} <span style="font-size:14px; color:#64748b;">Records</span></div></div>', unsafe_allow_html=True)
    with col_d3:
        gross_volume_calc = sum(float(v['Total Amount']) for v in st.session_state['invoice_database']) if st.session_state['invoice_database'] else 0.0
        st.markdown(f'<div style="background:rgba(234,179,8,0.02); padding:20px; border-radius:14px; border:1px solid rgba(234,179,8,0.1);"><h5>Gross Audited Revenue</h5><div class="accent-number" style="background:linear-gradient(135deg, #fef08a 0%, #eab308 100%); -webkit-background-clip: text;">{gross_volume_calc:.3f} <span style="font-size:16px; color:#eab308; font-weight:600;">OMR</span></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. ATTENDANCE OPERATIONS MATRIX ---
with tab_workforce:
    st.subheader("Daily Field Roster Deployment Engine")
    selected_roster_date = st.date_input("Target Operational Date Window", datetime.now(), key="roster_date_anchor")
    
    col_w_left, col_w_right = st.columns(2)
    with col_w_left:
        st.markdown('<div class="modern-dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4>🔍 Query Master Roster Registry</h4>", unsafe_allow_html=True)
        pool_query = st.text_input("Filter via Identity Code Sequence / Name", placeholder="Scan databases...")
        
        if pool_query:
            if not st.session_state['master_labor_pool']:
                st.warning("Primary workforce directories possess zero cataloged metrics.")
            else:
                matched_pool = [x for x in st.session_state['master_labor_pool'] if pool_query.lower() in x['Name'].lower() or pool_query in x['Employee ID']]
                if matched_pool:
                    for individual in matched_pool:
                        if st.button(f"Stage Deployment: {individual['Name']} ({individual['Employee ID']})", key=f"p_stg_{individual['Employee ID']}"):
                            if any(e['Employee ID'] == individual['Employee ID'] for e in st.session_state['daily_active_roster']):
                                st.error("Target employee unit already deployed inside today's open staging frame.")
                            else:
                                st.session_state['daily_active_roster'].append({
                                    "Employee ID": individual["Employee ID"], "Name": individual["Name"],
                                    "Company": individual["Company"], "Remarks": ""
                                })
                                st.success(f"Staged {individual['Name']} successfully.")
                                st.rerun()
                else:
                    st.info("No matching individual entities discovered for target query criteria.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_w_right:
        st.markdown('<div class="modern-dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4>➕ Provision New Corporate Personnel</h4>", unsafe_allow_html=True)
        in_em_id = st.text_input("Define Unique Employee ID")
        in_em_name = st.text_input("Legal Individual Full Name String")
        in_em_comp = st.text_input("Assigned Subcontracting Enterprise / Vendor Name")
        
        if st.button("Commit Node Provision Flow", use_container_width=True):
            if in_em_id and in_em_name and in_em_comp:
                if any(p['Employee ID'] == in_em_id for p in st.session_state['master_labor_pool']):
                    st.error("Structural conflict error. Designated ID code already holds valid master assignment profile.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": in_em_id, "Name": in_em_name, "Company": in_em_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": in_em_id, "Name": in_em_name, "Company": in_em_comp, "Remarks": ""})
                    st.success("New operational profile injected into live database tracks.")
                    st.rerun()
            else:
                st.warning("All input containers are structural pre-requisites.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📋 Current Staged Deployment Queue Frame")
    if not st.session_state['daily_active_roster']:
        st.info("Deployment staging logs hold zero entries for this operational sequence.")
    else:
        removal_index_target = None
        for r_index, r_worker in enumerate(st.session_state['daily_active_roster']):
            cl1, cl2, cl3, cl4, cl5 = st.columns([1.5, 2, 2, 3, 1])
            cl1.write(f"**ID Code:** {r_worker['Employee ID']}")
            cl2.write(f"**Legal Name:** {r_worker['Name']}")
            cl3.write(f"**Vendor Entity:** {r_worker['Company']}")
            st.session_state['daily_active_roster'][r_index]["Remarks"] = cl4.text_input("Operational Notes", key=f"f_rem_{r_index}", value=r_worker["Remarks"], label_visibility="collapsed")
            if cl5.button("❌ Drop", key=f"f_drop_{r_index}"):
                removal_index_target = r_index
                
        if removal_index_target is not None:
            st.session_state['daily_active_roster'].pop(removal_index_target)
            st.rerun()
            
        if st.button("💾 Finalize Shift Attendance Log Ledger", type="primary", use_container_width=True):
            for active_item in st.session_state['daily_active_roster']:
                st.session_state['attendance_database'].append({
                    "Date": str(selected_roster_date), "Employee ID": active_item["Employee ID"],
                    "Name": active_item["Name"], "Company": active_item["Company"],
                    "Status": "Present", "Remarks": active_item["Remarks"]
                })
            st.success("Daily attendance roster blocks verified and committed to persistent database streams.")
            st.session_state['daily_active_roster'] = []
            st.rerun()

# --- 3. TAX INVOICE TRACKING REGISTRY PANEL ---
with tab_invoices:
    st.subheader("Commercial Sales & Tax Procurement Audit Registry")
    
    st.markdown('<div class="modern-dashboard-card">', unsafe_allow_html=True)
    st.markdown("<h4>📥 Archive Raw Tax Invoice Parameters</h4>", unsafe_allow_html=True)
    in_col_1, in_col_2 = st.columns(2)
    with in_col_1:
        reg_inv_date = st.date_input("Document Legal Date of Issue", datetime.now(), key="invoice_calendar_date")
        reg_inv_serial = st.text_input("Document Serial Number Focus (Invoice No.)", placeholder="e.g. A204306")
    with in_col_2:
        reg_inv_total = st.number_input("Invoice Total Gross Financial Valuation (OMR)", min_value=0.000, step=0.001, format="%.3f")
        reg_inv_vat = st.number_input("Calculated Tax Value Component (5% VAT OMR)", min_value=0.000, step=0.001, format="%.3f")
        
    if st.button("🔒 Archive Document Metadata Into Secure Ledgers", type="primary"):
        if reg_inv_serial and reg_inv_total > 0:
            st.session_state['invoice_database'].append({
                "Date": str(reg_inv_date),
                "Invoice Number": reg_inv_serial,
                "Total Amount": f"{reg_inv_total:.3f}",
                "VAT Amount": f"{reg_inv_vat:.3f}",
                "System Operational Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"Commercial purchase document entry [{reg_inv_serial}] logged under corporate parameters successfully.")
            st.rerun()
        else:
            st.error("Input metadata validation error. Please verify financial data parameters.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Logged Commercial Invoices")
    if st.session_state['invoice_database']:
        st.dataframe(pd.DataFrame(st.session_state['invoice_database']), use_container_width=True)
    else:
        st.info("Commercial transaction indices contain zero archived ledger line items.")

# --- 4. EXPORT AND REPORT GENERATION PANEL ---
with tab_reports:
    st.subheader("Granular Operational Report Compilers & Binary Downloads")
    
    st.markdown('<div class="modern-dashboard-card">', unsafe_allow_html=True)
    chronological_scope = st.radio("Specify Target Aggregation Timeline Scope Focus:", ["View Complete History Logs", "Compile Target Monthly Matrix View", "Compile Target Yearly Matrix View"], horizontal=True)
    
    assigned_m_code = datetime.now().strftime("%m")
    assigned_y_code = datetime.now().strftime("%Y")
    
    if chronological_scope == "Compile Target Monthly Matrix View":
        bx1, bx2 = st.columns(2)
        assigned_m_code = bx1.selectbox("Filter Target Month Focus Block", [f"{n:02d}" for n in range(1, 13)], index=int(datetime.now().month)-1)
        assigned_y_code = bx2.selectbox("Filter Target Year Focus Block", [str(y) for y in range(2025, 2032)], key="m_anchor_yr")
    elif chronological_scope == "Compile Target Yearly Matrix View":
        assigned_y_code = st.selectbox("Filter Target Year Focus Block", [str(y) for y in range(2025, 2032)], key="y_anchor_yr")
    st.markdown('</div>', unsafe_allow_html=True)

    c_output_left, c_output_right = st.columns(2)
    
    with c_output_left:
        st.markdown("#### 📊 Filtered Workforce Shift Matrix Ledgers")
        if st.session_state['attendance_database']:
            df_att_engine = pd.DataFrame(st.session_state['attendance_database'])
            df_att_engine['D_Obj'] = pd.to_datetime(df_att_engine['Date'])
            
            if chronological_scope == "Compile Target Monthly Matrix View":
                df_attendance_filtered = df_att_engine[(df_att_engine['D_Obj'].dt.strftime('%m') == assigned_m_code) & (df_att_engine['D_Obj'].dt.strftime('%Y') == assigned_y_code)]
            elif chronological_scope == "Compile Target Yearly Matrix View":
                df_attendance_filtered = df_att_engine[df_att_engine['D_Obj'].dt.strftime('%Y') == assigned_y_code]
            else:
                df_attendance_filtered = df_att_engine
                
            if not df_attendance_filtered.empty:
                aggregated_shift_tally_sheet = df_attendance_filtered.groupby(["Employee ID", "Name", "Company"]).size().reset_index(name="Total Shifts Logged")
                st.dataframe(aggregated_shift_tally_sheet, use_container_width=True)
                
                excel_binary_workforce = compile_excel_ledger(aggregated_shift_tally_sheet)
                st.download_button(label="📥 Download Workforce Summary (.xlsx)", data=excel_binary_workforce, file_name=f"Workforce_Operations_Report_{assigned_y_code}_{assigned_m_code}.xlsx", mime="application/vnd.ms-excel", key="dl_workforce_btn")
            else:
                st.info("No recorded deployment profiles found corresponding with target timeline anchors.")
        else:
            st.info("Workforce shift databases hold zero data logs currently.")

    with c_output_right:
        st.markdown("#### 🧾 Filtered Commercial Revenue Ledgers")
        if st.session_state['invoice_database']:
            df_invoice_engine = pd.DataFrame(st.session_state['invoice_database'])
            df_invoice_engine['D_Obj'] = pd.to_datetime(df_invoice_engine['Date'])
            
            if chronological_scope == "Compile Target Monthly Matrix View":
                df_invoices_filtered = df_invoice_engine[(df_invoice_engine['D_Obj'].dt.strftime('%m') == assigned_m_code) & (df_invoice_engine['D_Obj'].dt.strftime('%Y') == assigned_y_code)]
            elif chronological_scope == "Compile Target Yearly Matrix View":
                df_invoices_filtered = df_invoice_engine[df_invoice_engine['D_Obj'].dt.strftime('%Y') == assigned_y_code]
            else:
                df_invoices_filtered = df_invoice_engine
                
            if not df_invoices_filtered.empty:
                aggregated_invoice_tally_sheet = df_invoices_filtered[["Date", "Invoice Number", "Total Amount", "VAT Amount"]]
                st.dataframe(aggregated_invoice_tally_sheet, use_container_width=True)
                
                excel_binary_financial = compile_excel_ledger(aggregated_invoice_tally_sheet)
                st.download_button(label="📥 Download Commercial Ledger Report (.xlsx)", data=excel_binary_financial, file_name=f"Financial_Ledger_Report_{assigned_y_code}_{assigned_m_code}.xlsx", mime="application/vnd.ms-excel", key="dl_financial_btn")
            else:
                st.info("No corporate transaction line items map inside specified filter windows.")
        else:
            st.info("Financial ledger records contain zero transactional metrics.")