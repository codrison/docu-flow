from ingestion.vector_store import VectorStore
from services.chat_service import ChatService
from prompts.rag import build_messages
from providers.factory import ProvideFactory


class RAGService:
    def __init__(self, vector_store: VectorStore, chat_service: ChatService):
        self.vector_store = vector_store
        self.chat_service = chat_service

    def chat(self, query: str, history: list, namespace: str, model_name: str, api_key: str):
        relevant_docs = self.vector_store.search(query, namespace)

        messages = build_messages(
            query=query,
            history=history,
            relevant_docs=relevant_docs,
            system_prompt="Use the following retrieved documents to answer the user's question. If you don't know the answer, say you don't know.",
        )

        model = ProvideFactory.get_provider(model_name, api_key).get_model()
        response = model.invoke(messages)

        return response.content