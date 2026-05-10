# 📚 Biblioteca Universal — Proyecto Flask

**JSON original:** https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json  
**Modificaciones realizadas:** Se añadieron tres campos nuevos a cada objeto del JSON:
- `id` → número único para identificar cada libro (necesario para la ruta /libro/ID)
- `genre` → género literario (Novela, Teatro, Poesía, Épica, Cuentos…)
- `rating` → valoración del 1 al 5

---

## 🗂️ Estructura del proyecto

```
biblioteca/
├── app.py              ← Código Python de Flask (rutas y lógica)
├── books.json          ← Datos de los 100 libros (modificado)
├── requirements.txt    ← Dependencias (Flask y Gunicorn)
├── Procfile            ← Para el despliegue (le dice al servidor cómo arrancar)
├── static/
│   └── style.css       ← Estilos CSS
└── templates/
    ├── base.html       ← Plantilla base (cabecera + footer)
    ├── index.html      ← Página principal
    ├── libros.html     ← Listado y búsqueda
    ├── detalle.html    ← Detalle de un libro
    └── 404.html        ← Página de error
```

---

## 🚀 Cómo ejecutarlo en tu ordenador (paso a paso)

### Paso 1 — Instala Python
Descarga Python 3 desde https://python.org si no lo tienes.  
Para comprobar que lo tienes, abre una terminal y escribe:
```
python --version
```

### Paso 2 — Crea un entorno virtual
Un entorno virtual es como una "caja separada" donde instalar las librerías del proyecto sin mezclarlas con el resto de tu ordenador.

En la carpeta del proyecto (donde está app.py), escribe:
```bash
python -m venv venv
```

Luego actívalo:
- En Windows: `venv\Scripts\activate`
- En Mac/Linux: `source venv/bin/activate`

Sabrás que está activo porque el prompt de la terminal pondrá `(venv)` al principio.

### Paso 3 — Instala Flask
Con el entorno activo, instala las dependencias:
```bash
pip install -r requirements.txt
```

### Paso 4 — Arranca la aplicación
```bash
python app.py
```

Verás algo como:
```
 * Running on http://127.0.0.1:5000
```

Abre ese enlace en el navegador y ya funciona.

---

## 📤 Cómo subirlo a GitHub (control de versiones)

### Paso 1 — Crea el repositorio en GitHub
1. Ve a https://github.com → New repository
2. Ponle nombre (ej: `biblioteca-flask`)
3. Deja todo lo demás por defecto → Create repository

### Paso 2 — Sube el código desde la terminal
```bash
git init
git add .
git commit -m "Proyecto inicial: estructura Flask y libros JSON"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/biblioteca-flask.git
git push -u origin main
```

### Ejemplos de mensajes de commit durante el desarrollo
A medida que vayas haciendo cambios, haz commits con mensajes claros:
```bash
git add .
git commit -m "Añadir formulario de búsqueda con filtro por género"

git add .
git commit -m "Añadir página de detalle con manejo de error 404"

git add .
git commit -m "Mejorar estilos CSS: tabla y página principal"
```

---

## ☁️ Cómo desplegarlo en Render (gratis)

Render es una plataforma que ejecuta tu app en internet, gratis.

### Paso 1 — Crea una cuenta
Ve a https://render.com y regístrate (puedes usar tu cuenta de GitHub).

### Paso 2 — Nuevo Web Service
1. En el panel de Render → "New" → "Web Service"
2. Conecta tu repositorio de GitHub
3. Elige el repositorio `biblioteca-flask`

### Paso 3 — Configuración
Render detectará automáticamente Python. Asegúrate de que pone:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Plan:** Free

### Paso 4 — Deploy
Pulsa "Create Web Service". Render tardará 1-2 minutos.  
Al terminar te dará una URL tipo `https://biblioteca-flask.onrender.com`.

---

## 🔗 Rutas de la aplicación

| Ruta | Qué hace |
|------|----------|
| `/` | Página principal con imagen/logo |
| `/libros` | Listado, búsqueda y filtros |
| `/libros?busqueda=tolstoy&genero=Novela&orden=asc` | Búsqueda con parámetros |
| `/libro/27` | Detalle del libro con id=27 |
| `/libro/999` | Devuelve error 404 |

---

## ❓ Preguntas frecuentes del código

**¿Qué es `url_for()`?**  
Es una función de Flask que genera la URL de una ruta a partir de su nombre en Python.  
Así si cambias la ruta, no tienes que cambiar todos los enlaces a mano.

**¿Por qué usamos GET y no POST en el formulario?**  
Con GET, los parámetros de búsqueda van en la URL. Eso permite copiar y compartir la URL con los resultados. Con POST no se podría.

**¿Qué hace `abort(404)`?**  
Le dice a Flask que devuelva el error 404 (no encontrado). Flask llama al manejador `@app.errorhandler(404)` que muestra nuestra página de error personalizada.

**¿Qué es Gunicorn?**  
Es un servidor web más robusto que el de desarrollo de Flask. Solo se usa en producción (cuando la app está en internet). Localmente usamos `python app.py`.
