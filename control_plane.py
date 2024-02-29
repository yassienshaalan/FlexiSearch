class ControlPlane:
    def __init__(self, indexer, searchers):
        self.indexer = indexer
        self.searchers = searchers

    def update_index(self, documents):
        """
        Updates the index with new documents, reflecting changes across all Searcher instances.

        Parameters:
            documents: A list of documents to be indexed.
        """
        self.indexer.index_documents(documents)
        # In a real application, you'd also trigger the Searchers to update their index segments
        # This might involve re-downloading index segments from a central store or refreshing connections

    def deploy_new_searcher(self, searcher):
        """
        Adds a new Searcher instance to the pool.

        Parameters:
            searcher: The new Searcher instance to be added.
        """
        self.searchers.append(searcher)
        # Additional logic to integrate the new Searcher into the system

    def __repr__(self):
        return f"ControlPlane(Indexer: {self.indexer}, Searchers: {len(self.searchers)})"
