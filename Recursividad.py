def SumaLista (Lista):
    
    tamaño = len(Lista)
    aux = 0
    
    for elem in range (tamaño):
        aux = Lista[0]

        if tamaño > 1:
            Lista.pop(0)
            return SumaLista(Lista) + aux
        
        elif tamaño == 1:
            print('Suma Total: ')
            return aux
        
def main():
    print(SumaLista([1,2,3,4]))
main()    
