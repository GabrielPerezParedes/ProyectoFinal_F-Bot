import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader

# Establecer la clave API
os.environ["OPENAI_API_KEY"] = "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"

# Directorio de datos
data_directory = "data"

# Obtener una lista de todos los archivos PDF en el directorio 'data'
pdf_files = [f for f in os.listdir(data_directory) if f.endswith('.pdf')]

# Iterar sobre cada archivo PDF
for pdf_file in pdf_files:
    # Crear la ruta completa al archivo
    full_path = os.path.join(data_directory, pdf_file)
    
    # Cargar el PDF
    loader = PyPDFLoader(full_path)
    pages = loader.load()

    # Mostrar el nombre del archivo y la cantidad de páginas
    print(f"\nArchivo: {pdf_file}")
    print(f"Total de páginas: {len(pages)}\n")
    
    # Mostrar todo el contenido del archivo PDF
    for page in pages:
        print(page.page_content)
        print("\n" + "-"*50 + "\n")  # Esto añade una línea de separación entre las páginas.
