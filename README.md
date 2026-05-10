# Biblioteca Universal — Proyecto Flask

JSON original: https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json

Modificaciones realizadas sobre el JSON original:
- Campo "id": numero unico para identificar cada libro
- Campo "genre": genero literario de cada obra
- Campo "rating": valoracion del libro sobre 5

---

## Estructura del proyecto

```
libros/
├── app.py
├── books.json
├── requirements.txt
├── Procfile
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── libros.html
    ├── detalle.html
    └── 404.html
```

---

## Descripcion de los archivos

**app.py**
Archivo principal de Flask. Contiene las cuatro rutas de la aplicacion:
- / : pagina principal
- /libros : listado con busqueda y filtros
- /libro/<id> : detalle de un libro concreto
- Error 404 personalizado si el libro no existe

**books.json**
Conjunto de datos con los 100 mejores libros de la historia. Modificado para añadir los campos id, genre y rating.

**templates/base.html**
Plantilla base de la que heredan todas las demas. Incluye la cabecera, el pie de pagina y los bloques "titulo" y "contenido".

**templates/index.html**
Pagina principal. Muestra una imagen representativa que al hacer clic lleva al catalogo.

**templates/libros.html**
Pagina de busqueda y listado.

**templates/detalle.html**
Pagina de detalle de un libro. Muestra toda la informacion del libro seleccionado y un enlace para volver al catalogo.

**templates/404.html**
Pagina de error personalizada que se muestra cuando el libro no existe.

**static/style.css**
Hoja de estilos de la aplicacion.


---

## Despliegue en Render

1. Crear cuenta en https://render.com
2. New -> Web Service
3. Conectar el repositorio de GitHub
4. Create Web Service
5. Render proporciona una URL publica para acceder a la aplicacion, en mi caso es esta https://biblioteca-flask-2p1h.onrender.com
