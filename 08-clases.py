#clases

class Persona:
    # las variables que creemos dentro de una clase se pasan a llama atributos
    fechaNacimiento = '1990-01-01'
    nombre = ''
    estatura = 1.50

    def saludar(self):
        texto = f"Hola soy {self.nombre}, mucho gusto "
        print(texto)
    
    def despedir(self):
        print("adios")

persona1 = Persona()
persona2 = Persona()

persona1.nombre = 'Rigoberto'
persona2.nombre = 'Derrick'

persona1.saludar()
persona2.saludar()
