import marqo
from typing import List
from document import Document

class Indexer:
    """
    Handles the processing and indexing of documents into searchable index segments.

    Attributes:
        index_name (str): Index name.
    """

    def __init__(self, index_name: str):
        self.mq = marqo.Client(url='http://localhost:8882')
        self.index_name = index_name
        self.mq.create_index(index_name)

    def index_documents(self, documents: List[Document]):
        """
        Indexes documents using Marqo, converting them to the format Marqo expects.

        Parameters:
            documents (List[Document]): The documents to be indexed.
        """
        marqo_documents = []
        for doc in documents:
            marqo_doc = {**doc.content, "_id": doc.id}
            marqo_documents.append(marqo_doc)
        
        self.mq.index(self.index_name).add_documents(marqo_documents, tensor_fields=["Description"])

    def __repr__(self):
        return f"Indexer(Index Name: {self.index_name})"
    
