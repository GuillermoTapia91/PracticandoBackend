#listas (arrays)
#Es una coleccion de datos lineal,es decir ordenada
#ordenada: puedo acceder a sus elementos mediante su posición

meses = ['enero','febrero','marzo']
mezclada = ['Guillermo', 10, 100, 50.2, 45.6, True, False]

print(mezclada)
#Para acceder a los elementos de la lista se escribe el nombre de la lista y entre corchetes la posición del elemento

#para enero sería
print(meses[0])

# si quiero empezar desde la última posición utilizo números negativos
#Para imprimir marzo
print(meses[-1])

print(meses[1:3])
print(meses[:2])
print(meses[1:])

#Para agregar elementos uso .append(elemento) y agrega al final
meses.append('abril')
print(meses)

#para borrar un elemento por nombre uso .remove(elemento)
meses.remove('enero')
print(meses)

#para borrar un elemento por posicion uso .pop(posicion) y ademas devuelve el valor quitado
mes_eliminado = meses.pop(1)
print(mes_eliminado)
print(meses)

#tambien podamos usar .dell para eliminar variables y contenidos de las listas
del meses[0]
print(meses)

#para saber cuantos elementos tengo en una lista uso len(lista)
print(len(meses))

## DICCIONARIOS
# Es una colección de listas ordenadas mediante llaves y valores dic1 = {'llave1' : valor1, 'llave2': valor2, etc } . La llave siemrpe debe ser un string

persona = {
    'nombre':'Juan',
    'edad' : 80,
    'nacionalidad' : 'Peruano',
    'soltero' : True,
    'estatura': 1.92
}

# para entrar a un dic usamo las llave como posiciones dic1['llave1']
print(persona['nombre'])

# si quiero agregar  un elementos mas dic1['llave'] = valor
persona['fecha_nacimiento'] = 'agosto del 1970'

# si se quiere reemplazar un valor existente dic1['llave] = nuevaValor
persona['nombre'] = "Roberto"

print(persona)
#Para imprimir todas las llaves de un dic
print(persona.keys())
#Para imprimir todos los valores de un dic
print(persona.values())
#Para borra un elemento de un dic, uso del dic1['llave']

del persona['edad']
print(persona)

# Conjuntos
# es una coleccion de datos desordenados, no se puede entrar a sus elementos
#una vez credad no se podra acceder a sus elementos
# conjunto1 = { elemento1, elemento2}

alumnos = { 'Eduardo', 'María', 'Luisa', 'Dante'}
#Para agregar elementos a un conjunto se usa .add(elementoNuevo)
alumnos.add('Roberto')
#para borrar elementos de un conjunto se usa .remove(elemento)
alumnos.remove('Eduardo')
print(alumnos)

# Si se quiere saber si elemento está o no uso in
print('Eduardo' in alumnos)

#Tuplas
# Es una coleccion de datos que una vez creada no se puede modificar tupla1 = (e1,e2,e3)
# no se puede agregar ni eliminar valores
conocimientos = ('Matematica', 'Comunicación','Backend')