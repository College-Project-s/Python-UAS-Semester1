import openpyxl
import os

FILE_NAME = 'data_rekrutmen.xlsx'

# Fungsi untuk membuat sheet jika belum ada
def cekApakahAdaExcel(workbook, sheet_name, header=None):
    if sheet_name not in workbook.sheetnames:
        sheet = workbook.create_sheet(sheet_name)
        if header:
            sheet.append(header)
    return workbook[sheet_name]
