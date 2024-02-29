from typing import List
from document import Document
from index_segment import IndexSegment

class Searcher:
    """
    Executes search queries against the indexed documents contained in index segments.

    Attributes:
        index_segments (List[IndexSegment]): A list of IndexSegments that the searcher can query against.
    """

    def __init__(self,index_name):
        """
        Initializes a new instance of the Searcher class.
        """
        self.mq = marqo.Client(url='http://localhost:8882')
        self.index_name = index_name

    def search(self, query: str, top_k: int = 10) -> List[dict]:
        """
        Performs a vector search using Marqo based on the query.

        Parameters:
            query (str): The search query.
            top_k (int): Number of top results to retrieve.

        Returns:
            List[dict]: A list of dictionaries representing the matching documents.
        """
        results = self.mq.index(self.index_name).search(q=query, top_k=top_k)
        return results["hits"]


    def retrieve_document(self, document_id: str) -> Document:
        # Logic to retrieve a Document object by its ID
        pass

    def __repr__(self):
        """
        Provides a string representation of the Searcher object, primarily for debugging purposes.

        Returns:
            str: A string representation of the Searcher, including the number of loaded index segments.
        """
        return f"Searcher(Loaded Index: {len(self.index_name)})"
