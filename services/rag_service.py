from ingestion.vector_store import VectorStore
from services.chat_service import ChatService
from storage.conversation import InMemory
from prompts.rag import build_messages
from uuid import uuid4


class RAGService:
    def __init__(self, vector_store: VectorStore, chat_service: ChatService, conversation_service: InMemory):
        self.vector_store = vector_store
        self.chat_service = chat_service
        self.conversation_service = conversation_service


    def chat(self, query, namespace, model_name, api_key, conversation_id):

        # Step 1: Retrieve relevant documents from vector store
        relevant_docs = self.vector_store.search(query, namespace)

        # Step 2: Get history + build current prompt
        history = self.conversation_service.get_conversation(conversation_id)
        
        messages = build_messages(
            system_prompt="Use the following retrieved documents to answer the user's question. If you don't know the answer, say you don't know.",
            history=history,
            query=query,
            relevant_docs=relevant_docs
        )

        # Step 3: Call LLM with full context
        response = self.chat_service.chat(messages, model_name=model_name, api_key=api_key)

        # Step 4: Log both turns AFTER response
        self.conversation_service.add_message(conversation_id, "user", query)
        self.conversation_service.add_message(conversation_id, "assistant", response)

        return response