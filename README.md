#Sistem Pakar Diagnosa Penyakit THT (GUI)
1. Deskripsi Program
Program ini merupakan implementasi sistem pakar berbasis GUI untuk mendiagnosa penyakit THT (Telinga, Hidung, Tenggorokan). Sistem bekerja dengan cara mencocokkan gejala yang dipilih pengguna dengan basis pengetahuan yang telah disusun sebelumnya, kemudian menghasilkan diagnosis berupa kemungkinan penyakit beserta tingkat kecocokannya.
2. Fitur
  - Tampilan GUI menggunakan Tkinter
  - Input gejala menggunakan checkbox
  - Proses diagnosa otomatis
  - Menampilkan hasil dalam bentuk persentase kecocokan
  - Menampilkan 3 kemungkinan penyakit teratas
3. Metode yang Digunakan
  - Forward Chaining (Data-Driven)
    Metode ini bekerja dengan cara mengambil fakta berupa gejala yang dipilih pengguna, mencocokkannya dengan aturan dalam basis pengetahuan, lalu menghasilkan kesimpulan berupa kemungkinan penyakit
  - Perhitungan Tingkat Kecocokan
    Rumus yang digunakan: Skor = (Jumlah gejala yang cocok) / (Total gejala pada penyakit)
    Hasil akhir ditampilkan dalam bentuk persentase.
4. Alur Kerja Sistem
  - Program dijalankan
  - Sistem menampilkan daftar gejala
  - Pengguna memilih gejala yang dirasakan
  - Pengguna menekan tombol diagnosa
  - Sistem mencocokkan gejala dengan basis pengetahuan
  - Sistem menghitung tingkat kecocokan
  - Sistem menampilkan hasil diagnosa
5. Cara menjalankan program
  - Pastikan Python sudah terinstall
  - Jalankan file program:diagnosapenyakit.py
  - Pilih gejala yang sesuai
  - Klik tombol **Diagnosa**
  - Hasil akan ditampilkan dalam popup

*Penjelasan code terdapat pada file pdf*





