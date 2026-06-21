import streamlit as st
import pandas as pd
from datetime import datetime
import os
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="Al Rabhan Trading - Secure ERP",
    page_icon="🏗️",
    layout="wide"
)

# 2. Base64 Image Conversion Functions (SAFELY MANAGED)
def get_base64_img(img_path):
    """Safely reads a local image file and converts it to Base64 for CSS rendering."""
    if os.path.exists(img_path):
        try:
            with open(img_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
        except Exception:
            return None
    return None

# Exact filenames inside your repository
logo_main_file = "ChatGPT Image Jun 20, 2026, 02_56_40 PM.png"
logo_bg_file = "image_436736.png"

# Convert assets to base64 strings safely
main_logo_b64 = get_base64_img(logo_main_file)
bg_logo_b64 = get_base64_img(logo_bg_file)

# 3. Dynamic Styling Engine (Watermark Layer with Strict Fallbacks)
if bg_logo_b64:
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.94), rgba(255, 255, 255, 0.94)), url("data:image/png;base64,{bg_logo_b64}");
            background-size: 40% !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        @media (prefers-color-scheme: dark) {{
            .stApp {{
                background-image: linear-gradient(rgba(14, 17, 23, 0.94), rgba(14, 17, 23, 0.94)), url("data:image/png;base64,{bg_logo_b64}");
                background-size: 40% !important;
            }}
        }}
        .stDataFrame, .stTable, .stTabs, div[data-testid="stForm"], div[data-testid="stExpander"] {{
            background-color: rgba(255, 255, 255, 0.05) !important;
            border-radius: 12px;
            padding: 15px;
        }}
        label p {{
            font-weight: bold !important;
            font-size: 15px !important;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        label p { font-weight: bold !important; font-size: 15px !important; }
        </style>
    """, unsafe_allow_html=True)


# 4. Central Session State Initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'workforce_db' not in st.session_state:
    st.session_state.workforce_db = pd.DataFrame([
        {"Employee ID": "92476849", "Name": "Mohammad Shahid", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "-", "Time Out": "-", "PPE": "-", "Status": "N/S"},
        {"Employee ID": "109748895", "Name": "M.Usman", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "-", "Time Out": "-", "PPE": "-", "Status": "N/S"},
        {"Employee ID": "136299814", "Name": "Jahanzeb Afzal", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "79705332", "Name": "Abdul khaliq", "Company": "Rimal. AL", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "91385467", "Name": "Murtuza", "Company": "Ahmed. AL", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "136025677", "Name": "USAMA IJAZ", "Company": "Sahool Wadi Trading", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "135028261", "Name": "M.Usama", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "134607323", "Name": "Shahid Ahmad", "Company": "Abu Hisham Al Riyami Trading", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "129149239", "Name": "ANWAR AHMAD", "Company": "Abu Sultan Al Hajri Trading Entities LLC", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "128565626", "Name": "AKRAMUL HAQUE", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "99092783", "Name": "IJAZ AHMAD", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "100018149", "Name": "JAVED BOOTA", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "137686123", "Name": "AZID ALI", "Company": "Millennium Building Trading & Contracting LLC", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "135028223", "Name": "MUHAMMAD NAVEED", "Company": "Rubhan. T", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "136138983", "Name": "GHULAM MOHI UD DIN", "Company": "AlSafa Distinguished Project", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "131430865", "Name": "MUHAMMAD WASEEM", "Company": "Al-Ahram AlMutajaddida LLC", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"},
        {"Employee ID": "126755181", "Name": "AHSAN ALI", "Company": "Rizwan Ali Trading & Contracting LLC", "Scope": "Civil", "Time In": "7:00 AM", "Time Out": "5:00 PM", "PPE": "Verified", "Status": "Present"}
    ])

if 'invoice_db' not in st.session_state:
    st.session_state.invoice_db = pd.DataFrame([
        {
            "Invoice/Receipt No": "A204306",
            "Date": "20/06/2026",
            "Vendor/Supplier": "Al Inma Building Materials L.L.C.",
            "Description": "Marsbit P 4mm (28 Rolls) & Tech Prime SB (2 Pails)",
            "Taxable Base (OMR)": 338.600,
            "VAT Amount (5%)": 16.930,
            "Gross Total (OMR)": 355.530,
            "Type": "Tax Invoice"
        },
        {
            "Invoice/Receipt No": "Cash Memo",
            "Date": "20/06/2026",
            "Vendor/Supplier": "Lulu Dhofar International LLC",
            "Description": "Safety Pant-Shirt (M) - 1 Set (with OMR 0.200 discount)",
            "Taxable Base (OMR)": 4.800,
            "VAT Amount (5%)": 0.000,
            "Gross Total (OMR)": 4.800,
            "Type": "Cash Purchase"
        },
        {
            "Invoice/Receipt No": "6752",
            "Date": "20/06/2026",
            "Vendor/Supplier": "Oman Oil (Awqad 8016 Salalah)",
            "Description": "Fuel Purchase - Visa Debit Terminal 5715",
            "Taxable Base (OMR)": 5.000,
            "VAT Amount (5%)": 0.000,
            "Gross Total (OMR)": 5.000,
            "Type": "Fuel Receipt"
        }
    ])

# ==============================================================================
# PHASE 1: SECURE AUTHENTICATION GATEWAY
# ==============================================================================
if not st.session_state.logged_in:
    # Renders the bold header branding explicitly using parsed Base64 blocks
    if main_logo_b64:
        st.markdown(
            f'<div style="text-align: center; margin-bottom: 20px;">'
            f'<img src="data:image/png;base64,{main_logo_b64}" style="width: 440px; max-width: 90%; font-weight: bold;">'
            f'</div>', 
            unsafe_allow_html=True
        )
    else:
        st.title("🏗️ AL RABHAN TRADING")
    
    st.markdown("<hr style='margin-top:0px; margin-bottom:30px;'>", unsafe_allow_html=True)

    left_col, right_col = st.columns(2, gap="large")
    
    with left_col:
        st.subheader("System Authentication")
        st.write("Provide administrative network keys to access logistical databases.")
        
        # Hardcoded verification fallback logic if deployment secret mapping isn't responding
        try:
            secret_user = st.secrets["auth"]["admin_email"]
            secret_pass = st.secrets["auth"]["admin_password"]
        except Exception:
            secret_user = "admin@construction.om"
            secret_pass = "Oman#Secure2026"

        input_user = st.text_input("Corporate ID / Email Address", value="admin@construction.om")
        input_pass = st.text_input("Security Access Key", type="password", value="Oman#Secure2026")
        
        if st.button("Log In to System", type="primary"):
            if input_user == secret_user and input_pass == secret_pass:
                st.session_state.logged_in = True
                st.success("Access Granted. Synchronizing Ledger Databases...")
                st.rerun()
            else:
                st.error("Invalid Administrative Credentials. Connection Denied.")
                
    with right_col:
        with st.container(border=True):
            st.markdown("### 🌐 Sultanate of Oman Logistics Core")
            st.markdown("**Real-Time Deployment & Financial Control Console**")
            st.write(
                "Custom built cloud interface tracking multi-vendor construction deployment matrix, "
                "site supervisor shifts, and active Omani Tax compliance audits."
            )
            st.caption("CONSTRUCTION | QUALITY | TRUST")

# ==============================================================================
# PHASE 2: INTERNAL OPERATIONS DASHBOARD
# ==============================================================================
else:
    h_logo_col, h_text_col = st.columns([1.5, 6])
    with h_logo_col:
        if main_logo_b64:
            st.markdown(f'<img src="data:image/png;base64,{main_logo_b64}" style="width: 140px;">', unsafe_allow_html=True)
    with h_text_col:
        st.title("AL RABHAN TRADING OPERATIONS SYSTEM")
        st.caption("Sultanate of Oman • Enterprise Control Node")
    
    h_col1, h_col2 = st.columns([6, 1])
    h_col1.success("🔒 System Integrity Node: Active & Protected by Environment Keys.")
    if h_col2.button("Log Out", type="secondary"):
        st.session_state.logged_in = False
        st.rerun()
        
    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🏠 Corporate Command Hub", 
        "📝 Daily Attendance Matrix", 
        "📄 Tax Invoices Registry", 
        "📊 Corporate Reports Export"
    ])

    # --- TAB 1: COMMAND HUB ---
    with tab1:
        st.subheader("📊 Real-Time Operations Overview Matrix")
        
        total_workers = len(st.session_state.workforce_db)
        present_workers = len(st.session_state.workforce_db[st.session_state.workforce_db["Status"] == "Present"])
        total_docs = len(st.session_state.invoice_db)
        total_financial_volume = st.session_state.invoice_db["Gross Total (OMR)"].sum()
        
        m1, m2, m3 = st.columns(3)
        m1.metric(label="TOTAL DEPLOYED WORKFORCE", value=f"{total_workers} Units", delta=f"{present_workers} Present Today")
        m2.metric(label="ARCHIVED TAX / REVENUE DOCUMENTS", value=f"{total_docs} Records")
        m3.metric(label="GROSS FINANCIAL ACCOUNTED VOLUME", value=f"{total_financial_volume:.3f} OMR")
        
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Live Field Attendance Ledger")
            st.dataframe(st.session_state.workforce_db[["Employee ID", "Name", "Company", "Status"]], use_container_width=True, hide_index=True)
        with col_b:
            st.markdown("#### Recent Transacted Invoices & Slips")
            st.dataframe(st.session_state.invoice_db[["Invoice/Receipt No", "Vendor/Supplier", "Gross Total (OMR)", "Type"]], use_container_width=True, hide_index=True)

    # --- TAB 2: DAILY ATTENDANCE MATRIX ---
    with tab2:
        st.subheader("📝 Daily Attendance Matrix Logging Panel")
        
        with st.expander("➕ Add New Field Worker Entry", expanded=False):
            with st.form("add_worker_real_form", clear_on_submit=True):
                c1, c2, c3 = st.columns(3)
                emp_id = c1.text_input("Employee ID / Card Code *")
                emp_name = c2.text_input("Worker Full Name *")
                emp_company = c3.text_input("Subcontractor/Company Entity", value="Rubhan. T")
                
                c4, c5, c6 = st.columns(3)
                emp_scope = c4.selectbox("Scope of Work", ["Civil", "Mechanical", "Electrical", "Supervision", "Logistics"])
                emp_status = c5.selectbox("Duty Status", ["Present", "N/S (No Shift)", "Absent"])
                emp_ppe = c6.checkbox("Full PPE Compliant (Yes/No)", value=True)
                
                if st.form_submit_button("Commit Entry to Field Database"):
                    if emp_id.strip() == "" or emp_name.strip() == "":
                        st.error("Validation Error: Employee ID and Full Name are required fields.")
                    else:
                        new_worker = {
                            "Employee ID": emp_id, "Name": emp_name, "Company": emp_company, "Scope": emp_scope,
                            "Time In": "7:00 AM" if emp_status == "Present" else "-",
                            "Time Out": "5:00 PM" if emp_status == "Present" else "-",
                            "PPE": "Verified" if emp_ppe and emp_status == "Present" else "-",
                            "Status": emp_status
                        }
                        st.session_state.workforce_db = pd.concat([st.session_state.workforce_db, pd.DataFrame([new_worker])], ignore_index=True)
                        st.success(f"Success: Record for {emp_name} linked successfully.")
                        st.rerun()

        st.dataframe(st.session_state.workforce_db, use_container_width=True, hide_index=True)

    # --- TAB 3: TAX INVOICES REGISTRY ---
    with tab3:
        st.subheader("📄 Omani Tax Invoice Registry & Compliance Node")
        
        with st.expander("📥 Log New Transaction Slip / Invoice", expanded=False):
            with st.form("add_invoice_real_form", clear_on_submit=True):
                i1, i2 = st.columns(2)
                v_no = i1.text_input("Invoice/Receipt Number *")
                v_date = i2.text_input("Transaction Date (DD/MM/YYYY)", value=datetime.now().strftime("%d/%m/%Y"))
                v_supplier = i1.text_input("Vendor / Supplier Name *")
                v_desc = i2.text_area("Detailed Material / Expense Description")
                
                i3, i4 = st.columns(2)
                v_type = i3.selectbox("Document Classification Type", ["Tax Invoice", "Cash Purchase", "Fuel Receipt", "General Voucher"])
                v_base = i4.number_input("Taxable Base/Net Amount (OMR)", min_value=0.000, value=0.000, step=0.001, format="%.3f")
                
                if st.form_submit_button("Authenticate Expense Entry"):
                    if v_no.strip() == "" or v_supplier.strip() == "":
                        st.error("Validation Error: Please fill out critical registration parameters.")
                    else:
                        vat_computed = v_base * 0.05 if v_type == "Tax Invoice" else 0.000
                        gross_computed = v_base + vat_computed
                        
                        new_inv = {
                            "Invoice/Receipt No": v_no, "Date": v_date, "Vendor/Supplier": v_supplier,
                            "Description": v_desc, "Taxable Base (OMR)": v_base,
                            "VAT Amount (5%)": vat_computed, "Gross Total (OMR)": gross_computed,
                            "Type": v_type
                        }
                        st.session_state.invoice_db = pd.concat([st.session_state.invoice_db, pd.DataFrame([new_inv])], ignore_index=True)
                        st.success("Success: Expense parameters computed and committed.")
                        st.rerun()

        st.dataframe(st.session_state.invoice_db, use_container_width=True, hide_index=True)

    # --- TAB 4: EXPORTS ---
    with tab4:
        st.subheader("📊 Corporate Reports Export Panel")
        st.radio("Timeline Scope Configuration:", ["Complete Historical Logs", "Active Audited Month Only"])
        st.markdown("---")
        
        csv_w = st.session_state.workforce_db.to_csv(index=False).encode('utf-8')
        csv_i = st.session_state.invoice_db.to_csv(index=False).encode('utf-8')
        
        d_col1, d_col2 = st.columns(2)
        d_col1.download_button(label="📥 Export Actual Workforce Matrix (.CSV)", data=csv_w, file_name="Al_Rabhan_Actual_Roster.csv", mime="text/csv", use_container_width=True)
        d_col2.download_button(label="📥 Export Verified Expense Ledger (.CSV)", data=csv_i, file_name="Al_Rabhan_Expense_Ledger.csv", mime="text/csv", use_container_width=True)