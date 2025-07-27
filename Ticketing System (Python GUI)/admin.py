import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def get_ticket_stats():
    con = sqlite3.connect("support.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM tickets")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tickets WHERE status='Pending'")
    pending = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tickets WHERE status='Resolved'")
    resolved = cursor.fetchone()[0]

    con.close()
    return total, pending, resolved


def update_dashboard():
    total, pending, resolved = get_ticket_stats()
    label_total.config(text=f"Total Tickets: {total}")
    label_pending.config(text=f"Total Pending: {pending}")
    label_resolved.config(text=f"Total Resolved: {resolved}")


def load_tickets(filter_status="All"):
    listbox_tickets.delete(0, tk.END)

    con = sqlite3.connect("support.db")
    cursor = con.cursor()
    if filter_status == "All":

        cursor.execute("SELECT id, name, issue, category, status FROM tickets")
    else:
        cursor.execute(
            "SELECT id, name, issue, category, status FROM tickets WHERE status = ?", (filter_status,))

    rows = cursor.fetchall()
    con.close()

    for row in rows:
        ticket_text = f"ID: {row[0]} | {row[1]} | {row[2]} | {row[3]} | Status: {row[4]}"
        listbox_tickets.insert(tk.END, ticket_text)

        # Highlight pending tickets in red
        if row[4] == "Pending":
            listbox_tickets.itemconfig(tk.END, {'fg': 'red'})
        else:
            listbox_tickets.itemconfig(tk.END, {'fg': 'green'})


def update_filter(*args):
    selected_status = combo_filter.get()
    load_tickets(selected_status)
    update_dashboard()


def mark_as_resolved():
    selected = listbox_tickets.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a ticket.")
        return

    ticket_text = listbox_tickets.get(selected[0])
    ticket_id = int(ticket_text.split('|')[0].split(':')[1].strip())
    con = sqlite3.connect("support.db")
    cursor = con.cursor()
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?",
                   ("Resolved", ticket_id))
    con.commit()
    con.close()

    messagebox.showinfo(
        "Success", f"Ticket ID {ticket_id} marked as Resolved.")
    update_filter()


def logout():
    admin_root.destroy()
    import login


# Admin UI
admin_root = tk.Tk()
admin_root.title("Admin Panel - Support Tickets")
admin_root.geometry("700x400")

# DASHBOARD
frame_dashboard = tk.Frame(admin_root, pady=10)
frame_dashboard.pack()

label_total = tk.Label(
    frame_dashboard, text="Total tickets: 0", font=("Arial", 12, "bold"))
label_total.pack()

label_pending = tk.Label(
    frame_dashboard, text="Pending: 0", fg="red", font=("Arial", 10))

label_resolved = tk.Label(
    frame_dashboard, text="Resolved: 0", fg="green", font=("Arial", 12, "bold"))

# FILTER

frame_top = tk.Frame(admin_root, pady=10)
frame_top.pack()

tk.Label(frame_top, text="Filter by Status:").pack(side=tk.LEFT)
combo_filter = ttk.Combobox(
    frame_top, values=["All", "Pending", "Resolved"], state="readonly")
combo_filter.current(0)
combo_filter.pack(side=tk.LEFT, padx=5)
combo_filter.bind("<<ComboboxSelected>>", update_filter)

# LIST

frame_list = tk.Frame(admin_root)
frame_list.pack()

listbox_tickets = tk.Listbox(frame_list, width=80, height=15)
listbox_tickets.pack()

# BUTTONS

frame_buttons = tk.Frame(admin_root, pady=10)
frame_buttons.pack()

tk.Button(frame_buttons, text="Refresh",
          command=update_filter).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Mark as Resolved",
          command=mark_as_resolved).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Logout",
          command=logout).pack(side=tk.LEFT, padx=10)

# INITIAL LOAD
update_filter()
update_dashboard()

admin_root.mainloop()
