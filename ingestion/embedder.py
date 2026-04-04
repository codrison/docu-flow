from config import EmbeddingConfig
from langchain_pinecone import PineconeEmbeddings


class Embedder:
    def __init__(self, config: EmbeddingConfig):
        self.embedder = PineconeEmbeddings(model=config.model_name, 
                                           api_key=config.api_key)

    def embed_documents(self, documents):
        texts = [doc.page_content for doc in documents]
        return self.embedder.embed_documents(texts)
    
    def embed_query(self, query):
        return self.embedder.embed_query(query)
