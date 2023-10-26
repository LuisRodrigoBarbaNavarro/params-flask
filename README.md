# Práctica 2 I Flask Con Parámetros 🐈

---

### Información Básica ✨

**Nombre:** Barba Navarro Luis Rodrigo

**Fecha (Creación):** 24/10/23

**Descripción:** Este repositorio presenta una aplicación web desarrollada en Flask. Muestra ejemplos de funciones que toman parámetros, lo que permite personalizar la respuesta de la aplicación basándose en la entrada del usuario.

---

### Recursos ✨
!["Código Fuente"](https://i.imgur.com/7dNRhGt.png)

---
### Implementación ✨

Con `@app.route('/welcome')` en `practice-1-1.py`

```python
Bienvenido a la página principal.
```

Explicación: En este caso, cuando un usuario acceda a la ruta '/welcome' en el navegador, la función welcome() se ejecutará y devolverá el texto "Bienvenido a la página principal." como respuesta en el navegador.

Con `@app.route('/welcome/<name>')` en `practice-1-2.py`

```python
Bienvenido a la página principal, Rodrigo.
```

Explicación: En este caso, cuando un usuario acceda a la ruta '/welcome/Rodrigo' en el navegador, la función welcome() se ejecutará y devolverá el texto con el nombre proporcionado "Bienvenido a la página principal, Rodrigo." como respuesta en el navegador.

Con `@app.route('/welcome/<int:control>')` en `practice-1-3.py`

```python
El número recibido es: 20490687.
```

Explicación: En este caso, cuando un usuario acceda a la ruta '/welcome/20490687' en el navegador, la función welcome() se ejecutará y devolverá el texto con el número de control proporcionado "El número recibido es: 20490687." como respuesta en el navegador.

Con `@app.route('/welcome/<name>/<int:control>')` en `practice-1-4.py`

```python
El número recibido es: 20490687 y el nombre es: Rodrigo Barba.
```

Explicación: En este caso, cuando un usuario acceda a la ruta '/welcome/Rodrigo%02Barba/20490687' en el navegador, la función welcome() se ejecutará y devolverá el texto con el nombre y número de control proporcionado concatenado al texto superior "El número recibido es: 20490687 y el nombre es: Rodrigo Barba." como respuesta en el navegador.

Con `practice-1-5.py`

Explicación: Básicamente son las cuatros formas de enrutamiento anteriormente expuestas, y todas hacen llamar la misma función welcome(), sólo que mediante excepciones podemos controlar la forma en la que los parámetros de entrada son manejados; si solamente llega el nombre se proporciona la vista sobre el nombre, caso contrario, solamente llega el número control, se proporciona la vista con el número de control. Lo mismo sucede cuando llegan los dos parámetros juntos o no llega ninguno.

Con `practice-1-6.py`
Explicación: Básicamente, se muestran la clasificación de cuatro diferentes tipos de datos utilizados en Python, donde se hace notorio la aparición de 'None' como un objeto especial de tipo 'NoneType', por lo que esta palabra reservada en si, no significa cero, sino nulo o no disponible.
