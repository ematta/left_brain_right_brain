import os
from llama_index.core import VectorStoreIndex, Settings, PromptTemplate  # type: ignore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding  # type: ignore
from llama_index.embeddings.ollama import OllamaEmbedding  # type: ignore
from llama_index.llms.ollama import Ollama  # type: ignore


MODEL = "llama3.2:1b"


def load_documents_huggingface(documents):
    """
    Create a VectorStoreIndex from a list of documents.

    Parameters
    ----------
    documents : list of dict
        The list of documents to create the index from. Each document
        should be a dictionary containing the text of the document and
        possibly other metadata. The dictionary should have a "text" key
        with the text of the document.

    Returns
    -------
    index : VectorStoreIndex
        The created VectorStoreIndex.

    Notes
    -----
    The index is created with a HuggingFaceEmbedding model and an Ollama
    language model. The embeddings are computed using the BAAI/bge-small-en-v1.5
    model, and the language model is the llama3.2:1b model.
    """
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5")
    Settings.llm = Ollama(model="llama3.2:1b", request_timeout=360.0)
    index = VectorStoreIndex.from_documents(
        documents,
    )
    return index


def load_documents_ollama(documents):
    """
    Create a VectorStoreIndex from a list of documents.

    Parameters
    ----------
    documents : list of dict
        The list of documents to create the index from. Each document
        should be a dictionary containing the text of the document and
        possibly other metadata. The dictionary should have a "text" key
        with the text of the document.

    Returns
    -------
    index : VectorStoreIndex
        The created VectorStoreIndex.

    Notes
    -----
    The index is created with an OllamaEmbedding model and an Ollama
    language model. The embeddings are computed using the OllamaEmbedding
    model, and the language model is the Ollama model.
    """
    Settings.embed_model = OllamaEmbedding(
        model_name=MODEL,
        base_url=os.environ.get("EMBEDDING_BASE_URL",
                                "http://localhost:11434"),
        ollama_additional_kwargs={"mirostat": 0},
    )
    Settings.llm = Ollama(model=MODEL, request_timeout=360.0)
    index = VectorStoreIndex.from_documents(
        documents,
    )
    return index
