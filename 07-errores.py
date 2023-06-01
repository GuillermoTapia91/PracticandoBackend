# ERRORES TRY EXCEPT

try:
    # raise Exception('Error!!!')
    # int('a')
    division = 10/1
    print(division)

except ValueError:
    #Ingresa a este bloque si algo en el try termino de maner abrupta
    print('Error al ejecutar el codigo')

except ZeroDivisionError:
    print('Error al dividir entre 0')

except:
    print('Error desconocido')

# si no entra a ningun excep se ejecuta el else
else:
    print('Yo me ejecuto de manera exitosa')
finally:
    print('Yo me ejecuto si todo estuvo bien o no')
    
print('Soy otro codigo importante en el proyecto')  