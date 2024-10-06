from typing import List
import chromadb

from llama_index.core import StorageContext, VectorStoreIndex, Settings
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.schema import Document

MODEL_NAME = "llama3.2"
BASE_URL = "http://localhost:11434"

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5")
Settings.llm = Ollama(model=MODEL_NAME, request_timeout=360.0)

chroma_client = chromadb.PersistentClient(path="./chroma_db")


def add_documents_and_retrieve_index(
    documents: List[Document], name: str = "documents", embed_model=Settings.embed_model
) -> VectorStoreIndex:
    """
    Create a new Chroma collection and add the given documents to it.
    Then, create a VectorStoreIndex from the documents and return it.

    Args:
        documents: The list of documents to add to the collection.
        name: The name of the Chroma collection to create. Defaults to "documents".
        embed_model: The embed model to use for the VectorStoreIndex. Defaults to Settings.embed_model.

    Returns:
        The VectorStoreIndex created from the documents.
    """
    collection = chroma_client.get_or_create_collection(name=name)
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )
    return index


def load_documents(name: str = "documents", embed_model: BaseEmbedding = Settings.embed_model) -> VectorStoreIndex:
    """Load an existing VectorStoreIndex from a Chroma collection.

    Args:
        name: The name of the Chroma collection to load from. Defaults to "documents".
        embed_model: The embed model to use for the VectorStoreIndex. Defaults to Settings.embed_model.

    Returns:
        The loaded VectorStoreIndex.
    """
    collection = chroma_client.get_collection(name=name)
    vector_store = ChromaVectorStore(chroma_collection=collection)
    return VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)
