@echo off
REM Crear entorno virtual para RAG con Gemini
echo Creando entorno virtual...
python -m venv venv

REM Activar el entorno
call venv\Scripts\activate.bat

REM Instalar dependencias
echo Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ======================================
echo Entorno configurado correctamente!
echo ======================================
echo.
echo Para activar el entorno en el futuro, ejecuta:
echo   venv\Scripts\activate.bat
echo.
echo Para desactivar el entorno:
echo   deactivate
echo.
echo Para ejecutar Jupyter:
echo   jupyter notebook
echo.
pause
