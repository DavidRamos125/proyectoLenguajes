@echo off

REM Crear entorno virtual si no existe
if not exist .projectEnv (
    python -m venv .projectEnv
)

REM Activar entorno virtual
call .projectEnv\Scripts\activate

REM Instalar dependencias
pip install -r requirements.txt

pause