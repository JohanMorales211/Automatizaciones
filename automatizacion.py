import openpyxl

# Crea una nueva hoja de cálculo de Excel
wb = openpyxl.Workbook()

# Selecciona la primera hoja
ws = wb.active

# Escribe los números del 1 al 10 en la hoja
for i in range(1, 11):
    ws.cell(row=i, column=1, value=i)

# Guarda la hoja de cálculo en el escritorio
wb.save("C:\\Users\\ACER NITRO 5\\Desktop\\numeros.xlsx")
