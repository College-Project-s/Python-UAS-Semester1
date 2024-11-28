from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl

# Function untuk menambahkan lowongan
def functionTambahLowongan():
    posisi = input("Masukkan posisi: ")
    deskripsi = input("Masukkan deskripsi: ")
    status = "Dibuka"

    if not os.path.exists(FILE_NAME):
        workbook = openpyxl.Workbook()
    else:
        workbook = openpyxl.load_workbook(FILE_NAME)

    sheet = cekApakahAdaExcel(workbook, 'Lowongan', ['Kode', 'Posisi', 'Deskripsi', 'Status'])
    kode = f"L{sheet.max_row:03d}"
    sheet.append([kode, posisi, deskripsi, status])
    workbook.save(FILE_NAME)
    print("Lowongan berhasil ditambahkan.")
