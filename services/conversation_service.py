from storage.store import InMemory
from storage.models import Conversation, Message
from services.chat_service import ChatService
from services.rag_service import RAGService
from datetime import datetime
from uuid import uuid4


class ConversationService:
    def __init__(self, store: InMemory, chat_service: ChatService = None, rag_service: RAGService = None):
        self.store = store
        self.chat_service = chat_service
        self.rag_service = rag_service

    def create_conversation(self, user_id: str, title: str = None, namespace: str = None):
        conversation = Conversation(
            conversation_id=str(uuid4()),
            user_id=user_id,
            title=title,
            namespace=namespace,
            created_at=datetime.now()
        )
        self.store.create_conversation(conversation)
        return conversation.conversation_id

    def chat(self, conversation_id: str, query: str, model_name: str, api_key: str):
        conversation = self.store.get_conversation(conversation_id)
        history = conversation["messages"]
        namespace = conversation["namespace"]

        if namespace is not None:
            response = self.rag_service.chat(
                query=query,
                history=history,
                model_name=model_name,
                api_key=api_key,
                namespace=namespace
            )
        else:
            response = self.chat_service.chat(
                query=query,
                history=history,
                model_name=model_name,
                api_key=api_key
            )

        self.store.add_message(conversation_id, Message(role="user", content=query, model_name=model_name))
        self.store.add_message(conversation_id, Message(role="assistant", content=response, model_name=model_name))

        return response