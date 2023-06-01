#clases con constructores def __init__
class Persona:
    def __init__(self,nombre,nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    
    def saludar(self):
        print(f'Hola soy {self.nombre} y soy {self.nacionalidad}')

persona1 = Persona('Alan','peruano')
persona1.saludar()

