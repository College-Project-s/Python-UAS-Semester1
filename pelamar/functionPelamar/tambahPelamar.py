from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl

# Function untuk menambah pelamar
def functionTambahPelamar():
    nama = input("Masukkan nama pelamar: ")
    kontak = input("Masukkan kontak pelamar: ")
    posisi = input("Masukkan posisi yang dilamar: ")

    if not os.path.exists(FILE_NAME):
        workbook = openpyxl.Workbook()
    else:
        workbook = openpyxl.load_workbook(FILE_NAME)

    sheet = cekApakahAdaExcel(workbook, 'Pelamar', ['Kode Pelamar', 'Nama', 'Kontak', 'Posisi Dilamar'])
    kode = f"P{sheet.max_row:03d}"
    sheet.append([kode, nama, kontak, posisi])
    workbook.save(FILE_NAME)
    print("Pelamar berhasil ditambahkan.")