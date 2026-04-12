from fastapi import APIRouter

# App Imports
from api.v1.schemas.conversations import CreateConversation, ResponseConversation, SendMessage
from api.v1.dependencies import conversation_service, store
from datetime import datetime

router = APIRouter()

@router.post("/conversations/", response_model=ResponseConversation)
def create_conversation(data: CreateConversation):
    # Generating Conversation ID
    conversation_id = conversation_service.create_conversation(
        title=data.title,
        model_name=data.model_name,
        kb_ids=data.kb_ids
    )
   
    return ResponseConversation(
       conversation_id=conversation_id,
       title=data.title,
       model_name=data.model_name,
       created_at=datetime.now()
    )

@router.post("/conversations/{conversation_id}/chat")
def send_message(conversation_id: str, data: SendMessage):
    response = conversation_service.chat(
        conversation_id=conversation_id,
        query=data.query,
        model_name=data.model_name,
        api_key=data.api_key,
        name_space=data.name_space
    )

    return response

@router.delete("/conversations/{conversation_id}")
def delete_conversation(conversation_id: str):
    store.delete_conversation(conversation_id=conversation_id)


@router.get("/conversations/")
def get_history():
    return store.get_history()