# Importing Support Files
from utils import config, utils
# Library Imports
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from time import time

# creating embedding to be used in chromadb store
def embd_chromaDB():
    start_time=time()
    embedding = SentenceTransformerEmbeddings(model_name=config.core["Model Name"])
    utils.Logger(
        log=f"core.embedding (embd_chromaDB) executed in {time() - start_time}s",
        logLevel="debug"
    )
    return embedding


def get_embeddingsDoc(texts):
    start_time = time()
    """
    Generates embeddings for a list of texts using the specified model for documents.

    Args:
        texts: A list of strings.

    Returns:
        A list of embedding vectors.
    """
    embedding = embd_chromaDB()
    utils.Logger(
        log=f"core.embedding (get_embeddingsDoc) executed in {time() - start_time}s",
        logLevel="debug"
    )
    return embedding.embed_documents(texts)

def get_embeddingsQuery(texts):
    start_time = time()
    """
    Generates embeddings for a list of texts using the specified model for documents.

    Args:
        texts: A list of strings.

    Returns:
        A list of embedding vectors.
    """
    embedding = embd_chromaDB()
    utils.Logger(
        log=f"core.embedding (get_embeddingsQuery) executed in {time() - start_time}s",
        logLevel="debug"
    )
    return embedding.embed_query(texts)


# write a code to test this embedding and visualize it
# For example, you can use the following code to test the embedding and visualize it
# def test_embedding():
#     # Test the embedding
#     text = "This is a test sentence."
#     embedding_vector = embedding.embed(text)
#     print(embedding_vector)
    
if __name__ == "__main__":
    utils.Logger(log=str(get_embeddingsDoc(["Hello World", "This is not a test document."]))[:100] + '...', logLevel="debug")
    utils.Logger(log=str(get_embeddingsQuery("Hello World"))[:100] + '...', logLevel="debug")