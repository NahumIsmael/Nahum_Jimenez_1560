import xlrd
from xlrd import open_workbook,cellname
from Arrays3 import Array3D

rains = Array3D(32,12,35)

for year in range (1985,2020):
    
    excel = xlrd.open_workbook(filename="./Precipitacion/"+str(year)+'Precip.xls')
    sheet = excel.sheet_by_index(0)

    for state in range (sheet.nrows):

        if state >1 and state <34:

            for month in range (sheet.ncols):
                

                if month >0 and month <13:
                    dato = sheet.cell_value(state,month)
                    rains.set_item(state-2,month-1,year-1985,dato)
def main():
    i=1
    while(True):
        year = int(input("\nIngrese el año a consultar entre 1985-2019: "))
        state = int(input("Ingrese el estado a consultar entre 1-32: "))
        month = int(input("Ingrese el mes a consultar entre 1-12: "))
        print(f"El promedio de lluvia fue de: {rains.get_item(state-1, month-1, year-1985)}")
        i = int(input("\n¿Que quieres hacer? Salir [0] Nueva Consulta [1]\n"))
        if (i == 0):
            break
main()

