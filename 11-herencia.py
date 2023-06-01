# Herencia cuando clases hereda a otra clase class clase2(clase1) clase1 es la clase padre de la clase2
class Usuario:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print(f'Hola soy {self.nombre} {self.apellido} ')

class Alumno(Usuario):
    def __init__(self, nombre, apellido,dni):
        super().__init__(nombre, apellido)
        self.dni = dni

    def saludar2(self):
        print(f'Hola soy {self.nombre} {self.apellido} y mi dni es {self.dni}')

alumno1 = Alumno('Daniel','Paredes',1234567)
alumno1.saludar2()




