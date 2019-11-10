class NodoArbol:
    def __init__ (self,value,izquierdo=None,derecho=None):
        self.data=value
        self.left=izquierdo
        self.right=derecho

#Proximamente aqui... arboles binarios... gran estreno!!!!

class ArbolBinarioBusqueda:
    def __init__ (self):
        self.__root = None

    def insert(self,value):
        if self.__root == None:
            self.__root = NodoArbol(value)
        else:
            self.__inserta_nodo(self.__root,value)

    def __inserta_nodo(self,nodo,value):
        if nodo.data == None:
            return False     #Ya existe
        elif value < nodo.data:
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            else:
                return self.__inserta_nodo(nodo.left,value)
        elif value > nodo.data:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                return self.__inserta_nodo(nodo.right,value)
        else:
            print("Sin repetir crack")
            
    def transversal(self,formato = 'inorden'):
        if formato == 'inorden':
            self.__inorden(self.__root)
        elif formato == 'preorden':
            self.__preorden(self.__root)
        elif formato == 'posorden':
            self.__posorden(self.__root)

    def __inorden(self,nodo):
        if nodo != None:
            self.__inorden(nodo.left)
            print(nodo.data)
            self.__inorden(nodo.right)

    def __posorden(self,nodo):
        if nodo != None:
            print(nodo.data)
            self.__inorden(nodo.left)
            self.__inorden(nodo.right)

    def __preorden(self,nodo):
        if nodo != None:
            self.__inorden(nodo.left)
            self.__inorden(nodo.right)
            print(nodo.data)

    def search(self,value):
        if self.__root == None:
            return False ##Arbol vacio
        else:
            return self.__search_node(self.__root,value)

    def __search_node(self,nodo,value):
        if nodo == None:
            return False
        elif nodo.data == value:
            print('Encontrado')
            return nodo
        elif value < nodo.data:
            print("Busca Izquierda")
            return self.__search_node(nodo.left,value)
        elif value > nodo.data:
            print("Busca Derecha")
            return self.__search_node(nodo.right,value)
        
