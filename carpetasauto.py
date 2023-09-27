import os
import calendar

desktop = "C:/Users/ACER NITRO 5/Desktop"

months_folder = "Meses Del Año"
months_folder_path = os.path.join(desktop, months_folder)
os.makedirs(months_folder_path) # Crear carpeta madre

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for month in months:
    month_path = os.path.join(months_folder_path, month)
    os.makedirs(month_path) # Crear carpeta para el mes
    num_days = calendar.monthrange(2023, months.index(month) + 1)[1] # Obtener número de días en el mes
    for day in range(1, num_days + 1):
        day_path = os.path.join(month_path, str(day))
        os.makedirs(day_path) # Crear carpeta para el día