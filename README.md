# FlexiSearch
This repository hosts a prototype of a scalable, general-purpose search engine, showcasing an advanced architecture that addresses common scalability challenges in search systems. The project is based on a segment-replication model and is designed to efficiently handle both indexing and searching operations, making it suitable for handling large volumes of data and high query loads.
This search engine prototype leverages vector search to enhance search capabilities, enabling more nuanced and semantically relevant search results. Vector search uses machine learning models to convert text into high-dimensional vectors that represent semantic meanings, allowing for searches based on conceptual similarity rather than keyword matching alone.

## Key Features:

Segment Replication Model: Divides the indexing and searching responsibilities into distinct services to optimize performance and scalability.
Custom Indexing Service: A dedicated service for handling all incoming indexing traffic, capable of processing and storing diverse document types with complex relationships.
Searcher Service: A replicated service that performs searches against indexes stored in a cloud-based storage solution, designed to scale dynamically with search traffic.
Broker Service: Serves as an aggregation layer, distributing queries to the appropriate index shards and merging results to provide a seamless search experience.
Query Understanding and Planning: Incorporates a sophisticated component for interpreting and optimizing user queries, ensuring relevant and accurate search results.
Configurable Index Schema: Supports a flexible index schema to accommodate various document types and relationships, enabling users to tailor the search engine to specific needs.
Architecture Highlights:
The architecture is built on top of Apache Lucene, leveraging its powerful information retrieval capabilities. It features a clean separation between core search functionalities and business logic, allowing for easy customization and extension. The system is designed to be horizontally scalable, with the ability to add more replicas to handle increased loads.

## Technologies Used:

Apache Lucene for the foundational information retrieval functionalities.
Cloud-based storage solutions for storing index segments, ensuring durability and availability.
A modern programming language and framework for developing the services, ensuring robustness and maintainability.
This prototype serves as an educational tool and a starting point for developers looking to understand or build their own search engine systems. It demonstrates how to tackle common challenges in search engine architecture, such as scalability, efficiency, and flexibility, while also providing insights into advanced features like query understanding and planning."

This description provides a comprehensive overview of the project, highlighting its purpose, key features, architecture, and the technologies used, without attributing the architecture to a specific source. It sets the stage for potential contributors or learners to understand what the project is about, how it's structured, and what technologies it leverages.



## Integration with Marqo
We've integrated Marqo, a tensor search engine, to provide powerful vector search functionalities. Marqo allows us to index our documents as vectors and perform similarity searches, making our search results more relevant and context-aware.
