from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl
from datetime import datetime
import calendar  # Untuk validasi jumlah hari dalam bulan

def functionTambahWawancara():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Pelamar dan Lowongan ada
    if 'Pelamar' not in workbook.sheetnames or 'Lowongan' not in workbook.sheetnames:
        print("Sheet Pelamar atau Lowongan tidak ditemukan.")
        workbook.close()
        return

    sheet_pelamar = workbook['Pelamar']
    sheet_lowongan = workbook['Lowongan']

    # Memeriksa atau membuat sheet Wawancara
    sheet_wawancara = cekApakahAdaExcel(workbook, 'Wawancara', ['Kode Lowongan', 'Kode Pelamar', 'Nama Pelamar', 'Posisi', 'Jadwal Tanggal', 'Jadwal Jam'])

    while True:
        # Input kode lowongan
        kode_lowongan = input("\nMasukkan kode lowongan untuk menambahkan jadwal wawancara (atau ketik 'CANCEL' untuk keluar): ")
        if kode_lowongan.upper() == 'CANCEL':
            print("Proses selesai.")
            break

        # Validasi kode lowongan di sheet Lowongan
        posisi_lowongan = None
        for row in sheet_lowongan.iter_rows(min_row=2, values_only=True):
            if row[0] == kode_lowongan:  # row[0] = Kode Lowongan
                posisi_lowongan = row[1]  # row[1] = Posisi
                break

        if not posisi_lowongan:
            print(f"Tidak ada lowongan dengan kode {kode_lowongan}.")
            continue

        # Filter pelamar berdasarkan posisi lowongan dan status wawancara
        pelamar_lowongan = [
            (row[0], row[1], row[3])  # Kode Pelamar, Nama, Posisi Dilamar
            for row in sheet_pelamar.iter_rows(min_row=2, values_only=True)
            if row[3] == posisi_lowongan and row[4] == 'Belum'  # Posisi Dilamar cocok dan Status Wawancara = 'Belum'
        ]

        if not pelamar_lowongan:
            print(f"Tidak ada pelamar dengan status wawancara 'Belum' untuk lowongan dengan kode {kode_lowongan}.")
            continue

        # Tampilkan daftar pelamar yang memenuhi syarat
        print(f"\nPelamar dengan status wawancara 'Belum' untuk lowongan {kode_lowongan}:")
        for i, (kode_pelamar, nama, posisi) in enumerate(pelamar_lowongan, start=1):
            print(f"{i}. Kode: {kode_pelamar}, Nama: {nama}, Posisi: {posisi}")

        # Pilih pelamar untuk wawancara
        while True:
            try:
                pilihan = int(input("Pilih nomor pelamar untuk dijadwalkan wawancara (atau ketik '0' untuk membatalkan): "))
                if pilihan == 0:
                    print("Proses pemilihan pelamar dibatalkan.")
                    break

                if 1 <= pilihan <= len(pelamar_lowongan):
                    kode_pelamar, nama, posisi = pelamar_lowongan[pilihan - 1]
                    break

                print("Pilihan tidak valid. Masukkan nomor yang sesuai.")
            except ValueError:
                print("Input harus berupa angka.")

        if pilihan == 0:
            continue

        # Masukkan jadwal wawancara
        while True:
            try:
                bulan = int(input("Masukkan bulan wawancara (1-12): "))
                tahun = datetime.now().year  # Tahun otomatis diambil dari sistem

                # Validasi bulan
                if not (1 <= bulan <= 12):
                    print("Bulan tidak valid. Masukkan bulan antara 1 dan 12.")
                    continue

                # Dapatkan jumlah hari dalam bulan
                max_hari = calendar.monthrange(tahun, bulan)[1]
                print(f"Bulan {bulan} pada tahun {tahun} memiliki {max_hari} hari.")

                # Minta input tanggal
                tanggal = int(input(f"Masukkan tanggal wawancara (1-{max_hari}): "))
                if 1 <= tanggal <= max_hari:
                    jam = input("Masukkan jam wawancara (format 24 jam, contoh: 14:00): ")
                    break
                else:
                    print(f"Masukkan tanggal antara 1 dan {max_hari}.")
            except ValueError:
                print("Input tidak valid. Masukkan angka untuk bulan dan tanggal.")

        # Format tanggal menjadi string
        jadwal_tanggal = f"{tahun:04d}-{bulan:02d}-{tanggal:02d}"  # Format: YYYY-MM-DD

        # Tambahkan jadwal ke sheet Wawancara
        sheet_wawancara.append([kode_lowongan, kode_pelamar, nama, posisi, jadwal_tanggal, jam])
        print(f"Jadwal wawancara berhasil ditambahkan untuk pelamar {nama} pada {jadwal_tanggal} jam {jam}.")

        # Update status wawancara di sheet Pelamar
        for row in sheet_pelamar.iter_rows(min_row=2):
            if row[0].value == kode_pelamar:
                row[4].value = 'Proses'
                break
            
    # Simpan workbook setelah selesai
    workbook.save(FILE_NAME)
    workbook.close()
    print("Data wawancara berhasil disimpan.")
