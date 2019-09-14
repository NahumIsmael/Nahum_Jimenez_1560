class Array:
    def __init__(self, size):
        self.__size = size
        self.__data = []
        for index in range(size):
            self.__data.append(None)

    def length(self):
        return self.__size

    def get_item(self , index):
        if index >= 0 and index < self.__size:
            return self.__data[index]
        else:
            return None

    def set_item(self , index ,valor):
        if index >= 0 and index < self.__size:
            self.__data[index] = valor
        else:
            print("El index fuera de rango")

    def clearing(self, valor):
        for i in range(self.__size):
            self.__data[i] = valor

    def to_string(self):
        print(self.__data)


def main():
    adt = Array(10)
    adt.to_string()
    print(f"El tamaño del arreglo es {adt.length()}")
    adt.set_item(0,5)
    adt.to_string()
    print(f"El elemento 0 es {adt.get_item(0)}")
    adt.clearing(50)
    adt.to_string()

main()
