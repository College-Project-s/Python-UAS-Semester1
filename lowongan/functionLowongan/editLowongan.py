from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk mengedit lowongan
def functionEditLowongan():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        workbook.close()
        return

    sheet = workbook['Lowongan']

    # Tampilkan data lowongan
    if sheet.max_row == 1:  # Hanya header yang ada
        print("Belum ada data lowongan.")
        workbook.close()
        return

    print("\nDaftar Lowongan:")
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(f"Kode: {row[0]}, Posisi: {row[1]}, Gaji: {row[2]}, Deskripsi: {row[3]}, Status: {row[4]}")

    # Input kode lowongan
    kode = input("\nMasukkan kode lowongan yang ingin diedit (atau ketik 'CANCEL' untuk kembali): ")

    if kode.upper() == 'CANCEL':
        print("Proses mengedit dibatalkan.")
        workbook.close()
        return

    lowongan_ditemukan = False

    for row in sheet.iter_rows(min_row=2):
        if row[0].value == kode:
            lowongan_ditemukan = True
            print(f"Data saat ini: Posisi = {row[1].value}, Gaji = {row[2].value}, Deskripsi = {row[3].value}, Status = {row[4].value}")
            row[1].value = input("Masukkan posisi baru (kosongkan jika tidak ingin mengubah): ") or row[1].value
            row[2].value = input("Masukkan gaji (Per Bulan) baru (kosongkan jika tidak ingin mengubah): ") or row[2].value
            row[3].value = input("Masukkan deskripsi baru (kosongkan jika tidak ingin mengubah): ") or row[3].value
            row[4].value = input("Masukkan status baru (Dibuka/Ditutup, kosongkan jika tidak ingin mengubah): ") or row[4].value
            print("Lowongan berhasil diperbarui.")
            break

    if not lowongan_ditemukan:
        print("Kode lowongan tidak ditemukan.")

    workbook.save(FILE_NAME)
    workbook.close()
