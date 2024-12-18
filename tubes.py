import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Data pengguna (username, password, dan role)
USER_CREDENTIALS = {}
questions = []  # List untuk menyimpan soal dan jawaban

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
    register_window.config(bg="#D8BFD8")  # Latar belakang ungu muda

    tk.Label(register_window, text="Register", font=("Comic Sans MS", 18, "bold"), bg="#D8BFD8", fg="gold").pack(pady=15)
    tk.Label(register_window, text="Username:", font=("Comic Sans MS", 12), bg="#D8BFD8", fg="white").pack()
    username_entry = tk.Entry(register_window, font=("Comic Sans MS", 12))
    username_entry.pack(pady=5)

    tk.Label(register_window, text="Password:", font=("Comic Sans MS", 12), bg="#D8BFD8", fg="white").pack()
    password_entry = tk.Entry(register_window, show="*", font=("Comic Sans MS", 12))
    password_entry.pack(pady=5)

    tk.Label(register_window, text="Pilih Role:", font=("Comic Sans MS", 12), bg="#D8BFD8", fg="white").pack(pady=5)
    role_var = tk.StringVar(value="Student")

    student_radio = tk.Radiobutton(register_window, text="Student", variable=role_var, value="Student", bg="#D8BFD8", fg="white", font=("Comic Sans MS", 12))
    student_radio.pack(pady=3)
    teacher_radio = tk.Radiobutton(register_window, text="Teacher", variable=role_var, value="Teacher", bg="#D8BFD8", fg="white", font=("Comic Sans MS", 12))
    teacher_radio.pack(pady=3)

    def save_registration():
        username = username_entry.get()
        password = password_entry.get()
        role = role_var.get()

        if not username or username in USER_CREDENTIALS:
            messagebox.showerror("Error", "Username tidak valid atau sudah digunakan!", parent=register_window)
            return

        if not password:
            messagebox.showerror("Error", "Password tidak boleh kosong!", parent=register_window)
            return

        USER_CREDENTIALS[username] = {'password': password, 'role': role}
        messagebox.showinfo("Berhasil", "Registrasi berhasil! Silakan login.", parent=register_window)
        register_window.destroy()

    tk.Button(register_window, text="Register", command=save_registration, bg="gold", fg="black", font=("Comic Sans MS", 12)).pack(pady=10)
# Fungsi Menu Utama
def main_menu(role):
    login_frame.pack_forget()
    global main_frame
    main_frame = tk.Frame(window, bg="#D8BFD8")
    main_frame.pack(fill="both", expand=True)

    tk.Label(main_frame, text=f"MENU UTAMA - {role.upper()}", font=("Comic Sans MS", 18, "bold"), bg="#D8BFD8", fg="gold").pack(pady=10)

    if role == "Teacher":
        tk.Button(main_frame, text="TAMBAH SOAL", command=add_question, bg="gold", font=("Comic Sans MS", 12)).pack(pady=5)
        tk.Button(main_frame, text="SELESAI TAMBAH SOAL", command=finish_adding_questions, bg="gold", font=("Comic Sans MS", 12)).pack(pady=5)
        tk.Button(main_frame, text="LIHAT SOAL", command=view_questions, bg="gold", font=("Comic Sans MS", 12)).pack(pady=5)
    elif role == "Student":
        tk.Button(main_frame, text="MULAI KUIS", command=start_quiz, bg="gold", font=("Comic Sans MS", 12)).pack(pady=5)

    tk.Button(main_frame, text="KELUAR", command=logout, bg="gold", font=("Comic Sans MS", 12)).pack(pady=10)

# Fungsi Logout
def logout():
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Fungsi Tambah Soal
def add_question():
    question = simpledialog.askstring("Tambah Soal", "Masukkan pertanyaan:")
    answer = simpledialog.askstring("Tambah Jawaban", "Masukkan jawaban yang benar:")
    if question and answer:
        questions.append({"question": question, "answer": answer})
        messagebox.showinfo("Berhasil", "Soal berhasil ditambahkan!")
        view_questions()

# Fungsi Menyelesaikan Penambahan Soal
def finish_adding_questions():
    messagebox.showinfo("Berhasil", "Penambahan soal selesai!")
    logout()

# Fungsi Lihat Soal
def view_questions():
    if not questions:
        messagebox.showinfo("Soal Kosong", "Belum ada soal yang ditambahkan!")
        return

    questions_window = tk.Toplevel(window)
    questions_window.title("Daftar Soal")
    questions_window.geometry("400x400")
    questions_window.config(bg="#D8BFD8")

    ttk.Label(questions_window, text="Daftar Soal", font=("Comic Sans MS", 18, "bold"), background="#D8BFD8", foreground="gold").pack(pady=10)
    for i, q in enumerate(questions):
        ttk.Label(questions_window, text=f"Soal {i+1}: {q['question']}", font=("Comic Sans MS", 12), background="#D8BFD8", foreground="gold").pack(pady=5)

    ttk.Button(questions_window, text="Tutup", command=questions_window.destroy).pack(pady=10)
