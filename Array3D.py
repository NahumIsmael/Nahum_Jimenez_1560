class Array3D:
    def __init__ (self,rows,cols,depth):
        self.__rows = rows
        self.__cols = cols
        self.__depth = depth
        self.__data = []

        for i in range(self.__depth):
            aux=[]
            for j in range(self.__rows):
                aux2=[]
                for x in range(self.__cols):
                   aux2.append(0)
                aux.append(aux2)
            self.__data.append(aux)

    def to_String(self):
        print(self.__data)
 
    def get_num_rows(self):
        return(self.__rows)

    def get_num_cols(self):
        return(self.__cols)

    def get_num_depth(self):
        return(self.__depth)

    def set_item(self,rows,cols,depth,value):
        self.__data[depth][rows][cols] = value

    def clearing(self,value):
        for i in range (self.__depth):
            for j in range(self.__rows):
                for x in range(self.__cols):
                   self.__data[i][j][x] = value

    def get_item(self,rows,cols,depth):
        return self.__data[depth][rows][cols]

def main():
"""    
    a3d = Array3D(4,3,2)
    a3d.to_String()
    print(a3d.get_num_rows())
    a3d.clearing('EASY')
    a3d.to_String()
"""
main()

"""
import xlrd
for anio in range(1985,1019,1):
   archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
   hoja=archivo.sheet_by_index(0)
   ##leer mes de enero primer estado
   print(hoja.cell_value(2,1))
"""

