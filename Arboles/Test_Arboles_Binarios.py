from Arboles_Binarios import NodoArbol

def main():
    
    #Arbol Inicial ABC
    root = NodoArbol("A",NodoArbol("B"),NodoArbol("C"))
    #Arbol Mediano ABCDIJ (Nodo D)
    root.left.left = NodoArbol("D",NodoArbol("I"),NodoArbol("J"))
    #Arbol Grande ABDFIJKL (Nodo F)
    root.left.right = NodoArbol("F",NodoArbol("K"),NodoArbol("L"))
    #Noco C, en una sola linea
    root.right = NodoArbol("C",NodoArbol("G"),NodoArbol("H",NodoArbol("M",None,NodoArbol("N",NodoArbol("O")))))
    print("    ",root.data)
    print(root.left.data,"       ",root.right.data)
    print(root.right.right.left.right.left.data)
    #Solo la hoja de la extrema izquierda
    print(root.left.left.left.data)
    #Solo la hoja de la extrema izquierda sin conocer la profundidad
    curr_node = root
    while curr_node.left != None:
        curr_node = curr_node.left
    print(curr_node.data)
    #Ambos nodos del nodo padre de la extrema derecha (No se conoce profundidad)
    curr_node = root
    while curr_node.right != None:
        curr_node = curr_node.right
    print(f"izq:{curr_node.left.data} der:{curr_node.right}")
        
main()
