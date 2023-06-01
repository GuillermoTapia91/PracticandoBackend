#03-operadores.py 

#operadores Aritmeticos
edad1 = 10
edad2 =30
#suma ( + )
print(edad1 + edad2)

#resta( - )
print(edad1 - edad2)

#Multiplicación( * )
print(edad1 * edad2)

#División( / ) resultado con flotante
print(edad1 / edad2)

#Modulo ( % )
print(edad1 % edad2)

#Cociente ( // ) resultado solo parte entera de las divisón
print(edad1 // edad2)

#Operadores Asignación
#Asiganación( = )
persona = 'Ximena'

#Incremento
edad1 += 1 #incrementamos el valor de la variable edad1 en una unidad

#Decremento
edad1 -= 1

# Multiplicador
edad1 *= 2 #edad1 = edad1 * 2

#Division
edad1 /= 2

#Potencia
edad1 **= 3 # edad1 = edad1 * edad1 * edad1

#Operadores Comparacion
persona1 = "Eduardo"
persona2 = "Juan"

# == es igual que
# en python no existe el trople igual ===

print(persona1 == persona2)

# != no es igual que | es diferente de
print(persona1 != persona2)

# < , > menor que | mayor que
print(10 > 20)
print(50 < 80)

# <=, >=
print(10 >=10 )

#Operadores Lógicos
edad_juan = 10
edad_jonathan = 15
edad_roxana = 18
edad_martina = 19
# and (y)
print((edad_jonathan > edad_juan) and (edad_martina > edad_roxana))
print((edad_jonathan > edad_juan) and (edad_roxana > edad_martina))

# or (o)
print((edad_jonathan > edad_juan) or (edad_roxana > edad_martina))
