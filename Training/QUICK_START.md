# 🚀 Quick Start - RAG Agentico con Gemini

## 1️⃣ Configuración Inicial (Primera vez)

### Opción A: PowerShell (Recomendado)
```powershell
# Ejecuta desde la carpeta del proyecto
.\setup_env.ps1
```

### Opción B: Command Prompt (CMD)
```cmd
setup_env.bat
```

## 2️⃣ Configurar API Key de Google

### Paso 1: Crear una API Key
1. Ve a https://ai.google.dev/
2. Haz clic en "Get API Key" (Obtener clave API)
3. Selecciona o crea un proyecto en Google Cloud
4. Copia la clave generada

### Paso 2: Añadirla al proyecto
```powershell
# Abre el archivo .env
notepad .env

# O si prefieres desde PowerShell
Copy-Item .env.example .env
```

Edita `.env` y reemplaza:
```
GOOGLE_API_KEY=your-api-key-here
```

con tu clave real:
```
GOOGLE_API_KEY=AIzaSy...
```

## 3️⃣ Activar el Entorno

Si no está activo automáticamente:

### PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

### CMD:
```cmd
venv\Scripts\activate
```

Verás el prompt cambiar a `(venv)` cuando esté activado.

## 4️⃣ Iniciar Jupyter

### Opción A: Abrir todo Jupyter
```powershell
jupyter notebook
```

### Opción B: Abrir solo el notebook del workshop
```powershell
jupyter notebook rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb
```

## 5️⃣ Preparar los PDFs

1. Crea una carpeta `docs/` en el proyecto
2. Coloca tus PDFs dentro (ej: `docs/documento.pdf`)

```
Training/
├── rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb
├── docs/
│   ├── documento1.pdf
│   ├── documento2.pdf
│   └── ...
├── chroma_pdfs/
└── ...
```

## ✅ Verificar la instalación

Ejecuta el script de verificación:
```powershell
.\venv\Scripts\python.exe verify_setup.py
```

Deberías ver:
```
✅ ¡Configuración completada exitosamente!
```

## 🐛 Troubleshooting

### "Module not found: langchain"
- Asegúrate de haber corrido `setup_env.ps1` o `setup_env.bat`
- Verifica que el entorno esté activado: debe mostrar `(venv)` en el prompt

### "GOOGLE_API_KEY not found"
- Verifica que existe el archivo `.env` en la carpeta del proyecto
- Verifica que contiene tu API key correctamente

### "Port 8888 is already in use"
```powershell
# Abre Jupyter en otro puerto
jupyter notebook --port 8889
```

### "No PDF files found"
- Asegúrate de crear la carpeta `docs/`
- Coloca los PDFs dentro
- Reinicia el kernel del notebook

## 📚 Siguiente paso

Una vez completada la verificación:
1. Abre el notebook: `rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb`
2. Lee las instrucciones en cada celda
3. Rellena los huecos marcados con `<FILL_IN>`
4. Ejecuta cada celda para aprender cómo funciona el RAG agentico

## 💡 Notas importantes

- El notebook contiene **blancos para rellenar** donde aprenderás los conceptos clave
- Cada celda tiene explicaciones en markdown
- Los PDFs se procesan la primera vez (puede tomar un poco)
- Los embeddings se almacenan en `chroma_pdfs/` para uso futuro

## 🤝 Necesitas ayuda?

Consulta el `README.md` para más detalles técnicos o ejecuta `verify_setup.py` para diagnosticar problemas.

---

**¡Listos para aprender sobre RAG Agentico con Gemini!** 🤖
