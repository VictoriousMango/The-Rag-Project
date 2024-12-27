# Files Imports
from utils.utils import Logger
from data.data_loader import pdfLoader
from utils.config import data

# Import Files
from langchain.text_splitter import RecursiveCharacterTextSplitter
from time import time

'''
!Docstring
- Prepares Data before storing it in the retriever.
- Functionalities include:
    - Text Cleaning. {QueryPreprocessor}
    - Chunking large document into smaller pieces.
    - Token Limit management for embeddings and LLMs.
'''

def QueryPreprocessor(query):
    return query.lower().strip()

def ChunkedDocument():
    start_time = time()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=40,
        is_separator_regex=False
        )
    splits = text_splitter.split_documents(pdfLoader())
    Logger(
        log=f"core.preprocessor (ChunkedDocument) executed in {time() - start_time}",
        logLevel="debug"
    )
    return splits

if __name__ == "__main__":
    try:
        Logger(
            log = f"Splits = {ChunkedDocument()}",
            logLevel="debug"
            )
    except Exception as e:
        Logger(
            log = f"Error: {str(e)}",
            logLevel="error"
            )
