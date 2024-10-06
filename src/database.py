import chromadb

from llama_index.core import StorageContext, VectorStoreIndex, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


MODEL_NAME = "llama3.2"
BASE_URL = "http://localhost:11434"

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5")
Settings.llm = Ollama(model=MODEL_NAME, request_timeout=360.0)

chroma_client = chromadb.PersistentClient(path="./chroma_db")


def add_and_retrieve_document(documents, name="documents", embed_model=Settings.embed_model):
    collection = chroma_client.get_or_create_collection(name="documents")
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=Settings.embed_model
    )
    return index


def load_documents(name="documents", embed_model=Settings.embed_model):
    chroma_collection = chroma_client.get_collection(name=name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        embed_model=embed_model,
    )
    return index
