#encapsulamiento atributos y metodos privados
class Producto:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio

        #para crear un atributo privado es decir que no pueda moficarlo atravez de una instancia se le pone self.__atributo
        self.__ganancia = self.precio * 0.3
    #para crear un metodo privado es decir que no pueda usarlo atravez de una instancia se le pone self.__atributo, se puede usar siempre y cuando este dentro de un metodo publico, y lo llamaría atravez del merodo publico    
    def __mostrarIgv(self):
        return self.__ganancia * 0.18
    def mostrarGanancia(self):
        print(f'La ganancia es {self.__ganancia} y el igv es {self.__mostrarIgv()}')

producto1 = Producto('huevo',0.5)
producto1.mostrarGanancia() 