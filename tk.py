import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Data Mahasiswa")
window.geometry('440x540')
window.configure(bg='#333333')

def Mhs():
    nim = "23100705"
    nama = "Dwioktasaputra"
    prodi = "Teknik Informatika"
    semester = "3"
    if (nim_entry.get() == nim and 
        nama_entry.get() == nama and 
        prodi_entry.get() == prodi and 
        semester_entry.get() == semester):
        messagebox.showinfo(title="Berhasil disimpan", message="You successfully Saved.")
    else:
        messagebox.showerror(title="Error", message="Invalid.")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
Mhs_label = tkinter.Label(
    frame, text="Data Mahasiswa", bg='#333333', fg="#FF3399", font=("Arial", 30))
nim_label = tkinter.Label(
    frame, text="NIM", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
nim_entry = tkinter.Entry(frame, font=("Arial", 16))
nama_label = tkinter.Label(
    frame, text="Nama", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
nama_entry = tkinter.Entry(frame, font=("Arial", 16))
prodi_label = tkinter.Label(
    frame, text="Prodi", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
prodi_entry = tkinter.Entry(frame, font=("Arial", 16))
semester_label = tkinter.Label(
    frame, text="Semester", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
semester_entry = tkinter.Entry(frame, font=("Arial", 16))
Mhs_button = tkinter.Button(
    frame, text="Simpan", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Mhs)

# Placing widgets on the screen
Mhs_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
nim_label.grid(row=1, column=0)
nim_entry.grid(row=1, column=1, pady=20)
nama_label.grid(row=2, column=0)
nama_entry.grid(row=2, column=1, pady=20)
prodi_label.grid(row=3, column=0)
prodi_entry.grid(row=3, column=1, pady=20)
semester_label.grid(row=4, column=0)
semester_entry.grid(row=4, column=1, pady=20)
Mhs_button.grid(row=5, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()