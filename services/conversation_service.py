from storage.conversation import InMemory
from services.chat_service import ChatService
from services.rag_service import RAGService

class ConversationService:
    def __init__(self, store: InMemory, chat_service: ChatService, rag_service: RAGService):
        self.store = store
        self.chat_service = chat_service
        self.rag_service = rag_service

    def create_conversation(self, conversation_id: str, created_at=None, kb_ids: list[str] = None, title: str = None):
        self.store.create_conversation(conversation_id=conversation_id,
                                       created_at=created_at,
                                       kb_ids=kb_ids,
                                       title=title)

    def chat(self, conversation_id: str, query: str, use_rag: bool, model_name: str, api_key: str, **kwargs):
        
        

        # 2. Fetch History
        history = self.store.get_conversation(conversation_id)["messages"]
        
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
        self.store.add_message(conversation_id,
                               role="user",
                               content=query,
                               model=model_name)
        
        self.store.add_message(conversation_id=conversation_id, 
                               role="assistant", 
                               content=response, 
                               model=model_name)
        
        return response