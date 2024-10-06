from llama_index.core import VectorStoreIndex


def query_index(query: str, index: VectorStoreIndex, streaming: bool = False) -> str:
    """
    Query a VectorStoreIndex using the HuggingFace embedding model.

    Args:
        query: The query to use for the query.
        index: The VectorStoreIndex to query.
        streaming: Whether to stream the query results. Defaults to False.

    Returns:
        The query result.
    """
    query_engine = index.as_query_engine(
        response_mode="tree_summarize",
        verbose=True)
    response = query_engine.query(query)
    return response
