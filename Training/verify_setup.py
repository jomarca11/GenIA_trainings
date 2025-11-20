#!/usr/bin/env python3
"""
Verification script to test if all dependencies are installed and working correctly.
Run this after setting up the environment to ensure everything is configured properly.
"""

import sys

def test_imports():
    """Test if all required packages can be imported."""
    packages = {
        'langchain': 'LangChain',
        'langchain_community': 'LangChain Community',
        'langchain_text_splitters': 'LangChain Text Splitters',
        'langchain_google_genai': 'LangChain Google Genai',
        'chromadb': 'Chroma DB',
        'tiktoken': 'TikToken',
        'pypdf': 'PyPDF',
        'dotenv': 'python-dotenv',
        'langgraph': 'LangGraph',
        'IPython': 'IPython',
        'jupyter': 'Jupyter',
    }
    
    failed = []
    print("=" * 60)
    print("VERIFICANDO DEPENDENCIAS")
    print("=" * 60)
    
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}: OK")
        except ImportError as e:
            print(f"✗ {name}: FALLO ({e})")
            failed.append(name)
    
    print("=" * 60)
    
    if failed:
        print(f"\n❌ {len(failed)} paquete(s) no instalado(s):")
        for name in failed:
            print(f"   - {name}")
        return False
    else:
        print("\n✓ ¡Todas las dependencias están instaladas correctamente!")
        return True

def test_google_genai():
    """Test if Google GenAI is properly configured."""
    print("\n" + "=" * 60)
    print("VERIFICANDO CONFIGURACIÓN DE GOOGLE GENAI")
    print("=" * 60)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("✓ ChatGoogleGenerativeAI: Disponible")
        
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        print("✓ GoogleGenerativeAIEmbeddings: Disponible")
        
        print("\n⚠ NOTA: Para usar Gemini necesitas una API Key de Google")
        print("   1. Ve a https://ai.google.dev/")
        print("   2. Crea una API key gratuita")
        print("   3. Copia la clave en el archivo .env")
        return True
    except ImportError as e:
        print(f"✗ Google GenAI: {e}")
        return False

def test_chromadb():
    """Test if Chroma DB is working."""
    print("\n" + "=" * 60)
    print("VERIFICANDO CHROMA DB")
    print("=" * 60)
    
    try:
        import chromadb
        print(f"✓ Chroma DB: Versión {chromadb.__version__}")
        
        # Test basic connection
        client = chromadb.Client()
        print("✓ Conexión básica a Chroma: OK")
        return True
    except Exception as e:
        print(f"✗ Chroma DB: {e}")
        return False

def test_environment_file():
    """Check if .env file exists."""
    import os
    print("\n" + "=" * 60)
    print("VERIFICANDO CONFIGURACIÓN")
    print("=" * 60)
    
    if os.path.exists(".env"):
        print("✓ Archivo .env encontrado")
        try:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("GOOGLE_API_KEY")
            if api_key and api_key != "your-api-key-here":
                print("✓ GOOGLE_API_KEY configurada")
                return True
            else:
                print("⚠ GOOGLE_API_KEY no configurada o vacía")
                print("   Por favor, actualiza el archivo .env con tu API key")
                return False
        except Exception as e:
            print(f"✗ Error cargando .env: {e}")
            return False
    else:
        print("⚠ Archivo .env no encontrado")
        print("   Copia .env.example a .env y configura tu GOOGLE_API_KEY")
        return False

def main():
    """Run all verification tests."""
    print("\n🔍 VERIFICACIÓN DE INSTALACIÓN - RAG Agentico Gemini\n")
    
    results = {
        "Importaciones": test_imports(),
        "Google GenAI": test_google_genai(),
        "Chroma DB": test_chromadb(),
        "Configuración": test_environment_file(),
    }
    
    print("\n" + "=" * 60)
    print("RESUMEN DE VERIFICACIÓN")
    print("=" * 60)
    
    for test_name, passed in results.items():
        status = "✓" if passed else "⚠"
        print(f"{status} {test_name}")
    
    print("=" * 60)
    
    all_ok = all(results.values())
    
    if all_ok:
        print("\n✅ ¡Configuración completada exitosamente!")
        print("   Puedes iniciar Jupyter con: jupyter notebook")
        print("   O abre directamente: rag_local_pdfs-agentico_gemini_WORKSHOP.ipynb")
    else:
        print("\n⚠️ Hay algunos items por revisar. Consulta el README.md para más detalles.")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
