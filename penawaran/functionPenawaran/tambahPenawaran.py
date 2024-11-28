from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl

def functionTambahPenawaran():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)

    # Pastikan sheet Lowongan ada
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        workbook.close()
        return

    # Pastikan sheet Penawaran ada atau buat jika belum
    sheet_penawaran = cekApakahAdaExcel(workbook, 'Penawaran', ['Kode Pekerjaan', 'Benefit'])

    sheet_lowongan = workbook['Lowongan']

    while True:
        # Tampilkan daftar pekerjaan
        print("\nDaftar Pekerjaan yang Tersedia:")
        for row in sheet_lowongan.iter_rows(min_row=2, values_only=True):
            print(f"- Kode: {row[0]}, Posisi: {row[1]}")

        # Input kode pekerjaan
        kode_pekerjaan = input("\nMasukkan kode pekerjaan untuk menambahkan benefit (atau ketik 'CANCEL' untuk keluar): ")

        if kode_pekerjaan.upper() == 'CANCEL':
            print("Proses penambahan benefit selesai.")
            break

        # Validasi kode pekerjaan
        pekerjaan_valid = any(row[0] == kode_pekerjaan for row in sheet_lowongan.iter_rows(min_row=2, values_only=True))
        if not pekerjaan_valid:
            print("Kode pekerjaan tidak valid. Silakan coba lagi.")
            continue

        # Tambahkan benefit
        while True:
            benefit = input("Masukkan benefit untuk pekerjaan ini (atau ketik 'STOP' untuk berhenti menambahkan benefit): ")
            if benefit.upper() == 'STOP':
                break

            # Tambahkan ke sheet Penawaran
            sheet_penawaran.append([kode_pekerjaan, benefit])
            print(f"Benefit '{benefit}' berhasil ditambahkan untuk pekerjaan dengan kode {kode_pekerjaan}.")

    # Simpan workbook setelah selesai
    workbook.save(FILE_NAME)
    workbook.close()
    print("Data penawaran berhasil disimpan.")
