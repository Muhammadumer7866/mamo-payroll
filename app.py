import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os

# ====================== MAIN WINDOW ======================
root = tk.Tk()
root.title("AL RABHAN TRADING - Management System")
root.geometry("1200x700")
root.configure(bg="#0f172a")

# Logo Text (Agar real logo file hai to uncomment kar sakte hain)
try:
    root.iconbitmap("logo.ico")  # Optional
except:
    pass

# ====================== GLOBAL DATA ======================
labor_data = pd.DataFrame(columns=['Date', 'Employee_ID', 'Name', 'Trade', 'Start_Time', 'End_Time'])
invoice_data = pd.DataFrame(columns=['Invoice_No', 'Date', 'Supplier', 'Taxable_Amount', 'VAT_5', 'Total_Amount'])

# ====================== LOGIN WINDOW ======================
def login():
    login_win = tk.Toplevel(root)
    login_win.title("Login - AL RABHAN TRADING")
    login_win.geometry("400x300")
    login_win.configure(bg="#0f172a")

    tk.Label(login_win, text="AL RABHAN TRADING", font=("Arial", 16, "bold"), fg="#D4AF37", bg="#0f172a").pack(pady=20)
    tk.Label(login_win, text="Username", fg="white", bg="#0f172a").pack()
    user_entry = tk.Entry(login_win, width=30)
    user_entry.pack(pady=5)
    user_entry.insert(0, "admin")

    tk.Label(login_win, text="Password", fg="white", bg="#0f172a").pack()
    pass_entry = tk.Entry(login_win, width=30, show="*")
    pass_entry.pack(pady=5)
    pass_entry.insert(0, "1234")

    def check_login():
        if user_entry.get() == "admin" and pass_entry.get() == "1234":
            login_win.destroy()
            main_app()
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

    tk.Button(login_win, text="LOGIN", command=check_login, bg="#D4AF37", fg="black", font=("Arial", 10, "bold")).pack(pady=20)

# ====================== MAIN APPLICATION ======================
def main_app():
    # Clear root window
    for widget in root.winfo_children():
        widget.destroy()

    # Header
    header = tk.Label(root, text="AL RABHAN TRADING", font=("Arial", 24, "bold"), fg="#D4AF37", bg="#0f172a")
    header.pack(pady=10)
    tk.Label(root, text="Construction | Quality | Trust", font=("Arial", 12), fg="white", bg="#0f172a").pack()

    # Notebook (Tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # ==================== TAB 1: LABOR ATTENDANCE ====================
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="👷 Labor Attendance")

    # Add Labor Form
    tk.Label(tab1, text="Add New Labor Entry", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

    tk.Label(tab1, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    id_entry = tk.Entry(tab1, width=20)
    id_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(tab1, text="Name:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(tab1, width=25)
    name_entry.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(tab1, text="Trade:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    trade_combo = ttk.Combobox(tab1, values=["Mason", "Carpenter", "Electrician", "Plumber", "Helper", "Supervisor", "Welder"], width=18)
    trade_combo.grid(row=2, column=1, padx=5, pady=5)
    trade_combo.set("Helper")

    tk.Label(tab1, text="Start Time:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
    start_entry = tk.Entry(tab1, width=20)
    start_entry.grid(row=2, column=3, padx=5, pady=5)
    start_entry.insert(0, datetime.now().strftime("%H:%M"))

    def add_labor():
        global labor_data
        if name_entry.get() and id_entry.get():
            new_row = {
                'Date': datetime.now().strftime("%d/%m/%Y"),
                'Employee_ID': id_entry.get(),
                'Name': name_entry.get(),
                'Trade': trade_combo.get(),
                'Start_Time': start_entry.get(),
                'End_Time': "17:00"
            }
            labor_data = pd.concat([labor_data, pd.DataFrame([new_row])], ignore_index=True)
            messagebox.showinfo("Success", "Labor Entry Added!")
            refresh_labor_table()
        else:
            messagebox.showwarning("Warning", "Name and ID are required!")

    tk.Button(tab1, text="Save Attendance", command=add_labor, bg="#D4AF37", fg="black").grid(row=3, column=1, pady=10)

    # Labor Table
    tree_labor = ttk.Treeview(tab1, columns=('Date','ID','Name','Trade','Start','End'), show='headings')
    for col in tree_labor['columns']:
        tree_labor.heading(col, text=col)
        tree_labor.column(col, width=120)
    tree_labor.grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

    def refresh_labor_table():
        for item in tree_labor.get_children():
            tree_labor.delete(item)
        for _, row in labor_data.iterrows():
            tree_labor.insert("", "end", values=list(row))

    # ==================== TAB 2: INVOICES ====================
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="📄 Invoices")

    # Similar form for Invoice...
    tk.Label(tab2, text="New Invoice", font=("Arial", 14, "bold")).pack(pady=10)

    # (Shortened for space - you can expand it)
    tk.Button(tab2, text="Add New Invoice", command=lambda: messagebox.showinfo("Info", "Invoice Section Under Development\nUse Streamlit version for full features")).pack(pady=20)

    # ==================== TAB 3: REPORTS ====================
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="📊 Reports")

    tk.Button(tab3, text="Export Labor to Excel", command=lambda: labor_data.to_excel("labor_report.xlsx", index=False) or messagebox.showinfo("Done", "Labor Report Saved!")).pack(pady=10)
    tk.Button(tab3, text="Export Invoices to Excel", command=lambda: invoice_data.to_excel("invoice_report.xlsx", index=False) or messagebox.showinfo("Done", "Invoice Report Saved!")).pack(pady=10)

    tk.Label(tab3, text="More features (PDF/Word) coming soon...", fg="yellow").pack(pady=20)

# ===================== START APP =====================
login()
root.mainloop()