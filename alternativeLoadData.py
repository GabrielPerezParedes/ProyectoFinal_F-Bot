import os 
from langchain.document_loaders import PyPDFLoader 
from PyPDF2 import PdfReader

files_path = "/Users/gabrielperezparedes/Documents/GitHub/ProyectoFinal_F-Bot/data"
files = os.listdir(files_path)

def get_texts(files_path, files):
    texts = ""
    for file in files:
        # Usa os.path.join para unir la ruta del directorio con el nombre del archivo
        full_file_path = os.path.join(files_path, file)
        # Ahora verifica si el archivo es un PDF antes de intentar abrirlo
        if file.endswith('.pdf'):
            reader = PdfReader(full_file_path)
            for page in reader.pages:
                texts += page.extract_text()
    return texts  # Recuerda desindentar esta línea para que esté fuera del bucle for

def get_chunk_text (text):
    
    text_splitter = RecursiveCharacterTextsplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len
    )
    
    chunks = text_splitter.split_text(text)
    return chunks

chunks = get_chunk_text(texts)
print (chunks)
