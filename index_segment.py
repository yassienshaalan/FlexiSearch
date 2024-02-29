from typing import List
from document import Document

class IndexSegment:
    """
    Represents a segment of the search index, containing a collection of documents.

    Attributes:
        segment_id (str): A unique identifier for the index segment.
        documents (List[Document]): A list of Document objects contained within the segment.
    """

    def __init__(self, segment_id: str, documents: List[Document]):
        """
        Initializes a new instance of the IndexSegment class.

        Parameters:
            segment_id (str): The unique identifier for the index segment.
            documents (List[Document]): The list of Document objects to be included in the segment.
        """
        self.segment_id = segment_id
        self.documents = documents

    def __repr__(self):
        """
        Provides a string representation of the IndexSegment object, primarily for debugging purposes.

        Returns:
            str: A string representation of the IndexSegment, typically including the segment ID and the number of documents it contains.
        """
        return f"IndexSegment(ID: {self.segment_id}, Documents: {len(self.documents)})"

    def add_document(self, document: Document):
        """
        Adds a Document to the index segment.

        Parameters:
            document (Document): The Document object to be added to the segment.
        """
        self.documents.append(document)

    def remove_document(self, document_id: str):
        """
        Removes a Document from the index segment based on its ID.

        Parameters:
            document_id (str): The unique identifier of the Document to be removed.
        """
        self.documents = [doc for doc in self.documents if doc.id != document_id]
