# Proyecto B · API de avisos de seguridad (FastAPI)

Proyecto didáctico para **UD01-LAB01. Radiografía de proyectos**. Una API de avisos con documentación HTTP automática y almacenamiento de demostración en memoria.

## Reglas del laboratorio

- Trabaja exclusivamente sobre los repositorios facilitados y en tu propio equipo o laboratorio autorizado.
- Para completar el cuestionario Moodle, **identifica los archivos y las líneas de código** que justifican cada respuesta. Este README explica cómo ejecutar la aplicación, pero no sustituye el análisis del código.
- No necesitas modificar el código ni entregar un informe.
- Los datos son de prueba. No publiques esta aplicación en Internet como servicio de producción.

## Preparar y explorar el proyecto

1. Descarga el ZIP del proyecto y extráelo.
2. Abre una terminal **dentro de la carpeta que contiene el archivo principal de dependencias**.
3. Abre la carpeta con VS Code, IntelliJ IDEA u otro editor.
4. Elige **una** de las dos formas de ejecución: local o Docker. No arranques ambas en el mismo puerto simultáneamente.

Los comandos siguientes asumen una terminal de Linux/macOS (o WSL en Windows). `curl` puede ejecutarse en otra terminal mientras el servidor sigue en marcha.

## Requisitos para ejecución local

- **Python 3.11 o superior** (se recomienda Python 3.12) con `pip` y `venv`.
- Comprueba la instalación: `python3 --version` y `python3 -m pip --version`.
- Si en Windows tu instalación usa el lanzador `py`, sustituye `python3` por `py`.

## Opción 1 · Ejecutar en un entorno virtual

Desde la raíz del proyecto, en **Linux/macOS**:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

En **Windows PowerShell**, crea y activa el entorno con:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e '.[test]'
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

No uses `--reload` en producción. Abre `http://localhost:8000/docs` para explorar la documentación interactiva y `http://localhost:8000/openapi.json` para consultar el contrato OpenAPI.

Para detenerlo, pulsa `Ctrl+C`; para salir del entorno virtual, ejecuta `deactivate`.

## Configuración opcional

El proyecto incorpora un archivo de ejemplo de variables de entorno. En Linux/macOS:

```bash
cp .env.example .env
```

En PowerShell usa `Copy-Item .env.example .env`. La ejecución funciona también sin copiarlo, usando los valores predeterminados. Edita `.env` para experimentar con la configuración de la API. El archivo `.env` no debe subirse al repositorio con secretos reales.

## Pruebas automatizadas y construcción

Con el entorno virtual activo:

```bash
pytest -v
python -m pip wheel . --no-deps --wheel-dir dist
```

La segunda instrucción construye una **distribución wheel** en `dist/`. No hace falta generar el wheel para ejecutar la aplicación durante el laboratorio.

## Opción 2 · Ejecutar con Docker

```bash
docker build -t lab01-fastapi .
docker run --rm --name lab01-fastapi -p 8000:8000 lab01-fastapi
```

Desde otra terminal prueba `curl -i http://localhost:8000/health`. El contenedor no incorpora las dependencias opcionales de test. Para detenerlo, `Ctrl+C` o `docker stop lab01-fastapi`.

## Probar la API

| Método | Ruta | Resultado esperado |
| --- | --- | --- |
| GET | `/health` | Estado de la aplicación |
| GET | `/api/notices/` | Listado JSON de avisos |
| GET | `/api/notices/1` | Consulta del aviso 1 |
| POST | `/api/notices/` | Crea un aviso (HTTP 201) |

```bash
curl -i http://localhost:8000/health
curl -i http://localhost:8000/api/notices/
curl -i http://localhost:8000/api/notices/1
curl -i -X POST http://localhost:8000/api/notices/ \
  -H 'Content-Type: application/json' \
  -d '{"title":"Comprobar accesos","severity":"high"}'
```

**Importante:** las rutas de colección terminan en `/`; si omites la barra, FastAPI puede redirigir a la URL canónica. Los valores de gravedad son `low`, `medium` o `high` en **minúsculas**.

## Configuración, datos y almacenamiento

Servidor local en el **puerto 8000**. Los avisos se mantienen en memoria durante la ejecución de cada proceso y se reinician al reiniciar la aplicación; no hay base de datos externa.

## Problemas frecuentes

- **No se encuentra `python3`**: comprueba instalación y `PATH` (o usa `py` en Windows).
- **`uvicorn` o `pytest` no encontrados**: activa `.venv` e instala la opción `[test]`.
- **Error de activación de PowerShell**: utiliza otra terminal o configura su política de ejecución conforme a las normas del centro.
- **Puerto 8000 ocupado**: cambia a `--port 8001` o usa `docker run --rm -p 8001:8000 lab01-fastapi`.
- **HTTP 422 al crear un aviso**: revisa los campos y los valores de `severity`.
