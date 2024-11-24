from moduleExcel import FILE_NAME, cekApakahAdaExcel, os, openpyxl

def functionTampilKandidatDiterima():
    if not os.path.exists(FILE_NAME):
        print("File data rekrutmen tidak ditemukan.")
        return

    workbook = openpyxl.load_workbook(FILE_NAME)
    if 'Seleksi' not in workbook.sheetnames:
        print("Sheet Seleksi belum ada.")
        return

    sheet = workbook['Seleksi']
    print("\nDaftar Kandidat Diterima:")
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[3] == "Diterima":
            print(row)
    workbook.close()