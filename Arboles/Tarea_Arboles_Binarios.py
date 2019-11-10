from Arboles_Binarios import NodoArbol

def main():
    
    #Arbol creado a partir de una sola linea
    root = NodoArbol("10",NodoArbol("20",NodoArbol("30",None,NodoArbol("40",NodoArbol("50"),NodoArbol("60",None,NodoArbol("70",NodoArbol("80")))))))
    print("-----Arbol Binario-----")
    print("    ",root.data)
    print("    /")
    print(" ",root.left.data)
    print(" /")
    print(root.left.left.data)
    print('  \\')
    print("  ",root.left.left.right.data)
    print("  /",'  \\')
    print(root.left.left.right.left.data,"   ",root.left.left.right.right.data)
    print('         \\')
    print("         ",root.left.left.right.right.right.data)
    print("\t /")
    print("      ",root.left.left.right.right.right.left.data)
    print("-----------------------")
    
main()
