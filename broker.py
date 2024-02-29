from typing import List
from searcher import Searcher  # Ensure this is the Searcher class that interacts with Marqo

class Broker:
    def __init__(self, searchers: List[Searcher]):
        self.searchers = searchers

    def fan_out_query(self, query: str) -> List[dict]:
        """
        Distributes the query to all registered Searcher instances and aggregates the results.

        Parameters:
            query (str): The search query to be executed.

        Returns:
            List[dict]: Aggregated search results from all Searcher instances.
        """
        aggregated_results = []
        for searcher in self.searchers:
            results = searcher.search(query)
            aggregated_results.extend(results)
        return aggregated_results

    def __repr__(self):
        return f"Broker(Searchers: {len(self.searchers)})"
