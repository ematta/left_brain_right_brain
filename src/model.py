from llama_index.core import VectorStoreIndex # type: ignore


def query_index(query: str, index: VectorStoreIndex) -> str:
    """
    Query a VectorStoreIndex using the HuggingFace embedding model.

    Args:
        query: The query to use for the query.
        index: The VectorStoreIndex to query.

    Returns:
        The query result.
    """
    query_engine = index.as_query_engine(
        response_mode="tree_summarize",
        verbose=True)
    response = query_engine.query(query)
    return response.response
