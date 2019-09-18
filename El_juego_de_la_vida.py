#El juego de la vida
"""del tipo Zero-player
creado por john h. conway(1970)
ejemplifica, el ascenso, caida y alternancia de seres vivos

Reglas:
1.- si una celula esta viva y tiene dos o 3 vecinos vivos, la celula sobrevive a
    la siguiente generacion. Los vecinos son las 8 celulas que la rodean inmediatamente
    tanto en vertical, horizontal, diagonal
    
2.- una celula que no tiene vecinos vivos o que tiene un solo vecino vivo, muere por
    soledad para la siguiente generacion
    
3.- una celula viva que tiene 4 o mas vecinos vivos, muere por sobrepoblacion para la
    siguiente generacion
    
4.- una celula muerta con exactamente 3 vecinos resulta en un nacimiento cuya vida
    empezara en la siguiente generacion. Todas las celulas muertas restantes se mantienen
    muertas la siguiente generacion
"""

from Arrays2 import Array2D

# 0 --> muerta
# 1 --> viva

class SoporteVida:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__gens = 0
        self.__grid = Array2D(rows, cols)
        self.__grid.clearing(0)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def configure(self, inicial, generaciones):
        self.__gens = generaciones
        for cell in inicial:
            self.__grid.set_item(cell[0],cell[1],1)
        
    def to_string(self):
        self.__grid.to_string()

    def clear_cell(self, row, col):
        self.__grid.set_item(row,col,0)

    def set_cell(self, row, col):
        self.__grid.set_item(row,col,1)

    def is_alive_cell(self, row, col):
        if self.__grid.get_item(row,col) ==1:
            return True
        else:
            return False

    def get_alive_neighbors(self,row,col):
        limites = self.__calcula_vecinos(row,col)
        vivos = 0
        for r in range(limites[2],limites[3]+1,1):
            for c in range(limites[0],limites[1],1):
                if self.__grid.get_item(r,c) == 1:
                    vivos +=1
        return vivos
        
    def __calcula_vecinos(self, ren, col):
        x_ini = col-1
        x_fin = col +1
        y_ini = ren-1
        y_fin = ren+1
        if col ==0:
            x_ini = 0
        if col == self.__cols-1:
            x_fin = self.__cols-1
        if ren == 0:
            y_ini = 0
        if ren== self.__rows -1:
            y_fin = self.__rows -1

        return [x_ini,x_fin,y_ini,y_fin]

def main():
    juego = SoporteVida(6,6)
    juego.configure([[1,2],[2,1],[2,2],[2,3]],5)
    juego.to_string()
    print(f"Celulas vivas: {juego.get_alive_neighbors(1,1)}")

main()
