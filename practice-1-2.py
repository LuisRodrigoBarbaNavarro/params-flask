from flask import Flask
app = Flask(__name__)

# Ruta de bienvenida con parámetro.
@app.route('/welcome/<name>')
def welcome_name(name=None):
    return f'Bienvenido a la página principal, {name}.'