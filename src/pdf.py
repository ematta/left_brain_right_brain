# type: ignore
import pymupdf4llm

def parse_pdf_to_llamaindex(path: str) -> list:
    llama_reader = pymupdf4llm.LlamaMarkdownReader()
    llama_docs = llama_reader.load_data(path)
    return llama_docs
