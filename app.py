import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- CORE SYSTEM CONFIGURATION ---
st.set_page_config(page_title="Al Rabhan Trading - Corporate Portal", layout="wide", initial_sidebar_state="collapsed")

# --- CLEAN EXECUTIVE CSS ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Base Core */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Style for the Left Form Side */
    .left-side-container {
        padding: 10px 20px;
    }

    /* Input Fields Styling */
    div.stTextInput > div > div > input {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        color: #0f172a !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
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

# --- SECURE GATEWAY HUB ---
if not st.session_state['logged_in']:
    st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
    
    # Robust 2-Column native layout
    col_left, col_right = st.columns([1.1, 1], gap="large")
    
    with col_left:
        st.markdown('<div class="left-side-container">', unsafe_allow_html=True)
        # Vector Graphic Logo Structure Layout
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
        
        # Interface Inputs
        gate_id = st.text_input("Corporate ID / Email Address", placeholder="e.g. admin@construction.om")
        gate_key = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
        
        st.markdown('<div style="margin-top: 20px;">', unsafe_allow_html=True)
        if st.button("Log In to System", type="primary", use_container_width=True):
            if gate_id == "admin@construction.om" and gate_key == "Oman#Secure2026":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Access Refused. Security parameters failed evaluation.")
        st.markdown('</div></div>', unsafe_allow_html=True)
        
    with col_right:
        # Fully Unified Single Block Template for entire right card layout
        st.markdown("""
            <div style="background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); padding: 40px; border-radius: 20px; color: #ffffff; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); margin-top: 15px; min-height: 500px;">
                <div style="background: rgba(234, 179, 8, 0.15); border: 1px solid rgba(234, 179, 8, 0.3); color: #fef08a; padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: inline-block; margin-bottom: 25px; width: fit-content;">
                    Oman Enterprise Infrastructure
                </div>
                <div style="font-size: 36px; font-weight: 800; line-height: 1.2; color: #ffffff; margin-bottom: 5px;">
                    Effortlessly manage
                </div>
                <div style="font-size: 36px; font-weight: 800; line-height: 1.2; color: #ffffff; margin-bottom: 5px;">
                    your workforce and
                </div>
                <div style="font-size: 36px; font-weight: 800; line-height: 1.2; color: #eab308; margin-bottom: 20px;">
                    corporate financials.
                </div>
                <div style="width: 60px; height: 4px; background: linear-gradient(90deg, #eab308 0%, #ca8a04 100%); border-radius: 2px; margin-bottom: 25px;"></div>
                
                <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 30px; max-width: 460px;">
                    Consolidated cloud tracking console custom engineered for real-time field operations, active shift logs control, and Omani Tax Invoice registry archiving.
                </p>
                
                <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); padding: 18px; border-radius: 12px; max-width: 460px;">
                    <span style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: #eab308; letter-spacing: 1px;">CONSTRUCTION | QUALITY | TRUST</span>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #94a3b8; line-height: 1.5;">
                        Automated analytical report structuring engine compiles binary Excel ledgers instantaneously for internal validation.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- MAIN INDUSTRIAL SYSTEM VIEWPORT ---
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

def generate_excel_stream(target_df):
    mem_buffer = io.BytesIO()
    with pd.ExcelWriter(mem_buffer, engine='xlsxwriter') as b_writer:
        target_df.to_excel(b_writer, index=False, sheet_name='Operations_Export')
    return mem_buffer.getvalue()

# INTERFACE DASHBOARD LOGS
t_overview, t_attendance, t_invoices, t_reporting = st.tabs([
    "🏠 Corporate Overview", 
    "📝 Daily Attendance Matrix", 
    "🧾 Tax Invoices Registry", 
    "📊 Chronological Reports Export"
])

# 1. OVERVIEW NODE
with t_overview:
    st.markdown("<h3 style='color: #0f172a; font-weight: 800; margin-top:10px;'>Command Operations Matrix</h3>", unsafe_allow_html=True)
    st.write("Real-time aggregated corporate performance indicators tracking cross-border human capital alongside archived transactions.")
    
    st1, st2, st3 = st.columns(3)
    with st1:
        st.metric(label="Master Active Workforce", value=f"{len(st.session_state['master_labor_pool'])} Units")
    with st2:
        st.metric(label="Archived Invoices Volume", value=f"{len(st.session_state['invoice_database'])} Records")
    with st3:
        gross_sum_value = sum(float(i['Total Amount']) for i in st.session_state['invoice_database']) if st.session_state['invoice_database'] else 0.0
        st.metric(label="Gross Value Transacted (OMR)", value=f"{gross_sum_value:.3f} OMR")

# 2. LABOUR ATTENDANCE MANAGEMENT
with t_attendance:
    st.subheader("Field Deployment Roster Logs")
    target_date_context = st.date_input("Target Calendar Date Focus Frame", datetime.now(), key="work_date_context")
    
    col_w_l, col_w_r = st.columns(2, gap="large")
    with col_w_l:
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

    with col_w_r:
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

    st.markdown("### 📋 Staged Attendance Matrix Deployment Queue")
    if not st.session_state['daily_active_roster']:
        st.info("Staging vectors hold zero deployment entries presently.")
    else:
        index_drop_target = None
        for i_idx, i_worker in enumerate(st.session_state['daily_active_roster']):
            ln1, ln2, ln3, ln4, ln5 = st.columns([1.5, 2, 2, 3, 1])
            ln1.write(f"**ID:** {i_worker['Employee ID']}")
            ln2.write(f"**Name:** {i_worker['Name']}")
            ln3.write(f"**Company:** {i_worker['Company']}")
            st.session_state['daily_active_roster'][i_idx]["Remarks"] = ln4.text_input("Notes", key=f"m_rem_{i_idx}", value=i_worker["Remarks"], label_visibility="collapsed")
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

# 3. FINANCIAL TAX REGISTRY
with t_invoices:
    st.subheader("Commercial Transaction & Invoice Audit Controls")
    
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
            st.success(f"Commercial purchase transaction line item [{f_inv_num}] logged successfully.")
            st.rerun()
        else:
            st.error("Input validation exception. Please provide valid transaction parameters.")
    
    st.markdown("### 📋 Logged Commercial Invoices")
    if st.session_state['invoice_database']:
        st.dataframe(pd.DataFrame(st.session_state['invoice_database']), use_container_width=True)
    else:
        st.info("System ledger arrays hold zero commercial transaction files currently.")

# 4. DATA EXPORTS & REPORT COMPILES
with t_reporting:
    st.subheader("Chronological Filter Systems & Binary Ledger Compilation Panels")
    
    sorting_scope = st.radio("Specify Analytical Report Target Chronology Scope Focus:", ["View Complete History Logs", "Filter Target Monthly Matrix View", "Filter Target Yearly Matrix View"], horizontal=True)
    
    var_m = datetime.now().strftime("%m")
    var_y = datetime.now().strftime("%Y")
    
    if sorting_scope == "Filter Target Monthly Matrix View":
        bx1, bx2 = st.columns(2)
        var_m = bx1.selectbox("Filter Target Month Focus Block", [f"{n:02d}" for n in range(1, 13)], index=int(datetime.now().month)-1)
        var_y = bx2.selectbox("Filter Target Year Focus Block", [str(y) for y in range(2025, 2032)], key="rep_m_yr")
    elif sorting_scope == "Filter Target Yearly Matrix View":
        var_y = st.selectbox("Filter Target Year Focus Block", [str(y) for y in range(2025, 2032)], key="rep_y_yr")

    col_out_l, col_out_r = st.columns(2, gap="large")
    
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