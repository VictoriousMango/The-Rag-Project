# File Imports
from utils import config
from utils.utils import Logger

# Library Imports
from langchain_community.document_loaders import PyMuPDFLoader
from time import time

'''
!Docstring
- Loads and processes raw data (eg., PDFs, Textfiles)
- Functionalities Include:
    - PDF Parsing (eg., PyPDF2, pdfplumber)
    - Data extraction from files and databases 
'''

def pdfLoader():
    start_time = time()
    loader = PyMuPDFLoader(config.data["PDF Path"])
    data = loader.load() 
    Logger(
        log = f"data.data_loader (pdfLoader) executed in {time() - start_time}s",
        logLevel="debug"
        )
    return data

if __name__ == "__main__":
    Logger(
        log = f"Data = {pdfLoader()}",
        logLevel="debug"
        )
    