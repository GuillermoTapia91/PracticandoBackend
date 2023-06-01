#Sentencias y bucles
nombres = ['Eduardo', 'Julia', 'Raul', 'Pedro']

print(nombres[0])

for nombre in nombres:
    print(nombre)

texto = 'Hola como estas'

for letra in texto:
    print(letra)

# si en el range no le indicamos inicio, empezara desde el 0
for numero in range(10):
    print(numero)

#Se imprime desde 5 hasta 9, menor  10
for numero in range(5,10):
    print(numero)

#Se imprime desde 2 hasta 9 , saltando de 2 en 2
for numero in range(2,20,2):
    print(numero)

mes = 'julio'
while(mes !='agosto'):
    print('no es agosto')
    break

edad = 20
if edad >= 18 :
    print('puede consumir alcohol')
elif edad > 10:
  print('no puede consumir alcohol pero si caramelos')
else:
    ('no pude consumir absolutamente nada')

    