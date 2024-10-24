from flask import Flask, request # type: ignore
from src.database import add_documents_and_retrieve_index, load_documents as db_load_documents
from src.pdf import load_documents as pdf_load_documents
import src.model as model


app = Flask(__name__)


@app.route("/query", methods=["POST"])
def query():
    """
    Handle a POST request to the /query endpoint.

    Args:
        None

    Returns:
        A JSON response containing the query result.
    """
    data = request.get_json()
    query = data["query"]
    index = db_load_documents()
    resp = model.query_index(index=index, query=query)
    return resp


@app.route("/document", methods=["POST"])
def document():
    """
    Handle a POST request to the /document endpoint.

    Args:
        None

    Returns:
        A JSON response containing the document.
    """
    data = request.get_json()
    document = data["document"]
    tokenized = pdf_load_documents(document)
    add_documents_and_retrieve_index(tokenized, model.load_documents_huggingface)
    return { "status": "ok" }