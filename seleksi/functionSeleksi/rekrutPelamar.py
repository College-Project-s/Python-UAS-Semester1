from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl

def functionRekrutPelamar():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    if 'Pelamar' not in workbook.sheetnames:
        print("Sheet Pelamar belum ada.")
        workbook.close()
        return
    
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        workbook.close()
        return

    # Pastikan sheet Seleksi ada
    sheet_seleksi = cekApakahAdaExcel(workbook, 'Seleksi', ['Kode Pelamar', 'Nama', 'Posisi', 'Status Seleksi'])
    sheet_lowongan = workbook['Lowongan']
    sheet_pelamar = workbook['Pelamar']

    while True:
        # Dapatkan daftar kode pelamar yang sudah ada di sheet Seleksi
        kode_pelamar_seleksi = set(row[0] for row in sheet_seleksi.iter_rows(min_row=2, values_only=True))

        # Filter posisi yang dibuka dan memiliki pelamar dengan wawancara selesai, namun belum ada di seleksi
        posisi_tersedia = []
        for lowongan in sheet_lowongan.iter_rows(min_row=2, values_only=True):
            kode_lowongan, posisi, _, status = lowongan
            if status == 'Dibuka':
                pelamar_tersedia = any(
                    row[3] == posisi and row[4] == "Selesai" and row[0] not in kode_pelamar_seleksi
                    for row in sheet_pelamar.iter_rows(min_row=2, values_only=True)
                )
                if pelamar_tersedia:
                    posisi_tersedia.append(posisi)

        if not posisi_tersedia:
            print("Tidak ada lowongan yang dibuka dengan pelamar (wawancara selesai) yang belum masuk seleksi.")
            workbook.close()
            return

        print("\nLowongan yang tersedia dengan pelamar (wawancara selesai):")
        for posisi in posisi_tersedia:
            print(f"- {posisi}")

        # Input posisi pilihan
        while True:
            posisi_pilihan = input("Masukkan posisi yang ingin dilihat pelamarnya (atau ketik 'CANCEL' untuk kembali): ")

            if posisi_pilihan.upper() == 'CANCEL':
                print("Proses dibatalkan.")
                workbook.close()
                return
            
            if posisi_pilihan in posisi_tersedia:
                break
            print("Posisi tidak valid atau tidak tersedia. Silakan coba lagi.")

        # Tampilkan daftar pelamar berdasarkan posisi yang dipilih, status wawancara selesai, dan belum masuk seleksi
        pelamar_terpilih = [
            (row[0], row[1])  # Kode Pelamar dan Nama
            for row in sheet_pelamar.iter_rows(min_row=2, values_only=True)
            if row[3] == posisi_pilihan and row[4] == "Selesai" and row[0] not in kode_pelamar_seleksi
        ]

        if not pelamar_terpilih:
            print(f"Tidak ada pelamar untuk posisi {posisi_pilihan} yang belum masuk seleksi.")
            continue

        print(f"\nDaftar pelamar untuk posisi {posisi_pilihan} (wawancara selesai dan belum masuk seleksi):")
        for kode, nama in pelamar_terpilih:
            print(f"- {kode}: {nama}")

        # Proses kode pelamar untuk seleksi
        while True:
            kode_pelamar = input("Masukkan kode pelamar yang ingin diproses (atau ketik 'CANCEL' untuk kembali): ")
            if kode_pelamar.upper() == 'CANCEL':
                print("Proses dibatalkan.")
                break

            pelamar_dipilih = next((pelamar for pelamar in pelamar_terpilih if pelamar[0] == kode_pelamar), None)
            if pelamar_dipilih:
                break
            print("Kode pelamar tidak valid. Silakan coba lagi.")

        if kode_pelamar.upper() == 'CANCEL':
            continue

        while True:
            status = input("Masukkan status seleksi (Diterima/Ditolak): ")
            if status in ["Diterima", "Ditolak"]:
                break
            print("Status tidak valid. Masukkan 'Diterima' atau 'Ditolak'.")

        # Tambahkan data ke sheet Seleksi
        seleksi_sheet = cekApakahAdaExcel(workbook, 'Seleksi', ['Kode Pelamar', 'Nama', 'Posisi', 'Status Seleksi'])
        seleksi_sheet.append([kode_pelamar, pelamar_dipilih[1], posisi_pilihan, status])
        workbook.save(FILE_NAME)
        print(f"Pelamar {pelamar_dipilih[1]} berhasil diperbarui ke seleksi dengan status '{status}'\n.")
