# GUI -> Graphical User Interface
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("500x300")
window.resizable(False, False)
window.title("Sapa Dia!")

# variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


# fungsi tombol click: dipanggil ketika klik tombol
def tombol_click():
    pesan = f"Halo, {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="TEST", message=pesan)


# frame input
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol_sapa.pack(pady=10, padx=10, fill="x", expand=True)

# Main loop window: harus ada ini untuk menampilkan window
window.mainloop()
