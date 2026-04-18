import tkinter as tk
from tkinter import messagebox

#data gejala penyait THT
gejala_list = [
    ("G01", "Nafas abnormal"),
    ("G02", "Suara serak"),
    ("G03", "perubahan kulit"),
    ("G04", "Telinga penuh"),
    ("G05", "Nyeri bicara menelan"),
    ("G06", "Nyeri tenggorokan"),
    ("G07", "Nyeri leher"),
    ("G08", "Pendarahan hidung"),
    ("G09", "Telinga berdenging"),
    ("G10", "Airliur menetes"),
    ("G11", "Perubahan suara"),
    ("G12", "Sakit kepala"),
    ("G13", "Nyeri pinggir hidung"),
    ("G14", "Serangan vertigo"),
    ("G15", "Getah bening"),
    ("G16", "Leher bengkak"),
    ("G17", "Hidung tersumbat"),
    ("G18", "Infeksi sinus"),
    ("G19", "Berat badan turun"),
    ("G20", "Nyeri telinga"),
    ("G21", "Selaput lendir merah"),
    ("G22", "Benjolan leher"),
    ("G23", "Tubuh tak seimbang"),
    ("G24", "Bola mata bergerak"),
    ("G25", "Nyeri wajah"),
    ("G26", "Dahi sakit"),
    ("G27", "Batuk"),
    ("G28", "Tumbuh di mulut"),
    ("G29", "Benjolan di leher"),
    ("G30", "Nyeri antara mata"),
    ("G31", "Radang gendang telinga"),
    ("G32", "Tenggorokan gatal"),
    ("G33", "Hidung meler"),
    ("G34", "Tuli"),
    ("G35", "Mual muntah"),
    ("G36", "Letih lesu"),
    ("G37", "Demam"),
]

#knowledge base penyakit THT
penyakit_list = [
    ("P01", "Tonsillitis", ["G37", "G12", "G5", "G27", "G6", "G21"]),
    ("P02", "Sinusitis Maksilaris", ["G37", "G12", "G27", "G17", "G33", "G36", "G29"]),
    ("P03", "Sinusitis Frontalis", ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"]),
    ("P04", "Sinusitis Edmoidalis", ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"]),
    ("P05", "Sinusitis Sfenoidalis", ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"]),
    ("P06", "Abses Peritonsiler", ["G37", "G12", "G6", "G15", "G2", "G29", "G10"]),
    ("P07", "Faringitis", ["G37", "G5", "G6", "G7", "G15"]),
    ("P08", "Kanker Laring", ["G5", "G27", "G6", "G15", "G2", "G19", "G1"]),
    ("P09", "Deviasi Septum", ["G37", "G17", "G20", "G8", "G18", "G25"]),
    ("P10", "Laringitis", ["G37", "G5", "G15", "G16", "G32"]),
    ("P11", "Kanker Leher & Kepala", ["G5", "G22", "G8", "G28", "G3", "G11"]),
    ("P12", "Otitis Media Akut", ["G37", "G20", "G35", "G31"]),
    ("P13", "Contact Ulcers", ["G5", "G2"]),
    ("P14", "Abses Parafaringeal", ["G5", "G16"]),
    ("P15", "Barotitis Media", ["G12", "G20"]),
    ("P16", "Kanker Nafasoring", ["G17", "G8"]),
    ("P17", "Kanker Tonsil", ["G6", "G29"]),
    ("P18", "Neuronitis Vestibularis", ["G35", "G24"]),
    ("P19", "Meniere", ["G20", "G35", "G14", "G4"]),
    ("P20", "Tumor Syaraf Pendengaran", ["G12", "G34", "G23"]),
    ("P21", "Kanker Leher Metastatik", ["G29"]),
    ("P22", "Osteosklerosis", ["G34", "G9"]),
    ("P23", "Vertigo Postular", ["G24"]),
]
# GUI
# ========================
root = tk.Tk()
root.title("Sistem Pakar THT")

checkbox_vars = {}

# tampilkan gejala
for i, (kode, gejala) in enumerate(gejala_list):
    var = tk.IntVar()
    cb = tk.Checkbutton(root, text=f"{kode} - {gejala}", variable=var)
    cb.grid(row=i//2, column=i%2, sticky="w")
    checkbox_vars[kode] = var


# ========================
# FUNGSI DIAGNOSA
# ========================
def diagnosa():
    selected = [kode for kode, var in checkbox_vars.items() if var.get() == 1]

    if not selected:
        messagebox.showwarning("Peringatan", "Pilih minimal 1 gejala!")
        return

    hasil = []
    
    for kode_p, nama_p, gejala_p in penyakit_list:
        cocok = len(set(selected) & set(gejala_p))
        skor = cocok / len(gejala_p)

        if cocok > 0:
            hasil.append((nama_p, skor))

    if not hasil:
        messagebox.showinfo("Hasil", "Tidak ditemukan penyakit yang cocok")
        return

    # urutkan
    hasil.sort(key=lambda x: x[1], reverse=True)

    teks = "Hasil Diagnosa:\n\n"
    for nama, skor in hasil[:3]:
        teks += f"{nama} ({skor*100:.2f}%)\n"

    messagebox.showinfo("Hasil Diagnosa", teks)


# tombol
btn = tk.Button(root, text="Diagnosa", command=diagnosa)
btn.grid(row=20, column=0, columnspan=2)

root.mainloop()