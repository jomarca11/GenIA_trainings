# RAG con Gemini - Guía de Configuración

## 📋 Requisitos previos

- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)
- Google API Key para acceder a Gemini

## 🚀 Instalación rápida

### Opción 1: PowerShell (Recomendado para Windows)

```powershell
# Abre PowerShell en esta carpeta y ejecuta:
.\setup_env.ps1
```

### Opción 2: CMD (Command Prompt)

```cmd
# Abre CMD en esta carpeta y ejecuta:
setup_env.bat
```

### Opción 3: Manual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar entorno (CMD)
venv\Scripts\activate.bat

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
```

## 🔑 Configurar Google API Key

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea una nueva API Key
3. Crea un archivo `.env` en esta carpeta con:

```
GOOGLE_API_KEY=tu_clave_aqui
```

## 📚 Notebooks disponibles

### rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb
Notebook con huecos (`<FILL_IN>`) para que los alumnos completen el código. Ideal para charlas de capacitación.

### rag_local_pdfs-agentico_gemini.ipynb
Notebook completo con soluciones.

## ▶️ Ejecutar los notebooks

Una vez el entorno esté activado:

```bash
# Iniciar Jupyter
jupyter notebook

# O abrir un notebook específico
jupyter notebook rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb
```

## 📁 Estructura de carpetas

```
Training/
├── requirements.txt                           # Dependencias
├── setup_env.ps1                             # Script de setup (PowerShell)
├── setup_env.bat                             # Script de setup (CMD)
├── .env                                      # API Key (crear)
├── docs/                                     # PDFs a procesar
├── chroma_pdfs/                              # Vector store (se crea automáticamente)
├── rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb    # Notebook con huecos
├── rag_local_pdfs-agentico_gemini.ipynb             # Notebook completo
└── venv/                                     # Entorno virtual (se crea)
```

## 🔧 Solución de problemas

### Error: "python: command not found"
- Verifica que Python está instalado: `python --version`
- En algunos sistemas puede ser `python3` en lugar de `python`

### Error: "Permission denied" (PowerShell)
- Ejecuta: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Error: "GOOGLE_API_KEY not found"
- Crea un archivo `.env` en esta carpeta con tu API Key
- O establece la variable de entorno manualmente

### Jupyter no abre el navegador
- Abre manualmente: http://localhost:8888

## 📖 Contenido del notebook

El notebook contiene un **RAG agentico** (Retrieval-Augmented Generation) con:

1. **Carga de PDFs** desde una carpeta
2. **Chunking** (división en trozos) de documentos
3. **Embeddings** con Google Gemini
4. **Vector Store** con Chroma
5. **Agente inteligente** que:
   - Decide si buscar información en los documentos
   - Evalúa la relevancia de los resultados
   - Reescribe preguntas poco claras
   - Genera respuestas finales

## ✅ Verificar instalación

```bash
# Verifica que el entorno está activado
python -c "import langchain; print('✓ LangChain instalado')"
python -c "import chromadb; print('✓ Chroma instalado')"
python -c "import langchain_google_genai; print('✓ Google Genai instalado')"
```

## 💡 Tips

- Coloca tus PDFs en la carpeta `docs/`
- El vector store se guardará en `chroma_pdfs/`
- Puedes reutilizar el vector store en futuras ejecuciones
- Ajusta `CHUNK_SIZE` y `CHUNK_OVERLAP` según tus necesidades

---

**¿Preguntas?** Revisa los notebooks o consulta la documentación de [LangChain](https://python.langchain.com/) y [Google Gemini API](https://ai.google.dev/)
