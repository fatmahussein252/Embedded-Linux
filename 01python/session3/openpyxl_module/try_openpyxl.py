import openpyxl

def write_excel_file(path):
    wrkbook=openpyxl.Workbook()
    sht=wrkbook.active
    data=[
        ['name','age','city'],
        ['fatma','22','giza'],
        ['yasmine','25','giza'],
        ['Basant','23','giza']
    ]
    for row in data:
        sht.append(row)

    wrkbook.save(path)
    wrkbook.close()

write_excel_file('session3/openpyxl_module/xlsxtry.xlsx')