import tkinter as tk
from tkinter import ttk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.resizable(False, False)

# Label judul
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold")
)
judul.pack(pady=20)

# Frame untuk input nilai
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Daftar mata pelajaran
mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Informatika",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Sejarah",
    "Geografi"
]

# Membuat 10 input nilai
input_nilai = []

for i, nama_mapel in enumerate(mapel):
    label = tk.Label(
        frame_input,
        text=nama_mapel,
        width=20,
        anchor="w",
        font=("Arial", 10)
    )
    label.grid(row=i, column=0, padx=10, pady=5)

    entry = ttk.Entry(frame_input, width=15)
    entry.grid(row=i, column=1, padx=10, pady=5)

    input_nilai.append(entry)

