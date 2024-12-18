import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Data pengguna (username, password, dan role)
USER_CREDENTIALS = {}
questions = [] # List untuk menyimpan soal dan jawaban

# Fungsi Login
def login():
username = username_entry.get()
password = password_entry.get()

if username in USER_CREDENTIALS and USER_CREDENTIALS[username]['password'] == password:
role = USER_CREDENTIALS[username]['role']
messagebox.showinfo("Login Berhasil", f"Selamat Datang, {username} ({role})!")
main_menu(role)
else:
messagebox.showerror("Login Gagal", "Username atau Password salah!")

# Fungsi Register
def register():
register_window = tk.Toplevel(window)
register_window.title("Register")
register_window.geometry("450x450")
register_window.config(bg="#2d3e50") # Background untuk Register Window

ttk.Label(register_window, text="Register", font=("Comic Sans MS", 18, "bold"), background="#2d3e50", foreground="gold").pack(pady=15)

ttk.Label(register_window, text="Username:", font=("Comic Sans MS", 12), background="#2d3e50", foreground="gold").pack()
username_entry = ttk.Entry(register_window, font=("Comic Sans MS", 12))
username_entry.pack(pady=5)

ttk.Label(register_window, text="Password:", font=("Comic Sans MS", 12), background="#2d3e50", foreground="gold").pack()
password_entry = ttk.Entry(register_window, show="*", font=("Comic Sans MS", 12))
password_entry.pack(pady=5)

ttk.Label(register_window, text="Pilih Role:", font=("Comic Sans MS", 12), background="#2d3e50", foreground="gold").pack(pady=5)
role_var = tk.StringVar(value="Student") # Default role
student_radio = ttk.Radiobutton(register_window, text="Student", variable=role_var, value="Student", style="TButton")
teacher_radio = ttk.Radiobutton(register_window, text="Teacher", variable=role_var, value="Teacher", style="TButton")
student_radio.pack(pady=3)
teacher_radio.pack(pady=3)
