from flask import Flask, render_template, request, Response, jsonify, redirect,url_for
import database as dbase
from usuario import Usuario

db=dbase.dbConection()

app = Flask(__name__)

#Rutas de la aplicacion
@app.route('/')
def home():
    usuarios = db['usuarios']
    usuariosRecividos = usuarios.find()
    return render_template('index.html', usuarios = usuariosRecividos)

#Metodo POST
@app.route('/usuarios',methods=["post"])
def addUsuario():
    usuarios = db['usuarios']
    name = request.form['name']
    dni = request.form['dni']
    correo = request.form['correo']
    telefono = request.form['telefono']

    if name and dni and correo and telefono:
        usuario = Usuario(name,dni,correo,telefono)
        usuarios.insert_one(usuario.toDBCollection())
        Response = jsonify({
            'name':name,
            'dni':dni,
            'correo':correo,
            'telefono':telefono
        })
        return redirect(url_for('home'))
    else:
        return NotFound()

#Metodo Delete
@app.route('/delete/<string:usuario_name>')
def delete(usuario_name):
    usuarios = db['usuarios']
    usuarios.delete_one({'name': usuario_name})
    return redirect(url_for('home'))

#Metodo PUT
@app.route('/edit/<string:usuario_name>', methods=['POST'])
def edit(usuario_name):
    usuarios = db['usuarios']
    name = request.form['name']
    dni = request.form['dni']
    correo = request.form['correo']
    telefono = request.form['telefono']

    if name and dni and correo and telefono:
        usuarios.update_one({
            'name': usuario_name,
        },
        {
            '$set':{
                'name':name,
                'dni':dni,
                'correo':correo,
                'telefono':telefono
            }
        })
        response = jsonify({'message':'Usuario '+ usuario_name+' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return NotFound()



@app.errorhandler(404)
def NotFound(error=None):
 message={
    'message':'No encontrado '+request.url,
    'status':'404 Not Found'
 }
 response = jsonify(message)
 response.status_code= 404
 return response

if __name__ == '__main__':
    app.run(debug=True,port=4000)




