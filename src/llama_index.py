from llama_index.core import VectorStoreIndex, Settings # type: ignore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding # type: ignore
from llama_index.llms.ollama import Ollama # type: ignore


def load_documents(documents):
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    Settings.llm = Ollama(model="llama3.2:1b", request_timeout=360.0)
    index = VectorStoreIndex.from_documents(
        documents,
    )
    return index
