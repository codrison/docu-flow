from config import VectorStoreConfig, ModelConfig

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
        self.conversation_id = str(uuid4())
        self.conversation_service.create_conversation(self.conversation_id)


    def chat(self, query, namespace):
        # Step 1: Retrieve relevant documents from vector store
        relevant_docs = self.vector_store.search(query, namespace)

        # Step 2: Get history + build current prompt
        history = self.conversation_service.get_conversation(self.conversation_id)
        
        messages = build_messages(
            system_prompt=ModelConfig.system_prompt,
            history=history,
            query=query,
            relevant_docs=relevant_docs
        )

        # Step 3: Call LLM with full context
        response = self.chat_service.chat(messages)

        # Step 4: Log both turns AFTER response
        self.conversation_service.add_message(self.conversation_id, "user", query)
        self.conversation_service.add_message(self.conversation_id, "assistant", response)

        return response