from moduleExcel import FILE_NAME, os, openpyxl

# Function untuk menampilkan pelamar
def functionTampilPelamar():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Pelamar' not in workbook.sheetnames:
        print("Sheet Pelamar belum ada.")
        return

    sheet = workbook['Pelamar']
    if sheet.max_row == 1:
        print("Belum ada data pelamar.")
        return

    print("\nDaftar Pelamar:")
    for row in sheet.iter_rows(min_row=2, max_col=4, values_only=True):
        print(row)
    workbook.close()