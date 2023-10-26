from flask import Flask
app = Flask(__name__)

# Ruta de bienvenida con parámetro y tipo de dato entero.
@app.route('/welcome/<int:control>')
def welcome_control(control=None):
    return f'El número recibido es: {control}'