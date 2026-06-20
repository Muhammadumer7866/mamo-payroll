import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- SYSTEM CONFIG ENGINE ---
st.set_page_config(page_title="Al Rabhan Trading - Dashboard", layout="wide", initial_sidebar_state="collapsed")

# --- EXECUTIVE THEME STYLING ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Overrides */
    .stApp {
        background-color: #f1f5f9;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Modern Card Styler */
    .dashboard-card {
        background: #ffffff;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
        margin-bottom: 25px;
    }
    
    /* Section Headers */
    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Custom Metric Blocks */
    .stat-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }
    
    /* Clean Input Borders */
    div.stTextInput > div > div > input, div.stNumberInput > div > div > input {
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
    }
    
    /* Custom Tabs Row styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# --- STATE ARCHITECTURE ---
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

# --- GATEWAY SECURE ENTRY ---
if not st.session_state['logged_in']:
    st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
    col_left, col_right = st.columns([1.1, 1], gap="large")
    
    with col_left:
        st.markdown("""
            <div style="display: flex; align-items: flex-end; gap: 6px; height: 70px; margin-bottom: 8px;">
                <div style="width: 16px; height: 42px; background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%); clip-path: polygon(100% 0, 0 40%, 0 100%, 100% 100%); border-radius: 2px;"></div>
                <div style="width: 20px; height: 65px; background: linear-gradient(135deg, #475569 0%, #0f172a 100%); clip-path: polygon(50% 0, 0 15%, 0 100%, 100% 100%, 100% 15%); border-radius: 2px;"></div>
                <div style="width: 14px; height: 50px; background: linear-gradient(135deg, #fef08a 0%, #eab308 100%); clip-path: polygon(0 0, 100% 30%, 100% 100%, 0 100%); border-radius: 2px;"></div>
            </div>
            <div style="font-size: 34px; font-weight: 800; color: #0f172a; letter-spacing: 2px; text-transform: uppercase; margin: 0; line-height: 1.1;">Al Rabhan</div>
            <div style="font-size: 16px; font-weight: 600; color: #ca8a04; letter-spacing: 8px; text-transform: uppercase; margin: 4px 0 12px 0;">Trading</div>
            <div style="font-size: 10px; font-weight: 600; color: #64748b; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 30px; border-top: 1px solid #e2e8f0; padding-top: 6px;">CONSTRUCTION | QUALITY | TRUST</div>
            <h2 style='color: #0f172a; font-weight: 800; font-size: 26px; margin: 0 0 4px 0;'>Welcome Back</h2>
            <p style='color: #64748b; font-size: 13px; margin: 0 0 25px 0;'>Please authenticate administrative level keys to open the operations panel.</p>
        """, unsafe_allow_html=True)
        
        gate_id = st.text_input("Corporate ID / Email Address", placeholder="e.g. admin@construction.om")
        gate_key = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
        
        st.markdown('<div style="margin-top: 20px;">', unsafe_allow_html=True)
        if st.button("Log In to System", type="primary", use_container_width=True):
            if gate_id == "admin@construction.om" and gate_key == "Oman#Secure2026":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Access Refused. Security parameters failed evaluation.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_right:
        with st.container(border=True):
            st.markdown("""
                <div style="background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); padding: 40px; border-radius: 14px; color: #ffffff; min-height: 480px;">
                    <div style="background: rgba(234, 179, 8, 0.15); border: 1px solid rgba(234, 179, 8, 0.3); color: #fef08a; padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: inline-block; margin-bottom: 25px;">
                        Oman Enterprise Infrastructure
                    </div>
                    <h3 style="font-size: 32px; font-weight: 800; line-height: 1.2; color: #ffffff; margin-bottom: 15px;">Effortlessly manage your workforce and corporate financials.</h3>
                    <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 30px;">
                        Consolidated cloud tracking console custom engineered for real-time field operations, active shift logs control, and Omani Tax Invoice registry archiving.
                    </p>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); padding: 18px; border-radius: 12px;">
                        <span style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: #eab308; letter-spacing: 1px;">CONSTRUCTION | QUALITY | TRUST</span>
                        <p style="margin: 6px 0 0 0; font-size: 13px; color: #94a3b8;">Automated analytical report engine compiles binary Excel ledgers instantaneously.</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    st.stop()

# --- MAIN INDUSTRIAL SYSTEM VIEWPORT ---
st.markdown("""
    <div style="background: linear-gradient(90deg, #0f172a 0%, #1e3a8a 100%); padding: 24px 40px; border-radius: 16px; margin-bottom: 35px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
        <div>
            <h1 style="font-size: 24px; font-weight: 800; color: #ffffff; margin: 0; letter-spacing:-0.5px;">AL RABHAN TRADING SYSTEM CONTROL</h1>
            <p style="font-size: 12px; color: #eab308; margin: 0; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Sultanate of Oman • Management Node Active</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2);">
            <span style="font-size: 13px; font-weight: 600; color: #ffffff;">🔒 Session Token: Secure Enterprise</span>
        </div>
    </div>
""", unsafe_allow_html=True)

def generate_excel_stream(target_df):
    mem_buffer = io.BytesIO()
    with pd.ExcelWriter(mem_buffer, engine='xlsxwriter') as b_writer:
        target_df.to_excel(b_writer, index=False, sheet_name='Operations_Export')
    return mem_buffer.getvalue()

# TABBED ROUTING NAVIGATION
t_overview, t_attendance, t_invoices, t_reporting = st.tabs([
    "🏠 Corporate Command Hub", 
    "📝 Attendance Roster Module", 
    "🧾 Tax Invoices Registry", 
    "📊 Analytical Ledger Exports"
])

# 1. OVERVIEW HUB
with t_overview:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Real-Time Operations Overview Matrix</div>', unsafe_allow_html=True)
    st.write("Aggregated system metrics reflecting current field deployment metrics and global transacted ledger archives.")
    
    st1, st2, st3 = st.columns(3, gap="large")
    with st1:
        st.markdown(f"""
            <div class="stat-box">
                <div style="font-size: 13px; font-weight: 600; color: #94a3b8; text-transform: uppercase;">Active Registered Workforce</div>
                <div style="font-size: 32px; font-weight: 800; color: #eab308; margin-top: 5px;">{len(st.session_state['master_labor_pool'])} Units</div>
            </div>
        """, unsafe_allow_html=True)
    with st2:
        st.markdown(f"""
            <div class="stat-box">
                <div style="font-size: 13px; font-weight: 600; color: #94a3b8; text-transform: uppercase;">Archived Tax Documents</div>
                <div style="font-size: 32px; font-weight: 800; color: #38bdf8; margin-top: 5px;">{len(st.session_state['invoice_database'])} Invoices</div>
            </div>
        """, unsafe_allow_html=True)
    with st3:
        gross_sum_value = sum(float(i['Total Amount']) for i in st.session_state['invoice_database']) if st.session_state['invoice_database'] else 0.0
        st.markdown(f"""
            <div class="stat-box">
                <div style="font-size: 13px; font-weight: 600; color: #94a3b8; text-transform: uppercase;">Gross Financial Volume</div>
                <div style="font-size: 32px; font-weight: 800; color: #4ade80; margin-top: 5px;">{gross_sum_value:.3f} OMR</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. LABOUR ATTENDANCE MODULE
with t_attendance:
    # Top Panel Configuration Block
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📅 Target Context Matrix Configuration</div>', unsafe_allow_html=True)
    target_date_context = st.date_input("Target Calendar Date Focus Frame", datetime.now(), key="work_date_context")
    st.markdown('</div>', unsafe_allow_html=True)

    col_w_l, col_w_r = st.columns(2, gap="large")
    
    with col_w_l:
        st.markdown('<div class="dashboard-card" style="min-height: 380px;">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🔍 Query & Deploy Active Staff</div>', unsafe_allow_html=True)
        search_filter_string = st.text_input("Filter via Identity Code / Worker Full Name", placeholder="Scan system tracks...")
        
        if search_filter_string:
            if not st.session_state['master_labor_pool']:
                st.info("Master database pools currently evaluate empty.")
            else:
                matches = [w for w in st.session_state['master_labor_pool'] if search_filter_string.lower() in w['Name'].lower() or search_filter_string in w['Employee ID']]
                if matches:
                    for entry_item in matches:
                        if st.button(f"⚡ Deploy Unit: {entry_item['Name']} ({entry_item['Employee ID']})", key=f"dpl_{entry_item['Employee ID']}", use_container_width=True):
                            if any(q['Employee ID'] == entry_item['Employee ID'] for q in st.session_state['daily_active_roster']):
                                st.error("Target employee unit already active inside staging queue.")
                            else:
                                st.session_state['daily_active_roster'].append({
                                    "Employee ID": entry_item["Employee ID"], "Name": entry_item["Name"],
                                    "Company": entry_item["Company"], "Remarks": ""
                                })
                                st.success(f"Staged {entry_item['Name']}.")
                                st.rerun()
                else:
                    st.warning("No structural personnel records correlate with query filters.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_w_r:
        st.markdown('<div class="dashboard-card" style="min-height: 380px;">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">➕ Direct Profile Creation Node</div>', unsafe_allow_html=True)
        sub_id = st.text_input("Assign Unique Employee ID")
        sub_name = st.text_input("Legal Individual Full Name")
        sub_comp = st.text_input("Corporate Vendor Affiliation / Company Entity")
        
        if st.button("💾 Commit Profile Creation", type="secondary", use_container_width=True):
            if sub_id and sub_name and sub_comp:
                if any(k['Employee ID'] == sub_id for k in st.session_state['master_labor_pool']):
                    st.error("Data tracking conflict. Assigned Employee ID already active.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": sub_id, "Name": sub_name, "Company": sub_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": sub_id, "Name": sub_name, "Company": sub_comp, "Remarks": ""})
                    st.success("New operational vector built successfully.")
                    st.rerun()
            else:
                st.warning("Execution paused. All data parameters are mandatory.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Active Staging Queue Wrapper
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 Staged Attendance Matrix Deployment Queue</div>', unsafe_allow_html=True)
    if not st.session_state['daily_active_roster']:
        st.info("Staging vectors hold zero deployment entries presently.")
    else:
        index_drop_target = None
        for i_idx, i_worker in enumerate(st.session_state['daily_active_roster']):
            ln1, ln2, ln3, ln4, ln5 = st.columns([1.5, 2, 2, 3, 1])
            ln1.write(f"**ID:** {i_worker['Employee ID']}")
            ln2.write(f"**Name:** {i_worker['Name']}")
            ln3.write(f"**Company:** {i_worker['Company']}")
            st.session_state['daily_active_roster'][i_idx]["Remarks"] = ln4.text_input("Notes / Site Remarks", key=f"m_rem_{i_idx}", value=i_worker["Remarks"], label_visibility="collapsed")
            if ln5.button("❌ Drop", key=f"m_drop_{i_idx}", use_container_width=True):
                index_drop_target = i_idx
                
        if index_drop_target is not None:
            st.session_state['daily_active_roster'].pop(index_drop_target)
            st.rerun()
            
        st.markdown('<br>', unsafe_allow_html=True)
        if st.button("🔒 Finalize & Securely Archive Daily Attendance Sheets", type="primary", use_container_width=True):
            for log_row in st.session_state['daily_active_roster']:
                st.session_state['attendance_database'].append({
                    "Date": str(target_date_context), "Employee ID": log_row["Employee ID"],
                    "Name": log_row["Name"], "Company": log_row["Company"],
                    "Status": "Present", "Remarks": log_row["Remarks"]
                })
            st.success("Log sheets archived securely inside core repositories.")
            st.session_state['daily_active_roster'] = []
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 3. FINANCIAL TAX REGISTRY
with t_invoices:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧾 Omani Tax Invoice Archive Registry</div>', unsafe_allow_html=True)
    
    iv_c1, iv_c2 = st.columns(2, gap="large")
    with iv_c1:
        f_inv_date = st.date_input("Document Legal Date of Issue", datetime.now(), key="f_inv_date_cal")
        f_inv_num = st.text_input("Document Serial Number Focus (Invoice No.)", placeholder="e.g. A204306")
    with iv_c2:
        f_inv_total = st.number_input("Invoice Total Gross Financial Valuation (OMR)", min_value=0.000, step=0.001, format="%.3f")
        f_inv_vat = st.number_input("Calculated Tax Value Component (5% VAT OMR)", min_value=0.000, step=0.001, format="%.3f")
        
    st.markdown('<br>', unsafe_allow_html=True)
    if st.button("🔒 Archive Transaction Metadata Into Secure Ledgers", type="primary", use_container_width=True):
        if f_inv_num and f_inv_total > 0:
            st.session_state['invoice_database'].append({
                "Date": str(f_inv_date), "Invoice Number": f_inv_num,
                "Total Amount": f"{f_inv_total:.3f}", "VAT Amount": f"{f_inv_vat:.3f}",
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"Commercial purchase transaction line item [{f_inv_num}] logged successfully.")
            st.rerun()
        else:
            st.error("Input validation exception. Please verify financial data parameters.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 Consolidated System Sales & Purchase Vault</div>', unsafe_allow_html=True)
    if st.session_state['invoice_database']:
        st.dataframe(pd.DataFrame(st.session_state['invoice_database']), use_container_width=True)
    else:
        st.info("System ledger arrays hold zero commercial transaction logs currently.")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. DATA EXPORTS & ANALYSIS
with t_reporting:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Dynamic Chronological Sorting Filters</div>', unsafe_allow_html=True)
    sorting_scope = st.radio("Specify Analytical Report Target Scope Focus:", ["View Complete History Logs", "Filter Target Monthly Matrix View"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col_out_l, col_out_r = st.columns(2, gap="large")
    
    with col_out_l:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📋 Workforce Analytics Output</div>', unsafe_allow_html=True)
        if st.session_state['attendance_database']:
            df_att_master = pd.DataFrame(st.session_state['attendance_database'])
            st.dataframe(df_att_master, use_container_width=True)
            
            bin_excel_workforce = generate_excel_stream(df_att_master)
            st.download_button(label="📥 Download Workforce Sheet (.xlsx)", data=bin_excel_workforce, file_name="Workforce_Report.xlsx", mime="application/vnd.ms-excel", use_container_width=True)
        else:
            st.info("Workforce metrics database evaluated completely clean.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_out_r:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🧾 Financial Bookkeeping Ledger Output</div>', unsafe_allow_html=True)
        if st.session_state['invoice_database']:
            df_inv_master = pd.DataFrame(st.session_state['invoice_database'])
            st.dataframe(df_inv_master, use_container_width=True)
            
            bin_excel_financial = generate_excel_stream(df_inv_master)
            st.download_button(label="📥 Download Financial Ledger (.xlsx)", data=bin_excel_financial, file_name="Financial_Ledger.xlsx", mime="application/vnd.ms-excel", use_container_width=True)
        else:
            st.info("Commercial books contain zero chronological transactions.")
        st.markdown('</div>', unsafe_allow_html=True)