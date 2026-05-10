import json
import os
from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Cargamos los libros desde el JSON al arrancar la app
def cargar_libros():
    ruta = os.path.join(os.path.dirname(__file__), 'books.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

LIBROS = cargar_libros()


@app.route('/')
def index():
    """Página principal con logo de bienvenida."""
    return render_template('index.html')


@app.route('/libros')
def libros():
    """Listado de libros con búsqueda y filtros."""
    # Recogemos los parámetros del formulario (GET)
    busqueda = request.args.get('busqueda', '').strip()
    genero   = request.args.get('genero', '')
    orden    = request.args.get('orden', 'asc')

    # Sacamos todos los géneros únicos para el <select>
    todos_generos = sorted(set(libro['genre'] for libro in LIBROS))

    # Filtramos según lo que haya escrito el usuario
    resultado = LIBROS

    if busqueda:
        resultado = [
            l for l in resultado
            if busqueda.lower() in l['title'].lower()
            or busqueda.lower() in l['author'].lower()
        ]

    if genero:
        resultado = [l for l in resultado if l['genre'] == genero]

    # Ordenamos por título
    resultado = sorted(resultado, key=lambda l: l['title'].lower(),
                       reverse=(orden == 'desc'))

    return render_template(
        'libros.html',
        libros=resultado,
        todos_generos=todos_generos,
        busqueda=busqueda,
        genero=genero,
        orden=orden,
        total=len(resultado)
    )


@app.route('/libro/<int:libro_id>')
def detalle(libro_id):
    """Detalle de un libro concreto. Si no existe → 404."""
    libro = next((l for l in LIBROS if l['id'] == libro_id), None)
    if libro is None:
        abort(404)
    return render_template('detalle.html', libro=libro)


@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
