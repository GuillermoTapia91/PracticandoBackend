# FUNCIONES
# def nombreFuncion(parametro1,parametro2):
      # return parametro1 + parametro2

def sumar(numero1,numero2):
    resultado = numero1 + numero2
    # print(resultado)
    return resultado

sumar(1 , 2)

def restar(num1, num2):
    return num1-num2

print(restar(5,4))

def saludar():
    print('HOLA')

saludar()

sumatoria = sumar(2,3)
print(sumatoria)

#si quiero tener parametros ilimitados uso *args dentro del (*args) o cualquier palabra *varios
def sumarIlimitado(numero3,*args,numero2):
    print(args)

# el primer valor sera del numero2, todo los demas de *args, y si coloco numero2=x
sumarIlimitado(2,1,3,4,5,6,7,8, numero2=10)

sumarIlimitado(2, 3,4,5,6,7,8,9,1,2, numero2=11)

#Si quiero recibir ilimitados valores con su nombre de parametro se usa **kwargs, esa info
# se almacenara en un diccionario

def valores(**kwargs):
    print(kwargs)

valores(num1 =10, nombre = 'Eduardo', nacionalidad = 'peruano', muerto = False)

def todoIlimitado(*args, **kwargs):
    print(args)
    print(kwargs)

todoIlimitado(10,'hola', True, marca = 'nike')

