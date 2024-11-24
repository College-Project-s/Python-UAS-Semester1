from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menampilkan lowongan
def functionTampilLowongan():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Lowongan' not in workbook.sheetnames:
        print("Sheet Lowongan belum ada.")
        return

    sheet = workbook['Lowongan']
    if sheet.max_row == 1:
        print("Belum ada data lowongan.")
        return

    print("\nDaftar Lowongan:")
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(row)
    workbook.close()
