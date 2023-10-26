from flask import Flask
app = Flask(__name__)

# Ruta de bienvenida.
@app.route('/welcome')
# Ruta de bienvenida con parámetro.
@app.route('/welcome/<name>')
# Ruta de bienvenida con parámetro y tipo de dato entero.
@app.route('/welcome/<int:control>')
# Ruta con dos parámetros.
@app.route('/welcome/<name>/<int:control>')
def welcome_name_control(name=None, control=None):
    if name == None and control == None:
        return 'Bienvenido a la página principal.'
    elif name == None:
        return f'El número recibido es: {control}'
    elif control == None:
        return f'Bienvenido a la página principal, {name}.'
    else:
        return f'El número recibido es: {control} y el nombre es: {name}'