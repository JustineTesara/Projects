import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

con = sqlite3.connect("support.db")
cursor = con.cursor()


def submit_ticket():
    name = entry_name.get()
    issue = entry_issue.get()
    category = combo_category.get()

    if not name or not issue or not category:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    cursor.execute("INSERT INTO tickets (name, issue, category, status) VALUES (?, ?, ?, ?)",
                   (name, issue, category, "Pending"))
    con.commit()
    con.close()

    messagebox.showinfo("Success", "Ticket Submitted Successfully!")
    entry_name.delete(0, tk.END)
    entry_issue.delete(0, tk.END)
    combo_category.set("")


def logout():
    root.destroy()
    import login


# UI
root = tk.Tk()
root.title("Submit IT Support Ticket")
root.geometry("400x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill='both', expand=True)

tk.Label(frame, text="Name:").grid(row=0, column=0, sticky='w')
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Issue:").grid(row=1, column=0, sticky='w')
entry_issue = tk.Entry(frame, width=30)
entry_issue.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Category:").grid(row=2, column=0, sticky='w')
combo_category = ttk.Combobox(frame, values=[
                              "Hardware", "Software", "Network", "Other"], state="readonly", width=27)
combo_category.grid(row=2, column=1, pady=5)

tk.Button(frame, text="Submit Ticket", command=submit_ticket).grid(
    row=3, column=1, pady=15)
tk.Button(frame, text="Logout", command=logout).grid(row=4, column=1)

root.mainloop()
