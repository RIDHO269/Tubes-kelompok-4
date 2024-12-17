import tkinter as tk
from tkinter import messagebox, simpledialog

# Data pengguna (username dan password)
USER_CREDENTIALS = {"admin": "1234"}

# Data soal kuis
questions = []  # List untuk menyimpan soal dan jawaban

# Fungsi Login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Berhasil", f"Selamat Datang, {username}!")
        main_menu()
    else:
        messagebox.showerror("Login Gagal", "Username atau Password salah!")

# Fungsi Menu Utama
def main_menu():
    login_frame.destroy()  # Hapus frame login
    global main_frame
    main_frame = tk.Frame(window)
    main_frame.pack()
    
    tk.Label(main_frame, text="Menu Utama", font=("Arial", 16)).pack()
    tk.Button(main_frame, text="Tambah Soal", command=add_question).pack(pady=5)
    tk.Button(main_frame, text="Edit Soal", command=edit_question).pack(pady=5)
    tk.Button(main_frame, text="Hapus Soal", command=delete_question).pack(pady=5)
    tk.Button(main_frame, text="Mulai Kuis", command=start_quiz).pack(pady=5)
    tk.Button(main_frame, text="Keluar", command=window.quit).pack(pady=5)

# Fungsi Tambah Soal
def add_question():
    question = simpledialog.askstring("Tambah Soal", "Masukkan pertanyaan:")
    answer = simpledialog.askstring("Tambah Jawaban", "Masukkan jawaban yang benar:")
    if question and answer:
        questions.append({"question": question, "answer": answer})
        messagebox.showinfo("Berhasil", "Soal berhasil ditambahkan!")

# Fungsi Edit Soal
def edit_question():
    if not questions:
        messagebox.showwarning("Peringatan", "Tidak ada soal untuk diedit.")
        return
    
    index = simpledialog.askinteger("Edit Soal", f"Masukkan nomor soal (1-{len(questions)}):")
    if index and 1 <= index <= len(questions):
        question = simpledialog.askstring("Edit Soal", "Masukkan pertanyaan baru:")
        answer = simpledialog.askstring("Edit Jawaban", "Masukkan jawaban baru:")
        if question and answer:
            questions[index - 1] = {"question": question, "answer": answer}
            messagebox.showinfo("Berhasil", "Soal berhasil diubah!")
    else:
        messagebox.showerror("Error", "Nomor soal tidak valid.")

# Fungsi Hapus Soal
def delete_question():
    if not questions:
        messagebox.showwarning("Peringatan", "Tidak ada soal untuk dihapus.")
        return
    
    index = simpledialog.askinteger("Hapus Soal", f"Masukkan nomor soal (1-{len(questions)}):")
    if index and 1 <= index <= len(questions):
        questions.pop(index - 1)
        messagebox.showinfo("Berhasil", "Soal berhasil dihapus!")
    else:
        messagebox.showerror("Error", "Nomor soal tidak valid.")

# Fungsi Mulai Kuis
def start_quiz():
    if not questions:
        messagebox.showwarning("Peringatan", "Tidak ada soal untuk kuis.")
        return
    
    score = 0
    for i, q in enumerate(questions):
        answer = simpledialog.askstring(f"Soal {i+1}", q["question"])
        if answer and answer.lower() == q["answer"].lower():
            score += 1
    
    messagebox.showinfo("Skor Akhir", f"Skor Anda: {score}/{len(questions)}")

# GUI Utama
window = tk.Tk()
window.title("Aplikasi Kuis Sederhana")

# Frame Login
login_frame = tk.Frame(window)
login_frame.pack()

tk.Label(login_frame, text="Login", font=("Arial", 16)).pack(pady=10)
tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=login).pack(pady=10)

window.mainloop()