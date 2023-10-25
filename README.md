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

Con `@app.route('/welcome')`

```python
Bienvenido a la página principal.
```

Con `@app.route('/welcome/<name>')`

```python
Bienvenido a la página principal, Rodrigo.
```

Con `@app.route('/welcome/<int:control>')`

```python
El número recibido es: 20490687.
```

Con `@app.route('/welcome/<name>/<int:control>')`

```python
El número recibido es: 20490687 y el nombre es: Rodrigo Barba.
```
