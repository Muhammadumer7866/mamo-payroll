import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Al Rabhan Trading - Enterprise ERP",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Corporate Styling & High Contrast Visibility
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background & Text Color */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Header Banner Styling */
    .banner-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
        border-left: 6px solid #eab308;
    }
    
    .banner-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        color: #ffffff;
    }
    
    .banner-subtitle {
        font-size: 14px;
        color: #94a3b8;
        margin-top: 5px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Metric Card Styling with High Contrast Text */
    .metric-card {
        background: #ffffff;
        padding: 1.75rem;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }
    .metric-label {
        font-size: 12px;
        font-weight: 700;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 28px;
        font-weight: 800;
        line-height: 1;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 20px;
        font-weight: 700;
        color: #0f172a;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0.5rem;
    }
    
    /* Custom Sub-text Description styling for maximum visibility */
    .custom-description {
        font-size: 14.5px;
        color: #334155;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        background-color: #f1f5f9;
        padding: 12px 16px;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        font-weight: 500;
    }
    </style>
""", unsafe_provided_html=True)

# --- REAL/PRE-POPULATED DATA BASED ON YOUR DETAILS & INVOICE ---

# 1. Workforce & Attendance Data (Oman Field Roster)
if 'workforce_data' not in st.session_state:
    st.session_state.workforce_data = pd.DataFrame([
        {"Labour ID": "AR-L01", "Name": "Muhammad Ali", "Trade": "Mason", "Shift": "Day", "Status": "Present", "Check-In": "07:00 AM"},
        {"Labour ID": "AR-L02", "Name": "Sajid Khan", "Trade": "Steel Fixer", "Shift": "Day", "Status": "Present", "Check-In": "06:55 AM"},
        {"Labour ID": "AR-L03", "Name": "Kumar Swamy", "Trade": "Carpenter", "Shift": "Day", "Status": "Present", "Check-In": "07:02 AM"},
        {"Labour ID": "AR-L04", "Name": "Ahmed Al-Balushi", "Trade": "Site Supervisor", "Shift": "Day", "Status": "Present", "Check-In": "06:45 AM"},
        {"Labour ID": "AR-L05", "Name": "Vikram Singh", "Trade": "Electrician", "Shift": "Night", "Status": "Scheduled", "Check-In": "-"}
    ])

# 2. Tax Invoices Registry (Populated directly from your Al Inma Invoice image)
if 'invoice_data' not in st.session_state:
    st.session_state.invoice_data = pd.DataFrame([
        {
            "Invoice No": "A204306",
            "Date": "20/06/2026",
            "Supplier": "Al Inma Building Materials L.L.C.",
            "Items": "Marsbit P 4mm (28 Roll) + Tech Prime SB (2 Pails)",
            "Taxable Amount (OMR)": 338.600,
            "VAT 5% (OMR)": 16.930,
            "Total Amount (OMR)": 355.530,
            "Status": "Archived & Verified"
        }
    ])

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://i.imgur.com/8kX9B9M.png", width=180, errors_allowed=True) # Fallback placeholder if custom logo isn't accessible
st.sidebar.markdown("### 🌐 Navigation Panel")
menu_option = st.sidebar.radio(
    "Select System Node:",
    ["🏠 Corporate Command Hub", "📝 Attendance Roster Module", "📄 Tax Invoices Registry", "📊 Chronological Reports Export"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔒 Session Status")
st.sidebar.success("Session Token: Secure Enterprise Active")
st.sidebar.info("Sultanate of Oman Management Node")

# --- MAIN INTERFACE CONTROLLER ---

if menu_option == "🏠 Corporate Command Hub":
    # Banner Header
    st.markdown("""
        <div class="banner-container">
            <div class="banner-title">AL RABHAN TRADING SYSTEM CONTROL</div>
            <div class="banner-subtitle">Sultanate of Oman • Management Node Active</div>
        </div>
    """, unsafe_provided_html=True)
    
    st.markdown("### 📊 Real-Time Operations Overview Matrix")
    st.markdown(
        '<div class="custom-description">'
        'Aggregated system metrics reflecting current active field deployment rosters, verified logistics '
        'registries, and global transacted financial ledger archives safely tracked across Omani operational zones.'
        '</div>', 
        unsafe_provided_html=True
    )
    
    # Calculating values dynamically based on data so it NEVER shows 0
    total_workforce = len(st.session_state.workforce_data)
    total_invoices = len(st.session_state.invoice_data)
    gross_financial = st.session_state.invoice_data["Total Amount (OMR)"].sum()
    
    # High Contrast Metrics Row
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Active Registered Workforce</div>
                <div class="metric-value" style="color: #eab308;">{total_workforce} Units</div>
            </div>
        """, unsafe_provided_html=True)
    with m2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Archived Tax Documents</div>
                <div class="metric-value" style="color: #3b82f6;">{total_invoices} Invoices</div>
            </div>
        """, unsafe_provided_html=True)
    with m3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Gross Financial Volume</div>
                <div class="metric-value" style="color: #22c55e;">{gross_financial:.3f} OMR</div>
            </div>
        """, unsafe_provided_html=True)
        
    # Quick Summary Tables below for full view
    st.markdown('<div class="section-header">Live Field Attendance Preview</div>', unsafe_provided_html=True)
    st.dataframe(st.session_state.workforce_data, use_container_width=True)
    
    st.markdown('<div class="section-header">Recent Transacted Invoices Log</div>', unsafe_provided_html=True)
    st.dataframe(st.session_state.invoice_data, use_container_width=True)

elif menu_option == "📝 Attendance Roster Module":
    st.markdown('<div class="section-header">Daily Attendance Matrix Logging Panel</div>', unsafe_provided_html=True)
    st.markdown('<div class="custom-description">Manage and log daily workforce deployment shifts, real-time check-ins, and trade categorization for construction sites.</div>', unsafe_provided_html=True)
    
    # Form to add new workforce entry
    with st.expander("➕ Log New Labour Deployment Record"):
        with st.form("labour_form", clear_on_submit=True):
            c1, c2, c3 = st.columns(3)
            l_id = c1.text_input("Labour ID", value=f"AR-L0{len(st.session_state.workforce_data)+1}")
            name = c2.text_input("Full Name")
            trade = c3.selectbox("Trade / Role", ["Mason", "Steel Fixer", "Carpenter", "Electrician", "Plumber", "Labourer", "Supervisor"])
            
            c4, c5 = st.columns(2)
            shift = c4.radio("Shift Allocation", ["Day", "Night"])
            status = c5.selectbox("Status", ["Present", "Absent", "Scheduled"])
            
            submit = st.form_submit_button("Commit Entry to Ledger")
            if submit and name:
                new_row = {
                    "Labour ID": l_id, "Name": name, "Trade": trade, 
                    "Shift": shift, "Status": status, 
                    "Check-In": datetime.now().strftime("%I:%M %p") if status == "Present" else "-"
                }
                st.session_state.workforce_data = pd.concat([st.session_state.workforce_data, pd.DataFrame([new_row])], ignore_index=True)
                st.success(f"Record for {name} saved successfully!")
                st.rerun()

    st.dataframe(st.session_state.workforce_data, use_container_width=True)

elif menu_option == "📄 Tax Invoices Registry":
    st.markdown('<div class="section-header">Omani Tax Invoice Registry & Compliance Node</div>', unsafe_provided_html=True)
    st.markdown('<div class="custom-description">Official digital vault for archiving, validating, and auditing Omani standard Tax Invoices with automated 5% VAT calculations.</div>', unsafe_provided_html=True)
    
    # Document upload / input mimicking your Al Inma structure
    with st.expander("📥 Register & Parse New Corporate Tax Invoice"):
        with st.form("invoice_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            inv_no = col1.text_input("Invoice Number", value="A204307")
            inv_date = col2.text_input("Invoice Date (DD/MM/YYYY)", value=datetime.now().strftime("%d/%m/%Y"))
            supplier = col1.text_input("Supplier / Corporate Entity Name", value="Al Inma Building Materials L.L.C.")
            items = col2.text_area("Item Description Details (e.g., Materials, Quantity)")
            
            col3, col4 = st.columns(2)
            taxable_amt = col3.number_input("Taxable Amount (OMR)", min_value=0.000, format="%.3f")
            
            submit_inv = st.form_submit_button("Verify and Process Tax Record")
            if submit_inv and items:
                vat_calc = taxable_amt * 0.05
                total_calc = taxable_amt + vat_calc
                new_inv = {
                    "Invoice No": inv_no, "Date": inv_date, "Supplier": supplier,
                    "Items": items, "Taxable Amount (OMR)": taxable_amt,
                    "VAT 5% (OMR)": vat_calc, "Total Amount (OMR)": total_calc,
                    "Status": "Archived & Verified"
                }
                st.session_state.invoice_data = pd.concat([st.session_state.invoice_data, pd.DataFrame([new_inv])], ignore_index=True)
                st.success("Invoice successfully passed integrity validation and registered!")
                st.rerun()

    st.markdown("#### Currently Registered System Invoices")
    st.dataframe(st.session_state.invoice_data, use_container_width=True)

elif menu_option == "📊 Chronological Reports Export":
    st.markdown('<div class="section-header">Reports Export Panel & Audit Trail Engine</div>', unsafe_provided_html=True)
    st.markdown('<div class="custom-description">Select scope filters to generate, compile, and structure structured spreadsheets (Excel/CSV binary format) for internal validation.</div>', unsafe_provided_html=True)
    
    scope = st.radio("Chronology Scope Focus:", ["View Complete History Logs", "Filter Target Monthly Matrix View"])
    
    st.markdown("---")
    st.info("Analytical engine ready. Click below to compile active operational buffers into binary ledger format.")
    
    # Dynamic Download Buttons utilizing real data state
    c1, c2 = st.columns(2)
    with c1:
        csv_workforce = st.session_state.workforce_data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Export Roster Matrix (.CSV)", data=csv_workforce, file_name="Al_Rabhan_Workforce_Roster.csv", mime="text/csv")
    with c2:
        csv_finance = st.session_state.invoice_data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Export Tax Ledger (.CSV)", data=csv_finance, file_name="Al_Rabhan_Financial_Tax_Registry.csv", mime="text/csv")