# Imagen base ligera con Python 3.12
FROM python:3.12-slim

# Establece /code como directorio de trabajo dentro del contenedor.
# A partir de aquí, los siguientes comandos se ejecutarán desde esta ruta.
WORKDIR /code

# Copia primero el archivo de configuración del proyecto.
# pyproject.toml contiene, entre otras cosas, las dependencias de la aplicación.
COPY pyproject.toml ./

# Copia el código fuente de la aplicación dentro del contenedor.
COPY app ./app

# Instala el proyecto y sus dependencias definidas en pyproject.toml.
# --no-cache-dir evita guardar la caché de pip y ayuda a reducir
# el tamaño final de la imagen.
RUN pip install --no-cache-dir .

# Documenta que la aplicación utiliza el puerto 8000.
# EXPOSE no publica el puerto automáticamente en el equipo anfitrión.
# Para acceder desde fuera habrá que usar, por ejemplo:
# docker run -p 8000:8000 ...
EXPOSE 8000

# Comando que se ejecutará al arrancar el contenedor.
#
# uvicorn            -> servidor ASGI
# app.main:app       -> módulo app/main.py y objeto FastAPI llamado app
# --host 0.0.0.0     -> permite recibir conexiones desde fuera del contenedor
# --port 8000        -> puerto donde escuchará la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]