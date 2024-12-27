# Importing Support Files
from utils import config, utils
from core import embedding
from core import preprocessor
#  Imports
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from time import time

##################################################################################################
'''
Different Embedding models available:
  {Word2Vec Embedding}   : {Trained ON/By}
- OpenAI Embedding       => GPT Model        : {Paid}
- Hugging Face Embedding => Open Source LLM  : {Free}
- Llama2 Embedding       => Facebook         : {Free}
- Google Palm Embedding  => Google           : {Free}
'''
'''
Different VectorDB Available:
- Chrome     : [Most Used Tool in Market, Local      ,        , Free]
- Pinecone   : [Most Used Tool in Market, Cloud-Based,        , Paid(1 Cluster Free)]
- Weaviate   : [Most Used Tool in Market, Cloud-Based,        , Paid(1 Cluster Free)]
- FAISS      : [                        ,            ,Facebook,]
- Redis      :
'''
######################################################################################################
'''
!Docstring
- This module should retrieve relevant data documents from your knowledge base or dataset.
- Actions Includes:
    - Vector Database Setup
    - Functions for Text embedding and similarity search.
    - Document retrieval logic.
- Testing this document : python -m core.retriever
'''
def chroma():
    print(config.core["OpenAi_API_Key"])
    DB_Client = chromadb.Client() # ChromaDB Client Setup
    # Create Collection in ChromaDB
    collection1 = DB_Client.create_collection(name="Testing1")
    pass

def CreateVectorStorage_ChromaDB():
    start_time = time()
    try:
        # Load Data from Directory {Class: DirectoryLoader, Object: loader}
        print("Starting PDF Load")
        model_name = "all-MiniLM-L6-v2" 
        
        
        embd = embedding.embd_chromaDB()
        # Create Chroma vectorstore
        vectorstore = Chroma.from_documents(
              documents=preprocessor.ChunkedDocument, 
              embedding=embd, 
              persist_directory="chroma_store"  # Directory to store the ChromaDB data
              )
        print("PDF loaded successfully.")
    except FileNotFoundError:
        print("Error: The specified PDF file was not found.")
    except Exception as e: 
        print(f"An error occurred: {e}")
    utils.Logger(logLevel="debug", log=f"CreateVectorStorage_ChromaDB took {time()-start_time}s to execute")
    

def loadVectorStorage_ChromaDB():
    start_time = time()
    """
    Loads a Chroma vectorstore from a persisted directory.

    Args:
        model_name: Name of the SentenceTransformer model to use for embeddings.

    Returns:
        A Chroma vectorstore object.
    """
    embd = embedding.embd_chromaDB()
    vectorstore = Chroma(
        persist_directory="chroma_store", 
        embedding_function=embd
    )
    utils.Logger(logLevel="debug", log=f"loadVectorStorage_ChromaDB took {time()-start_time}s to execute")
    return vectorstore

if __name__ == "__main__":
    CreateVectorStorage_ChromaDB()
    loadVectorStorage_ChromaDB()
    pass
