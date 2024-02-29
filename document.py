class Document:
    """
    Represents a document to be indexed or searched within the search engine.

    Attributes:
        id (str): Unique identifier for the document.
        content (dict): The content of the document stored in key-value pairs, where keys are field names
                        and values are the corresponding field values. This structure supports various data types
                        and is flexible for different document schemas.
    """

    def __init__(self, document_id: str, content: dict):
        """
        Initializes a new instance of the Document class.

        Parameters:
            document_id (str): The unique identifier for the document.
            content (dict): The content of the document, including all fields and their values.
        """
        self.id = document_id
        self.content = content

    def __repr__(self):
        """
        Provides a string representation of the Document object, primarily for debugging purposes.

        Returns:
            str: A string representation of the Document, typically including the document ID and a summary of the content.
        """
        content_summary = {key: value for key, value in self.content.items()[:5]}  # Just show a summary if many fields
        return f"Document(ID: {self.id}, Content: {content_summary})"
