from config import VectorStoreConfig, ModelConfig

from ingestion.vector_store import VectorStore
from services.chat_service import ChatService

class RAGService:
    def __init__(self, vector_store: VectorStore, chat_service: ChatService):
        self.vector_store = vector_store
        self.chat_service = chat_service


    def chat(self, query, namespace):
        # Step 1: Retrieve relevant documents from vector store
        relevant_docs = self.vector_store.search(query, namespace)

        # Step 2: Build Prompt (Context + Query)
        prompt = f"Context: {relevant_docs}\n\nQuestion: {query}\nAnswer:"
        # Step 3: Use retrieved documents to generate response
        response = self.chat_service.chat([{"role": "system", "content": "You are a helpful assistant that answers questions based on provided context."},
                                           {"role": "user", "content": prompt}])

        return response