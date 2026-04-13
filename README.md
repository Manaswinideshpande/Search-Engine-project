Project: Enhancing Search Engine Relevance for Video Subtitles

Video Subtitle Search Engine 🔍
An advanced search engine designed to improve the relevance and accuracy of video subtitle retrieval. By leveraging Natural Language Processing (NLP) and machine learning, this project enables users to find specific video content based on semantic subtitle data rather than just metadata.

Key Features
Semantic Retrieval: Uses advanced embeddings to understand the context of user queries beyond simple keyword matching.

Large-scale Data Processing: Efficiently handles and processes over 82,000 subtitle files from a compressed SQLite database.

Data Cleaning Pipeline: Includes a comprehensive preprocessing stage that handles Latin-1 decoding, subtitle timestamp removal, and text normalization.

Vector Embeddings: Implements BERT-based embeddings to convert subtitle text into dense vectors for high-relevance search.

Tech Stack
Core Logic: Python

Data Handling: Pandas, SQLite3

NLP & Embeddings: BERT (Bidirectional Encoder Representations from Transformers)

Environment: Jupyter Notebook / Anaconda

Project Workflow
Data Ingestion: Reading subtitle data (num, name, and encoded content) from a zipfiles table in a SQLite database.

Preprocessing: Decoding binary content, cleaning timestamps from .srt files, and re-indexing data.

Sampling: Optimized processing by utilizing a 10% stratified sample of the total dataset for model building.

Embedding Generation: Transforming cleaned subtitle text into vector representations using a BERT model
