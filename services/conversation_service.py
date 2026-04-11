from storage.conversation import InMemory
from services.chat_service import ChatService
from services.rag_service import RAGService

class ConversationService:
    def __init__(self, store: InMemory, chat_service: ChatService, rag_service: RAGService):
        self.store = store
        self.chat_service = chat_service
        self.rag_service = rag_service

    def chat(self, conversation_id: str, query: str, use_rag: bool, model_name: str, api_key: str, **kwargs):
        # 1. Implicitly create conversation if it doesn't exist
        if conversation_id not in self.store.conversations:
            self.store.conversations[conversation_id] = []

        # 2. Fetch History
        history = self.store.get_conversation(conversation_id)
        
        # 3. Get Response
        if use_rag:
            # RAGService requires: query, history, namespace, model_name, api_key
            response = self.rag_service.chat(
                query=query, 
                history=history, 
                model_name=model_name, 
                api_key=api_key, 
                **kwargs
            )
        else: 
            # ChatService requires: query, history, model_name, api_key
            response = self.chat_service.chat(
                query=query, 
                history=history, 
                model_name=model_name, 
                api_key=api_key
            )
            
        # 4. Log both query and response
        self.store.add_message(conversation_id, "user", query)
        self.store.add_message(conversation_id, "assistant", response)
        
        return response