import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader

# Establecer la clave API
os.environ["OPENAI_API_KEY"] = "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"

# Cargar el PDF
loader = PyPDFLoader("data/Cinemtica_2020.pdf")
pages = loader.load()

# Mostrar la cantidad de páginas y el contenido de la primera página
print(f"Total de páginas: {len(pages)}")
print("Contenido de la primera página:")
print(pages[0].page_content[0:500])  # Mostrando los primeros 500 caracteres de la página 1

# Mostrar los metadatos de la primera página (si deseas verlo)
print("Metadatos de la primera página:")
print(pages[0].metadata)
