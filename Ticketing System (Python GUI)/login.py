import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import hashlib
con = sqlite3.connect("users.db")
cursor = con.cursor()

# Create users.db if not exists
if not os.path.exists("users.db"):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)
    # Default admin
    hashed_admin = hashlib.sha256("admin123".encode()).hexdigest()
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
                   ("admin", hashed_admin, "admin"))

    con.commit()
    con.close()


def open_user_window():
    import user


def open_admin_window():
    import admin


def login():
    username = entry_username.get()
    password = entry_password.get()

    hashed_input = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute(
        "SELECT role FROM users WHERE username=? AND password=?", (username, hashed_input))

    result = cursor.fetchone()
    con.close()

    if result:
        role = result[0]
        messagebox.showinfo("Login Successful", f"Welcome, {role.title()}!")
        login_root.destroy()
        if role == "admin":
            open_admin_window()
        else:
            open_user_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def register():
    def save_registration():

        new_user = reg_username.get()
        new_pass = reg_password.get()

        if not new_user or not new_pass:
            messagebox.showwarning("Incomplete", "Please fill all fields.")
            return
        if len(new_pass) < 6:
            messagebox.showwarning(
                "Weak Password", "Password should be at least 6 characters.")
            return

        try:
            hashed_pass = hashlib.sha256(new_pass.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           (new_user, hashed_pass, "user"))

            con.commit()
            messagebox.showinfo(
                "Success", "Account created! You can now log in.")
            reg_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        con.close()

    reg_window = tk.Toplevel(login_root)
    reg_window.title("Register")
    reg_window.geometry("300x200")

    tk.Label(reg_window, text="New Username").pack(pady=5)
    reg_username = tk.Entry(reg_window)
    reg_username.pack()

    tk.Label(reg_window, text="New Password").pack(pady=5)
    reg_password = tk.Entry(reg_window, show="*")
    reg_password.pack()

    tk.Button(reg_window, text="Register",
              command=save_registration).pack(pady=15)


# Login Window
login_root = tk.Tk()
login_root.title("IT Support - Login")
login_root.geometry("300x230")

tk.Label(login_root, text="Username").pack(pady=5)
entry_username = tk.Entry(login_root)
entry_username.pack()

tk.Label(login_root, text="Password").pack(pady=5)
entry_password = tk.Entry(login_root, show="*")
entry_password.pack()

tk.Button(login_root, text="Login", command=login, width=20).pack(pady=10)
tk.Button(login_root, text="Register", command=register, width=20).pack()

login_root.mainloop()
