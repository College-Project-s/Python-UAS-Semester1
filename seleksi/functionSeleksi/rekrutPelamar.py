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

    sheet_lowongan = workbook['Lowongan']
    sheet_pelamar = workbook['Pelamar']

    # Filter posisi yang dibuka dan memiliki pelamar
    posisi_tersedia = []
    for lowongan in sheet_lowongan.iter_rows(min_row=2, values_only=True):
        kode_lowongan, posisi, _, status = lowongan
        if status == 'Dibuka':
            # Cek apakah ada pelamar untuk lowongan ini
            pelamar_untuk_posisi = any(row[3] == posisi for row in sheet_pelamar.iter_rows(min_row=2, values_only=True))
            if pelamar_untuk_posisi:
                posisi_tersedia.append(posisi)

    if not posisi_tersedia:
        print("Tidak ada lowongan yang dibuka dengan pelamar.")
        workbook.close()
        return

    print("\nLowongan yang tersedia dengan pelamar:")
    for posisi in posisi_tersedia:
        print(f"- {posisi}")

    while True:
        posisi_pilihan = input("Masukkan posisi yang ingin dilihat pelamarnya (atau ketik 'CANCEL' untuk kembali): ")

        if posisi_pilihan.upper() == 'CANCEL':
            print("Proses dibatalkan.")
            workbook.close()
            return
        
        if posisi_pilihan in posisi_tersedia:
            break
        print("Posisi tidak valid atau tidak tersedia. Silakan coba lagi.")

    # Tampilkan daftar pelamar berdasarkan posisi yang dipilih
    pelamar_terpilih = [
        (row[0], row[1])  # Kode Pelamar dan Nama
        for row in sheet_pelamar.iter_rows(min_row=2, values_only=True)
        if row[3] == posisi_pilihan
    ]

    print(f"\nDaftar pelamar untuk posisi {posisi_pilihan}:")
    for kode, nama in pelamar_terpilih:
        print(f"- {kode}: {nama}")

    while True:
        kode_pelamar = input("Masukkan kode pelamar yang ingin diproses (atau ketik 'CANCEL' untuk kembali): ")
        if kode_pelamar.upper() == 'CANCEL':
            print("Proses dibatalkan.")
            workbook.close()
            return
        
        pelamar_dipilih = next((pelamar for pelamar in pelamar_terpilih if pelamar[0] == kode_pelamar), None)
        if pelamar_dipilih:
            break
        print("Kode pelamar tidak valid. Silakan coba lagi.")

    while True:
        status = input("Masukkan status seleksi (Diterima/Ditolak): ")
        if status in ["Diterima", "Ditolak"]:
            break
        print("Status tidak valid. Masukkan 'Diterima' atau 'Ditolak'.")

    seleksi_sheet = cekApakahAdaExcel(workbook, 'Seleksi', ['Kode Pelamar', 'Nama', 'Posisi', 'Status Seleksi'])
    seleksi_sheet.append([kode_pelamar, pelamar_dipilih[1], posisi_pilihan, status])
    workbook.save(FILE_NAME)
    workbook.close()
    print(f"Pelamar {pelamar_dipilih[1]} berhasil diperbarui ke seleksi dengan status '{status}'.")
