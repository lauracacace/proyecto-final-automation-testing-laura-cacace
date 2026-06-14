# Framework de Automatización - Proyecto Final

Proyecto: framework de testing en Python que incluye pruebas UI (Selenium) y API (requests), organizado con Page Object Model y pytest.

Requisitos
- Python 3.8+
- Instalar dependencias listadas en `requirements.txt`

Instalación (Windows - PowerShell):

```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Instalación (Windows - CMD):

```cmd
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Estructura del proyecto
- `src/pages/` - Page Objects (POM)
- `src/utils/` - utilidades (CSV reader, API client)
- `tests/` - casos de prueba (marcados `ui` o `api`)
- `data/` - datos de prueba (CSV)
- `reports/` - reportes HTML, logs y capturas

Ejecutar pruebas

- Ejecutar solo pruebas UI (headless):

```powershell
# $env:HEADLESS='1'  # opcional para headless
& .\venv\Scripts\python.exe -m pytest -m ui
```

- Ejecutar solo pruebas API:

```powershell
& .\venv\Scripts\python.exe -m pytest -m api
```

- Ejecutar toda la suite y generar reporte HTML:

```powershell
& .\venv\Scripts\python.exe -m pytest -q --html=reports/report.html --self-contained-html
```

Marcadores pytest usados
- `ui` — pruebas de interfaz (Selenium)
- `api` — pruebas de API (requests)

Datos de prueba
- `data/users.csv` contiene usuarios para el test de login (parametrizado).

Reportes y artefactos
- Reporte HTML: `reports/report.html`
- Capturas: `reports/screenshots/` (guardadas cuando un test UI falla)
- Logs: `reports/logs/execution.log`

Notas sobre APIs
- Las pruebas de API usan por defecto JSONPlaceholder (no requiere API key).
- Si prefieres usar ReqRes con clave, ajusta `APIClient` en `src/utils/api_client.py` y agrega el header `x-api-key`.
