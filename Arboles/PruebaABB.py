from Arboles_Binarios import ArbolBinarioBusqueda

def main():
    
    arbol = ArbolBinarioBusqueda()
    arbol.insert(60)
    arbol.insert(29)
    arbol.insert(73)
    arbol.insert(40)
    arbol.insert(5)
    arbol.transversal()
    print("-+-+-+-+-+")
    arbol.transversal('posorden')
    print("-+-+-+-+-+")
    arbol.transversal('preorden')
    nodo = arbol.search(60)
    if nodo != False:
        print("\t",nodo.data)
        if nodo.left != None:
            print(nodo.left.data,end="")
        if nodo.right != None:
            print("\t\t",nodo.right.data)

main()
