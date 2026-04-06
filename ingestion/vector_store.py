from langchain_pinecone import PineconeVectorStore, PineconeEmbeddings
from pinecone import Pinecone
from config import VectorStoreConfig



class VectorStore:
    def __init__(self, config: VectorStoreConfig):
        pinecone_client = Pinecone(api_key=config.api_key)
        index = pinecone_client.Index("docuflow")
        embedder = PineconeEmbeddings(model="llama-text-embed-v2", api_key=config.api_key)
        self.vector_store = PineconeVectorStore(embedding=embedder, index=index)

    def add_documents(self, documents, namespace):
        self.vector_store.add_documents(documents, namespace=namespace)

    def search(self, query, namespace):
        return self.vector_store.similarity_search(query, namespace=namespace)