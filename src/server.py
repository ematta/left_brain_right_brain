# Create a flask app
from flask import Flask, request
import src.model as model
import src.args as args

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
    index = model.create_index(model.load_documents_huggingface)
    response = index.query(query)
    return response


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
    return document