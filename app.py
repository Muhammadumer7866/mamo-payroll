import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="Al Rabhan Trading", layout="wide", initial_sidebar_state="collapsed")

# --- INITIAL COLD SYSTEM STATES ---
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

# --- GATEWAY ENTRY VALIDATION ---
if not st.session_state['logged_in']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 2 Clear Structural Columns 
    col_left, col_right = st.columns([1, 1.2], gap="large")
    
    with col_left:
        st.title("🏗️ AL RABHAN TRADING")
        st.caption("SULTANATE OF OMAN • ENTERPRISE LOGISTICS CONTROL")
        st.divider()
        
        st.subheader("Welcome Back")
        st.write("Please authenticate administrative level keys to open the operations panel.")
        
        gate_id = st.text_input("Corporate ID / Email Address", placeholder="e.g. admin@construction.om")
        gate_key = st.text_input("Security Access Key", type="password", placeholder="••••••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Log In to System", type="primary", use_container_width=True):
            if gate_id == "admin@construction.om" and gate_key == "Oman#Secure2026":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Access Refused. Security parameters failed evaluation.")
                
    with col_right:
        # Zero HTML Error-Prone Code Layer. Standardized UI Components Container.
        with st.container(border=True):
            st.subheader("Oman Enterprise Infrastructure")
            st.info("🔒 Secure Multi-Tenant Data Core Node Activated.")
            
            st.markdown("""
            ### Effortlessly manage your workforce and corporate financials.
            Consolidated cloud tracking console custom engineered for real-time field operations, active shift logs control, and Omani Tax Invoice registry archiving.
            """)
            
            st.divider()
            st.markdown("#### SYSTEM INTEGRITY NODE")
            st.write("Automated analytical report structuring engine compiles binary Excel ledgers instantaneously for internal validation.")
            st.caption("CONSTRUCTION | QUALITY | TRUST")

    st.stop()

# --- MAIN SYSTEM AFTER LOGIN ---
st.success("Access Granted. Operations Node Active.")
st.title("AL RABHAN TRADING OPERATIONS SYSTEM")
st.caption("Sultanate of Oman • Enterprise Control Node")

# INTERFACE DASHBOARD LOGS
t_overview, t_attendance, t_invoices, t_reporting = st.tabs([
    "🏠 Corporate Overview", 
    "📝 Daily Attendance Matrix", 
    "🧾 Tax Invoices Registry", 
    "📊 Chronological Reports Export"
])

def generate_excel_stream(target_df):
    mem_buffer = io.BytesIO()
    with pd.ExcelWriter(mem_buffer, engine='xlsxwriter') as b_writer:
        target_df.to_excel(b_writer, index=False, sheet_name='Operations_Export')
    return mem_buffer.getvalue()

# 1. OVERVIEW NODE
with t_overview:
    st.markdown("### Command Operations Matrix")
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
        st.markdown("#### 🔍 Query Master Workforce Pools")
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
        st.markdown("#### ➕ First-Time Individual Registration Flow")
        sub_id = st.text_input("Assign Unique Employee ID")
        sub_name = st.text_input("Legal Individual Full Name")
        sub_comp = st.text_input("Corporate Vendor Affiliation / Company Entity")
        
        if st.button("Commit Profile Creation", use_container_width=True):
            if sub_id and sub_name and sub_comp:
                if any(k['Employee ID'] == sub_id for k in st.session_state['master_labor_pool']):
                    st.error("Data tracking conflict ID already assigned.")
                else:
                    st.session_state['master_labor_pool'].append({"Employee ID": sub_id, "Name": sub_name, "Company": sub_comp})
                    st.session_state['daily_active_roster'].append({"Employee ID": sub_id, "Name": sub_name, "Company": sub_comp, "Remarks": ""})
                    st.success("New operational vector built successfully.")
                    st.rerun()

    st.markdown("### 📋 Staged Attendance Matrix Deployment Queue")
    if st.session_state['daily_active_roster']:
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
                "Date": str(f_inv_date), "Invoice Number": f_inv_num,
                "Total Amount": f"{f_inv_total:.3f}", "VAT Amount": f"{f_inv_vat:.3f}"
            })
            st.success(f"Transaction [{f_inv_num}] logged.")
            st.rerun()
    
    if st.session_state['invoice_database']:
        st.dataframe(pd.DataFrame(st.session_state['invoice_database']), use_container_width=True)

# 4. DATA EXPORTS
with t_reporting:
    st.subheader("Reports Export Panel")
    sorting_scope = st.radio("Chronology Scope Focus:", ["View Complete History Logs", "Filter Target Monthly Matrix View"], horizontal=True)
    
    if st.session_state['attendance_database']:
        df_att_master = pd.DataFrame(st.session_state['attendance_database'])
        st.dataframe(df_att_master, use_container_width=True)
        bin_excel_workforce = generate_excel_stream(df_att_master)
        st.download_button(label="📥 Download Workforce Summary (.xlsx)", data=bin_excel_workforce, file_name="Workforce_Report.xlsx", mime="application/vnd.ms-excel")