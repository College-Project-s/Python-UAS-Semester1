# Sistem Manajemen Rekrutmen Berbasis Python

Proyek ini adalah **Sistem Manajemen Rekrutmen** berbasis Python yang dirancang untuk mengelola data lowongan kerja, penawaran, pelamar, jadwal wawancara, dan seleksi akhir. Sistem ini menggunakan **OpenPyXL** untuk memanipulasi file Excel sehingga mempermudah penyimpanan dan pengelolaan data rekrutmen.

## **Deskripsi Proyek**

Sistem ini dirancang untuk membantu mempermudah proses rekrutmen dengan menyediakan antarmuka berbasis terminal yang sederhana. Berikut adalah fitur utama yang tersedia:

1. **Manajemen Lowongan (Lowongan)**
   - Tambah, lihat, edit, dan hapus data lowongan kerja.
2. **Manajemen Penawaran (Penawaran)**
   - Tambah manfaat/benefit untuk lowongan tertentu.
3. **Manajemen Pelamar (Pelamar)**
   - Tambah dan lihat data pelamar yang mendaftar ke lowongan kerja.
4. **Penjadwalan Wawancara (Wawancara)**
   - Jadwalkan wawancara untuk pelamar dengan status wawancara "Belum".
5. **Manajemen Seleksi (Seleksi)**
   - Perbarui status wawancara pelamar dan lakukan seleksi akhir untuk menentukan pelamar yang diterima.

---

## **Alur Program**

Sistem ini mengikuti alur kerja rekrutmen yang terstruktur. Berikut penjelasan lengkap alur kerja program:

### **1. Menambahkan Lowongan**

Langkah pertama adalah membuat data lowongan kerja. Setiap lowongan terdiri dari:
- **Kode Lowongan**: ID unik untuk setiap lowongan.
- **Posisi**: Nama posisi yang ditawarkan.
- **Deskripsi**: Penjelasan singkat mengenai posisi tersebut.
- **Status**: Status lowongan, apakah `Dibuka` atau `Ditutup`.

### **2. Menambahkan Penawaran (Benefit)**

Setelah data lowongan ditambahkan, Anda dapat menambahkan manfaat atau benefit untuk lowongan tersebut. 
- Pilih **Kode Lowongan** yang sudah dibuat sebelumnya.
- Masukkan manfaat/benefit yang relevan dengan lowongan tersebut.

### **3. Menambahkan Data Pelamar**

Setelah data lowongan dan penawarannya tersedia, pelamar dapat didaftarkan ke sistem. Data pelamar meliputi:
- **Kode Pelamar**: ID unik untuk setiap pelamar.
- **Nama**: Nama pelamar.
- **Kontak**: Informasi kontak pelamar.
- **Kode Lowongan**: Lowongan yang dipilih pelamar.
- **Status Wawancara**: Secara default akan diatur ke `Belum`.

### **4. Menjadwalkan Wawancara**

Wawancara dapat dijadwalkan untuk pelamar dengan status wawancara "Belum":
- Tampilkan daftar lowongan yang memiliki pelamar dengan status "Belum".
- Pilih **Kode Lowongan** untuk melihat daftar pelamar.
- Jadwalkan tanggal dan waktu wawancara.
- Setelah wawancara dijadwalkan, status pelamar akan diperbarui menjadi `Proses`.

### **5. Proses Seleksi**

Proses seleksi dilakukan dalam dua tahap:
1. **Perbarui Status Wawancara**:
   - Tampilkan pelamar dengan status wawancara `Proses`.
   - Perbarui status wawancara menjadi `Sudah` (Selesai) setelah wawancara dilakukan.

2. **Seleksi Akhir**:
   - Tampilkan pelamar dengan status wawancara `Sudah`.
   - Tentukan status seleksi pelamar sebagai `Diterima` atau `Ditolak`.
   - Data seleksi akhir akan disimpan di sheet `Seleksi`.

---

## **Teknologi yang Digunakan**

- **Python**: Bahasa pemrograman utama untuk mengimplementasikan sistem.
- **OpenPyXL**: Library Python untuk membaca dan menulis file Excel.
- **Excel**: Berfungsi sebagai database untuk menyimpan data lowongan, pelamar, wawancara, dan seleksi.

---

## **Cara Menjalankan Program**

1. **Clone repository**:
   ```bash
   git clone https://github.com/College-Project-s/Python-UAS-Semester1.git
   cd Python-UAS-Semester1

## **Kontributor**
1. **Para Kontributor**: 
    - [Calvin William Wijaya] - [Merancang Dan Membuat Program]
    - [Farhan Ginting] - [Merancang Dan Membuat Program]
    - [Gefira Nazibah Nur Luza'In] - [Membuat Laporan Ringkasan Proyek]
    - [Muhamad Syaeful] - [Membuat Laporan Ringkasan Proyek]

## **Lisensi**
Proyek ini dilisensikan di bawah lisensi MIT. Lihat file [MIT license](https://opensource.org/licenses/MIT) untuk informasi lebih lanjut.
