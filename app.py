from indexer import Indexer
from searcher import Searcher
from broker import Broker
from document import Document

def main():
    # Initialize Indexer with the Marqo index name
    indexer = Indexer("my-first-index")

    # Indexing documents using Marqo
    indexer.index_documents([
        Document("1", {"Title": "The Travels of Marco Polo", "Description": "A 13th-century travelogue describing Polo's travels"}),
        Document("article_591", {"Title": "Extravehicular Mobility Unit (EMU)", "Description": "The EMU is a spacesuit that provides environmental protection, mobility, life support, and communications for astronauts"})
    ])

    # Initialize Searcher with the same Marqo index name
    searcher = Searcher("my-first-index")

    # Searching documents using Marqo
    search_results = searcher.search("What is the best outfit to wear on the moon?")
    print("Search results using Marqo:")
    for result in search_results:
        print(result)

    # If you still need the Broker for aggregating results from multiple Searchers, initialize it here
    # Note: In this setup, the Broker's functionality might overlap with Marqo's search capabilities, so consider whether it's still needed
    broker = Broker([searcher])
    broker_results = broker.fan_out_query("Example query")
    print(f"Broker aggregated search results: {broker_results}")

if __name__ == "__main__":
    main()