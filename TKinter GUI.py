import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nim = entry_nim.get()
    nama = entry_nama.get()
    prodi = entry_prodi.get()
    semester = entry_semester.get()
    ipk1 = entry_ipk1.get()
    ipk2 = entry_ipk2.get()

    if not (nim and nama and prodi and semester and ipk1 and ipk2):
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    try:
        ipk1 = float(ipk1)
        ipk2 = float(ipk2)
    except ValueError:
        messagebox.showerror("Kesalahan", "IPK harus berupa angka!")
        return

    # Simpan data ke file (contoh: CSV)
    with open("data_mahasiswa.csv", "a") as file:
        file.write(f"{nim},{nama},{prodi},{semester},{ipk1},{ipk2}\n")

    messagebox.showinfo("Sukses", "Data berhasil disimpan!")
    
    # Kosongkan input
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_prodi.delete(0, tk.END)
    entry_semester.delete(0, tk.END)
    entry_ipk1.delete(0, tk.END)
    entry_ipk2.delete(0, tk.END)

# Membuat GUI
root = tk.Tk()
root.title("Form Data Mahasiswa")

# Label dan Entry
labels = ["NIM", "Nama", "Prodi", "Semester", "IPK Semester 1", "IPK Semester 2"]
entries = []

for i, text in enumerate(labels):
    label = tk.Label(root, text=text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_nim, entry_nama, entry_prodi, entry_semester, entry_ipk1, entry_ipk2 = entries

# Tombol Simpan
btn_simpan = tk.Button(root, text="SIMPAN", command=simpan_data)
btn_simpan.grid(row=len(labels), column=0, columnspan=2, pady=10)

root.mainloop()
