import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Login ----------

def login():
    if username.get() == "admin" and password.get() == "1234":
        login_frame.pack_forget()
        dashboard.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Error", "Invalid Login")

root = tk.Tk()
root.title("AL RABHAN TRADING")
root.geometry("900x600")
root.configure(bg="#111111")

# Login Frame
login_frame = tk.Frame(root, bg="#111111")
login_frame.pack(fill="both", expand=True)

tk.Label(
    login_frame,
    text="AL RABHAN TRADING",
    font=("Arial", 24, "bold"),
    fg="gold",
    bg="#111111"
).pack(pady=20)

tk.Label(
    login_frame,
    text="Building Excellence Through Quality & Trust",
    fg="white",
    bg="#111111"
).pack()

username = tk.Entry(login_frame, width=30)
username.pack(pady=10)
username.insert(0, "admin")

password = tk.Entry(login_frame, width=30, show="*")
password.pack(pady=10)
password.insert(0, "1234")

tk.Button(
    login_frame,
    text="Login",
    bg="gold",
    command=login
).pack(pady=20)

# Dashboard
dashboard = tk.Frame(root, bg="white")

title = tk.Label(
    dashboard,
    text="AL RABHAN TRADING DASHBOARD",
    font=("Arial", 20, "bold"),
    bg="white"
)
title.pack(pady=10)

# Labour Section
labour_frame = tk.LabelFrame(
    dashboard,
    text="Labour Management",
    padx=10,
    pady=10
)
labour_frame.pack(fill="x", padx=20, pady=10)

tk.Label(labour_frame, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(labour_frame)
name_entry.grid(row=0, column=1)

tk.Label(labour_frame, text="Trade").grid(row=1, column=0)
trade_entry = tk.Entry(labour_frame)
trade_entry.grid(row=1, column=1)

tree = ttk.Treeview(
    labour_frame,
    columns=("Name", "Trade"),
    show="headings"
)

tree.heading("Name", text="Name")
tree.heading("Trade", text="Trade")
tree.grid(row=3, column=0, columnspan=2)

def add_labour():
    tree.insert(
        "",
        "end",
        values=(
            name_entry.get(),
            trade_entry.get()
        )
    )

tk.Button(
    labour_frame,
    text="Add Labour",
    command=add_labour
).grid(row=2, column=0, columnspan=2)

# Invoice Section
invoice_frame = tk.LabelFrame(
    dashboard,
    text="Invoice Management",
    padx=10,
    pady=10
)
invoice_frame.pack(fill="x", padx=20, pady=10)

tk.Label(invoice_frame, text="Invoice No").grid(row=0, column=0)
invoice_entry = tk.Entry(invoice_frame)
invoice_entry.grid(row=0, column=1)

tk.Label(invoice_frame, text="Amount").grid(row=1, column=0)
amount_entry = tk.Entry(invoice_frame)
amount_entry.grid(row=1, column=1)

invoice_tree = ttk.Treeview(
    invoice_frame,
    columns=("Invoice", "Amount"),
    show="headings"
)

invoice_tree.heading("Invoice", text="Invoice")
invoice_tree.heading("Amount", text="Amount")
invoice_tree.grid(row=3, column=0, columnspan=2)

def add_invoice():
    invoice_tree.insert(
        "",
        "end",
        values=(
            invoice_entry.get(),
            amount_entry.get()
        )
    )

tk.Button(
    invoice_frame,
    text="Add Invoice",
    command=add_invoice
).grid(row=2, column=0, columnspan=2)

root.mainloop()