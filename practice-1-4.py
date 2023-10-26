from flask import Flask
app = Flask(__name__)

# Ruta con dos parámetros.
@app.route('/welcome/<name>/<int:control>')
def welcome_name_control(name=None, control=None):
    return f'El número recibido es: {control} y el nombre es: {name}'