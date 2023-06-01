#LIBRERIAS

# pypi.org
# Para crear un entorno virtual uso el comando python -m venv nombreDelEntorno en el terminal fuera de todos los archivos, si estamos en mac o linux python3.11 -m venv nombreDelEntorno 

#para activar el entorno virtual usamos el comando 
# source nombreDelArchivo/Scripts/activate esto es para Windows, si es cmd  o powershell no va el source
# source nombreDelArchivo/bin/activate para linux o MAC

# para saber que esta funcionando saldra entre ( nombreDelEntorno)

#Luego de activar el entorno virtual, instalamos la librería

#pip install camelcase para Windows
#pip3.11 install camelcase para MAC o Linux

from camelcase import CamelCase

camel = CamelCase()

texto = 'hola desde el back'

print(camel.hump(texto))

# para eliminar la libreria se escribe en la terminal pip uninstall camelcase y luego y de yes
# si quiero desacticar el entorno escribo deactivate