import pymupdf4llm  # type: ignore

def pdf_documents(path):
    """
    Parse a PDF file into a list of documents that can be used with LlamaIndex.

    Parameters
    ----------
    path : str
        The path to the PDF file to parse

    Returns
    -------
    llama_docs : list of dict
        The list of documents, where each document is a dictionary containing
        the text of the document and possibly other metadata.

    Notes
    -----
    The PDF is parsed using pymupdf4llm, which is a thin wrapper around the
    PyMuPDF library. The parsing may not always be perfect, as the structure
    of the PDF can be complex and may not be easily converted into a plain
    text document.

    """
    llama_reader = pymupdf4llm.LlamaMarkdownReader()
    llama_docs = llama_reader.load_data(path)
    return llama_docs
