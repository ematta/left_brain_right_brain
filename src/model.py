from llama_index.core import VectorStoreIndex, Settings  # type: ignore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding  # type: ignore
from llama_index.embeddings.ollama import OllamaEmbedding  # type: ignore
from llama_index.llms.ollama import Ollama  # type: ignore


MODEL_NAME = "llama3.2"
BASE_URL = "http://localhost:11434"


def create_index(documents, use_huggingface: bool = True) -> VectorStoreIndex:
    """
    Create a VectorStoreIndex from a list of documents.

    Args:
        documents: The list of documents to create the index from.
        use_huggingface: Whether to use the HuggingFace embedding model.
            Defaults to True.

    Returns:
        The created VectorStoreIndex.
    """
    if use_huggingface:
        return load_documents_huggingface(documents)
    else:
        return load_documents_ollama(documents)


def load_documents_huggingface(documents) -> VectorStoreIndex:
    """
    Create a VectorStoreIndex from a list of documents using the HuggingFace
    embedding model.

    Args:
        documents: The list of documents to create the index from.

    Returns:
        The created VectorStoreIndex.
    """
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.llm = Ollama(model=MODEL_NAME, request_timeout=360.0)
    return VectorStoreIndex.from_documents(documents)


def load_documents_ollama(documents) -> VectorStoreIndex:
    """
    Create a VectorStoreIndex from a list of documents using the Ollama
    embedding model.

    Args:
        documents: The list of documents to create the index from.

    Returns:
        The created VectorStoreIndex.
    """
    Settings.embed_model = OllamaEmbedding(
        model_name=MODEL_NAME,
        base_url=BASE_URL,
        ollama_additional_kwargs={"mirostat": 0},
    )
    Settings.llm = Ollama(model=MODEL_NAME, request_timeout=360.0)
    return VectorStoreIndex.from_documents(documents)

