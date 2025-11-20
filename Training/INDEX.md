# 📑 Índice del Proyecto - RAG Agentico Gemini

## 🎯 Objetivo del Proyecto

Convertir un notebook de RAG agentico de OpenAI a Google Gemini, con espacios en blanco para que los estudiantes completen y aprendan los conceptos clave.

---

## 📁 Estructura del Proyecto

```
Training/
├── 📘 NOTEBOOKS (Principales)
│   ├── rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb   ← ⭐ MAIN NOTEBOOK (con blancos para alumnos)
│   ├── rag_local_pdfs-agentico_gemini_sol.ipynb         ← Solución completa (con respuestas)
│   ├── rag_local_pdfs-agentico_gemini.ipynb             ← Versión base Gemini
│   └── rag_local_pdfs-agentico_openAI.ipynb             ← Original OpenAI (referencia)
│
├── 📚 DOCUMENTACIÓN
│   ├── QUICK_START.md                                  ← Guía rápida para empezar
│   ├── README.md                                       ← Documentación completa
│   ├── INDEX.md                                        ← Este archivo
│   └── WORKSHOP_langchain_fillins.md                   ← Notas del workshop
│
├── ⚙️ CONFIGURACIÓN
│   ├── requirements.txt                                ← Dependencias Python
│   ├── .env                                            ← Configuración (local, no compartir)
│   ├── .env.example                                    ← Template de .env
│   ├── setup_env.ps1                                   ← Setup script (PowerShell)
│   ├── setup_env.bat                                   ← Setup script (CMD)
│   └── verify_setup.py                                 ← Script de verificación
│
├── 📁 DATOS & CACHÉ
│   ├── docs/                                           ← PDFs para procesar
│   ├── chroma_pdfs/                                    ← Base de datos vectorial (Chroma)
│   ├── chroma_pdfs_gemini/                             ← DB Chroma versión Gemini
│   └── 1.0.1/                                          ← Archivos de versión anterior
│
├── 🖼️ MULTIMEDIA
│   ├── images/                                         ← Imágenes del proyecto
│   └── .github/                                        ← Configuración GitHub
│
└── 🔧 ENTORNO
    └── venv/                                           ← Entorno virtual Python (creado por setup)
```

---

## 🚀 Flujo de Uso

### 1️⃣ PRIMERA VEZ (Setup)
```
Usuario descarga proyecto
    ↓
Ejecuta setup_env.ps1 (o .bat)
    ↓
Se crea venv/ + instala dependencias
    ↓
Ejecuta verify_setup.py
    ↓
Configura .env con GOOGLE_API_KEY
    ↓
✅ Listo para usar
```

### 2️⃣ DURANTE LA CLASE
```
1. Abrir: rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb
2. Leer instrucciones en cada celda
3. Buscar <FILL_IN> = espacios en blanco para completar
4. Ejecutar y aprender cómo funciona cada componente
5. Los PDFs se procesan automáticamente en la primera ejecución
```

### 3️⃣ VERIFICACIÓN
```
Ejecutar: verify_setup.py
    ↓
Verifica todas las dependencias
    ↓
Prueba conexión con Gemini API
    ↓
Valida Chroma DB
    ↓
✅ Confirma que todo está ready
```

---

## 📘 Notebooks Disponibles

### ⭐ `rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb`
**PROPÓSITO:** Notebook principal para la clase
- **Contenido:** RAG agentico con Google Gemini
- **Formato:** 50 celdas (markdown + código)
- **Características:**
  - Blancos `<FILL_IN>` para completar
  - Secciones:
    1. Instalación de dependencias
    2. Importaciones
    3. Configuración (CHUNK_SIZE, MODELOS, etc.)
    4. Carga de PDFs
    5. Chunking (RecursiveCharacterTextSplitter)
    6. Embeddings (GoogleGenerativeAIEmbeddings)
    7. Vector store (Chroma)
    8. Nodos agenticos (genera_query, grade_documents, rescribir_question, genera_respuesta)
    9. Grafo/Workflow (LangGraph)
    10. Ejecución e iteración
- **Alumnos:** Deben completar los espacios en blanco
- **Tiempo:** ~1-2 horas según nivel

### 📋 `rag_local_pdfs-agentico_gemini_sol.ipynb`
**PROPÓSITO:** Solución completa
- **Contenido:** Mismo que WORKSHOP pero sin blancos
- **Uso:** Referencia para instructor o para copiar soluciones

### 🔄 `rag_local_pdfs-agentico_gemini.ipynb`
**PROPÓSITO:** Versión base sin customizaciones
- **Contenido:** RAG Gemini sin blancos pero básico

### 🟠 `rag_local_pdfs-agentico_openAI.ipynb`
**PROPÓSITO:** Referencia original
- **Contenido:** Notebook original con OpenAI
- **Uso:** Comparar cambios para entender migración a Gemini

---

## ⚙️ Scripts de Configuración

### `setup_env.ps1` (PowerShell)
```powershell
# Ejecutar:
.\setup_env.ps1

# Acciones:
✓ Crea entorno virtual (venv/)
✓ Activa venv
✓ Actualiza pip
✓ Instala requirements.txt
✓ Muestra instrucciones de uso
```

### `setup_env.bat` (Command Prompt)
```cmd
# Ejecutar:
setup_env.bat

# Acciones: Similares a PowerShell pero para CMD
```

### `verify_setup.py` (Verificación)
```powershell
# Ejecutar:
.\venv\Scripts\python.exe verify_setup.py

# Verifica:
✓ Todas las dependencias importables
✓ Google GenAI disponible
✓ Chroma DB funciona
✓ Archivo .env existe y está configurado
```

---

## 📝 Archivos de Configuración

### `requirements.txt`
Especifica todas las dependencias necesarias:
- **langchain** (v0.2.5+) - Framework principal
- **langchain-community** - Integraciones
- **langchain-text-splitters** - Chunking
- **langchain-google-genai** - Google Gemini API
- **chromadb** (v0.5.0+) - Vector store
- **tiktoken** - Tokenización
- **pypdf** (v4+) - Lectura de PDFs
- **python-dotenv** - Gestión de .env
- **langgraph** - Workflow/grafo
- **jupyter** - Notebooks
- **ipython** - Shell interactivo

### `.env` (Configuración Local)
```env
GOOGLE_API_KEY=tu-api-key-aqui
LOG_LEVEL=INFO  # Opcional
```

**IMPORTANTE:** No compartir este archivo (contiene secretos)

### `.env.example` (Template)
```env
GOOGLE_API_KEY=your-api-key-here
# LOG_LEVEL=INFO
```

Uso: Copiar a `.env` y rellenar valores reales

---

## 📊 Datos & Caché

### `docs/` Carpeta
**Propósito:** Almacenar PDFs para procesar
```
docs/
├── documento1.pdf
├── documento2.pdf
└── documento3.pdf
```

Comportamiento:
- Vacía al principio
- El usuario añade PDFs aquí
- El notebook los procesa automáticamente

### `chroma_pdfs/` y `chroma_pdfs_gemini/`
**Propósito:** Almacenar embeddings vectoriales
- Bases de datos Chroma persistentes
- Se crean automáticamente en primera ejecución
- Reutilizan embeddings en ejecuciones posteriores
- Mejora performance: no reprocesa PDFs

---

## 📚 Documentación

### `QUICK_START.md` ⚡
**Para:** Empezar rápidamente
- 5 pasos simples
- Solución de problemas comunes
- Tiempo: ~10 minutos

### `README.md` 📖
**Para:** Referencia completa
- Prerequisitos detallados
- Opciones de instalación
- Configuración de Google API Key
- Descripción de notebooks
- Troubleshooting extenso
- Comandos de verificación

### `INDEX.md` 📑
**Para:** Entender la estructura del proyecto
- Este documento
- Mapeo de archivos
- Flujos de trabajo
- Referencias cruzadas

---

## 🔑 Conceptos Clave

### RAG (Retrieval-Augmented Generation)
1. **Retrieval:** Busca documentos relevantes
2. **Augmentation:** Aumenta el prompt con contexto
3. **Generation:** LLM genera respuesta informada

### Agentico
Flujo de control más inteligente:
- ¿La información recuperada es relevante?
- ¿Necesito reescribir la pregunta?
- ¿Puedo responder o necesito más contexto?

### Workflow (LangGraph)
Orquesta los pasos del agente:
```
Pregunta → Generar Query → Recuperar → Calificar
    ↓
¿Relevante? → No → Reescribir Pregunta → Recuperar
    ↓
Sí → Generar Respuesta
```

---

## 🎓 Huecos para Rellenar (<FILL_IN>)

En el notebook WORKSHOP encontrarás espacios como:
```python
embeddings = GoogleGenerativeAIEmbeddings(model=<FILL_IN>)
```

Los alumnos deben completar con:
```python
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
```

**Ubicaciones de blancos:**
- Configuración: CHUNK_SIZE, CHUNK_OVERLAP, nombres de modelos
- Chunking: parámetros de RecursiveCharacterTextSplitter
- Embeddings: nombre del modelo
- Nodos: lógica de los agentes
- Grafo: conexiones del workflow

---

## ✅ Checklist de Uso

Para el Instructor:
- [ ] Descarga/clona el proyecto
- [ ] Ejecuta `setup_env.ps1` o `setup_env.bat`
- [ ] Ejecuta `verify_setup.py` ← verifica que todo funciona
- [ ] Obtiene API key de Google (https://ai.google.dev/)
- [ ] Configura `.env` con API key
- [ ] Añade PDFs de ejemplo en `docs/`
- [ ] Abre `rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb` en Jupyter
- [ ] Revisa `rag_local_pdfs-agentico_gemini_sol.ipynb` como referencia
- [ ] Distribuye `QUICK_START.md` a los alumnos

Para los Alumnos:
- [ ] Lee `QUICK_START.md`
- [ ] Ejecuta `setup_env.ps1`
- [ ] Obtiene API key (https://ai.google.dev/)
- [ ] Configura `.env`
- [ ] Ejecuta `verify_setup.py`
- [ ] Abre `rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb`
- [ ] Completa los `<FILL_IN>`
- [ ] Aprende sobre RAG Agentico con Gemini 🎉

---

## 🔗 Enlaces Útiles

- [Google AI Studio](https://ai.google.dev/) - Crear API keys
- [LangChain Docs](https://python.langchain.com/) - Framework principal
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Workflow orchestration
- [Chroma](https://www.trychroma.com/) - Vector database
- [Google Generative AI](https://ai.google.dev/tutorials/python_quickstart) - Gemini API

---

## 📊 Información del Proyecto

**Nombre:** RAG Local PDFs - Agentico Gemini
**Versión:** 1.0.0
**Fecha:** 2025
**Tecnología:** LangChain + Google Gemini + Chroma
**Público:** Estudiantes / Profesionales de IA
**Duración:** 1-2 horas
**Nivel:** Intermedio (requiere conocimientos básicos de Python y ML)

---

## 🤝 Soporte & Troubleshooting

**Problema:** "ModuleNotFoundError: No module named 'langchain'"
- **Solución:** Ejecuta setup_env.ps1 nuevamente

**Problema:** "GOOGLE_API_KEY not found"
- **Solución:** Configura .env con tu API key

**Problema:** "Port 8888 already in use"
- **Solución:** `jupyter notebook --port 8889`

**Problema:** "No PDF files found"
- **Solución:** Crea carpeta docs/ y añade PDFs

Más en `README.md` → Troubleshooting section

---

**¡Proyecto listo para usar!** 🎉

Este INDEX sirve como mapa del proyecto. Consulta los archivos específicos para más detalles.
