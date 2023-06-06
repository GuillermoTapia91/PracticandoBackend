#inicios_flask.py
from flask import Flask,request

# indicar si nuestro archivo es el archivo principal, si el archivo es el principal su valor sera '__main__'
app = Flask(__name__)

productos = [
    {
      
      'nombre': 'Platano',
      'precio':3.50
    },
    {
      
      'nombre': 'Sandia',
      'precio':2.80
    },
    {
      
      'nombre': 'Tomate',
      'precio':2.30
    }
]

# decorador @app.route('/')
@app.route('/') #despues del decorador siempre va una función
def inicio():
   print('hola')
   return 'Welcome to my flask app'

@app.route('/productos', methods=['GET','POST'])
def gestionarProductos():
    print(request.method)

    if request.method == 'GET':
        
      return{
          'content' :productos
      }
    
    elif request.method == 'POST':
       print(request.get_data())#get_json() convierte la data entrante a diccionario
       data =request.get_json()
       productos.append(data)
       return {
          'message' : 'Producto creado existosamente'
       }

@app.route('/producto/<int:id>',methods=['GET','PUT','DELETE'])
def producto(id):
   limite =len(productos)
   if limite < id :
      return {
         "message":"Este producto no existe"
      }
   elif request.method == 'GET':
      return {
         "content":productos[id-1]
      }
   elif request.method == 'PUT':
      data = request.get_json()
      productos[id-1] = data
      return {
         "message": "El producto se actualizo exitosamente"
      }
   elif request.method == 'DELETE':
      del productos[id-1]
      return {
         "message":"El producto fue eliminado exitosamente"
      }

if __name__ == '__main__':
    app.run(debug=True) 
    # para que se actualice los cambios automaticamente se escribe debug=true, ya no se necesario dar control +c