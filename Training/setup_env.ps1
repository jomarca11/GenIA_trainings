# Script para configurar el entorno virtual en PowerShell
# Crear entorno virtual para RAG con Gemini

Write-Host "Creando entorno virtual..." -ForegroundColor Cyan
python -m venv venv

# Activar el entorno
Write-Host "Activando entorno virtual..." -ForegroundColor Cyan
& .\venv\Scripts\Activate.ps1

# Instalar dependencias
Write-Host "Instalando dependencias..." -ForegroundColor Cyan
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "`n======================================" -ForegroundColor Green
Write-Host "Entorno configurado correctamente!" -ForegroundColor Green
Write-Host "======================================`n" -ForegroundColor Green

Write-Host "Para activar el entorno en el futuro, ejecuta:" -ForegroundColor Yellow
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White

Write-Host "`nPara desactivar el entorno:" -ForegroundColor Yellow
Write-Host "  deactivate" -ForegroundColor White

Write-Host "`nPara ejecutar Jupyter:" -ForegroundColor Yellow
Write-Host "  jupyter notebook" -ForegroundColor White

Write-Host "`nPara ejecutar los notebooks:" -ForegroundColor Yellow
Write-Host "  jupyter notebook rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb" -ForegroundColor White
