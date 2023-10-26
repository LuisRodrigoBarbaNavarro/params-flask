from flask import Flask
app = Flask(__name__)

# Ruta de bienvenida.
@app.route('/welcome')
def welcome():
    return 'Bienvenido a la página principal.'