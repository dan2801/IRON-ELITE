@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Crea el entorno virtual e instala las dependencias siguiendo el README.
  exit /b 1
)
".venv\Scripts\python.exe" -m flask --app backend.app run --host 0.0.0.0 --port 5000
