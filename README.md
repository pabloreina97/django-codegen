# Django Codegen

**Django Codegen** es un generador de código automático para proyectos Django, diseñado para facilitar la creación de modelos, serializers, viewsets y URLs. Utiliza la API de OpenAI para generar estos componentes a partir de entradas proporcionadas por el usuario.

## Características

- Genera modelos Django a partir de nombres y campos proporcionados por el usuario, o automáticamente si se deja en blanco.
- Crea serializers, viewsets y URLs con el formato adecuado para integrarse en un proyecto Django.
- Organiza los archivos generados en carpetas (`models`, `serializers`, `viewsets`, `urls`) dentro de un directorio de salida.

## Requisitos

- Python 3.7 o superior
- Una clave de API de OpenAI

## Instalación

### 1. Clona el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd django-codegen
```

### 2. Instala las dependencias

Crea un entorno virtual y activa el entorno:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

Instala las dependencias listadas en `pyproject.toml` o `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configura la clave de la API de OpenAI

Añade la clave de API de OpenAI en tus variables de entorno. Puedes hacer esto en tu terminal:

```bash
export OPENAI_API_KEY="tu_clave_openai"  # Linux/Mac
$env:OPENAI_API_KEY="tu_clave_openai"  # Windows
```

### 4. Instala el paquete

Construye el paquete e instálalo de forma local:

```bash
python -m build
pip install dist/django_codegen-0.1.0-py3-none-any.whl
```

## Uso

1. **Ejecuta el generador**:
   Una vez instalado, puedes ejecutar el generador con:

   ```bash
   django_codegen
   ```

2. **Sigue las instrucciones**:
   El generador te pedirá que ingreses el nombre de cada modelo y sus campos:
   - Para cada modelo, introduce el nombre y los campos separados por comas (por ejemplo, `nombre:CharField, edad:IntegerField`).
   - Si prefieres que los campos se generen automáticamente, déjalo en blanco.

3. **Archivos generados**:
   - Los archivos generados se guardarán en un directorio `output/` en la raíz del proyecto, con subdirectorios (`models`, `serializers`, `viewsets`, `urls`).
   - Copia los archivos a las carpetas correspondientes de tu proyecto Django para integrarlos.

## Contribuir

Si quieres contribuir a este proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m "Añade nueva funcionalidad"`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

# TODOs

- Generar urls.py a partir de los modelos. Todo debería estar en un archivo
- Generar archivo generico. Es decir, que si yo le digo: Crea algunos permisos en permissions.py, automáticamente me genere ese archivo, con los permisos.