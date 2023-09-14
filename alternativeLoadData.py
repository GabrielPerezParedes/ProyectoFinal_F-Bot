import os 
from PyPDF2 import PdfReader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings, HuggingFaceEmbeddings


files_path = "/Users/gabrielperezparedes/Documents/GitHub/ProyectoFinal_F-Bot/data"
files = os.listdir(files_path)

def get_texts(files_path, files):
    texts = ""
    for file in files:
        full_file_path = os.path.join(files_path, file)
        if file.endswith('.pdf'):
            reader = PdfReader(full_file_path)
            for page in reader.pages:
                texts += page.extract_text()
    return texts

texts = get_texts(files_path, files)
print(texts)

def get_chunk_text(text):
    # Asegúrate de que RecursiveCharacterTextsplitter esté importado y adecuadamente inicializado.
    
    text_splitter = RecursiveCharacterTextsplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    
    chunks = text_splitter.split_text(text)
    return chunks

chunks = get_chunk_text(texts)
print(chunks)
