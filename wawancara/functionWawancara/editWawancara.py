from moduleExcel import FILE_NAME, os, openpyxl
from datetime import datetime
import calendar  # Untuk validasi jumlah hari dalam bulan

def functionEditWawancara():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Wawancara ada
    if 'Wawancara' not in workbook.sheetnames:
        print("Sheet Wawancara belum ada.")
        workbook.close()
        return

    sheet_wawancara = workbook['Wawancara']

    # Periksa apakah ada data di sheet Wawancara
    if sheet_wawancara.max_row == 1:  # Hanya header yang ada
        print("Belum ada data wawancara.")
        workbook.close()
        return

    # Loop untuk memastikan kode pelamar valid
    while True:
        # Tampilkan data wawancara
        print("\nDaftar Jadwal Wawancara:")
        for row in sheet_wawancara.iter_rows(min_row=2, values_only=True):
            print(f"Kode Lowongan: {row[0]}, Kode Pelamar: {row[1]}, Nama Pelamar: {row[2]}, Posisi: {row[3]}, Tanggal: {row[4]}, Jam: {row[5]}")

        # Input kode pelamar untuk diubah
        kode_pelamar = input("\nMasukkan kode pelamar yang ingin diubah jadwal wawancaranya (atau ketik 'CANCEL' untuk keluar): ")
        if kode_pelamar.upper() == 'CANCEL':
            print("Proses selesai.")
            break

        # Cari data wawancara berdasarkan kode pelamar
        baris_wawancara = None
        for row_index, row in enumerate(sheet_wawancara.iter_rows(min_row=2), start=2):
            if row[1].value == kode_pelamar:  # row[1] = Kode Pelamar
                baris_wawancara = row_index
                break

        if not baris_wawancara:
            print(f"Tidak ditemukan jadwal wawancara untuk pelamar dengan kode {kode_pelamar}. Silakan coba lagi.")
            continue  # Ulangi input kode pelamar

        # Data saat ini
        data_sebelumnya = {
            "tanggal": sheet_wawancara.cell(row=baris_wawancara, column=5).value,  # Kolom Tanggal
            "jam": sheet_wawancara.cell(row=baris_wawancara, column=6).value  # Kolom Jam
        }

        # Input jadwal baru
        print("\n--- Perbarui Jadwal Wawancara ---")
        print(f"Data sebelumnya: Tanggal = {data_sebelumnya['tanggal']}, Jam = {data_sebelumnya['jam']}")

        # Input bulan dan tanggal baru
        while True:
            try:
                bulan = input("Masukkan bulan wawancara baru (1-12) [kosongkan untuk tidak mengubah]: ")
                if bulan == "":
                    bulan = int(data_sebelumnya['tanggal'].split("-")[1])  # Gunakan bulan dari data sebelumnya
                else:
                    bulan = int(bulan)

                tahun = datetime.now().year  # Tahun otomatis diambil dari sistem

                # Validasi bulan
                if not (1 <= bulan <= 12):
                    print("Bulan tidak valid. Masukkan bulan antara 1 dan 12.")
                    continue

                # Dapatkan jumlah hari dalam bulan
                max_hari = calendar.monthrange(tahun, bulan)[1]
                print(f"Bulan {bulan} pada tahun {tahun} memiliki {max_hari} hari.")

                # Minta input tanggal
                tanggal = input(f"Masukkan tanggal wawancara baru (1-{max_hari}) [kosongkan untuk tidak mengubah]: ")
                if tanggal == "":
                    tanggal = int(data_sebelumnya['tanggal'].split("-")[2])  # Gunakan tanggal dari data sebelumnya
                else:
                    tanggal = int(tanggal)

                if 1 <= tanggal <= max_hari:
                    jam = input(f"Masukkan jam wawancara baru (format 24 jam, contoh: 14:00) [kosongkan untuk tidak mengubah]: ")
                    if jam == "":
                        jam = data_sebelumnya['jam']  # Gunakan jam dari data sebelumnya
                    break
                else:
                    print(f"Masukkan tanggal antara 1 dan {max_hari}.")
            except ValueError:
                print("Input tidak valid. Masukkan angka untuk bulan dan tanggal.")

        # Format tanggal baru menjadi string
        jadwal_tanggal_baru = f"{tahun:04d}-{bulan:02d}-{tanggal:02d}"  # Format: YYYY-MM-DD

        # Perbarui data di sheet Wawancara
        sheet_wawancara.cell(row=baris_wawancara, column=5).value = jadwal_tanggal_baru  # Kolom Tanggal
        sheet_wawancara.cell(row=baris_wawancara, column=6).value = jam  # Kolom Jam

        print(f"\nJadwal wawancara untuk pelamar {kode_pelamar} berhasil diperbarui ke tanggal {jadwal_tanggal_baru} jam {jam}.")

        # Simpan workbook setelah selesai
        workbook.save(FILE_NAME)
        workbook.close()
        print("Perubahan jadwal wawancara berhasil disimpan.")
        break  # Keluar dari loop setelah proses selesai
