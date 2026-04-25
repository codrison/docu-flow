# api/v1/routes/conversations.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from storage.database import get_db
from storage.models import User
from api.v1.schemas.conversations import (
    CreateConversation,
    ConversationResponse,
    SendMessage,
    MessageResponse,
)
from api.v1.dependencies import current_user, conversation_service

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("/", response_model=ConversationResponse, status_code=status.HTTP_201_CREATED)
def create_conversation(
    data: CreateConversation,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    conv = conversation_service.create_conversation(
        db=db,
        user_id=user.id,
        title=data.title,
        model_name=data.model_name,
    )
    return conv


@router.get("/", response_model=list[ConversationResponse])
def list_conversations(
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    return conversation_service.list_conversations(db=db, user_id=user.id)


@router.get("/{conversation_id}", response_model=ConversationResponse)
def get_conversation(
    conversation_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    conv = conversation_service.get_conversation(db=db, conversation_id=conversation_id, user_id=user.id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return conv


@router.get("/{conversation_id}/messages", response_model=list[MessageResponse])
def get_messages(
    conversation_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    conv = conversation_service.get_conversation(db=db, conversation_id=conversation_id, user_id=user.id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return conv.messages


@router.post("/{conversation_id}/messages", response_model=MessageResponse)
def send_message(
    conversation_id: str,
    data: SendMessage,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    try:
        response_text = conversation_service.chat(
            db=db,
            conversation_id=conversation_id,
            user_id=user.id,
            query=data.query,
            api_key=data.api_key,
            kb_id=data.kb_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    # Return the assistant message that was just persisted
    conv = conversation_service.get_conversation(db=db, conversation_id=conversation_id, user_id=user.id)
    return conv.messages[-1]


@router.delete("/{conversation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conversation(
    conversation_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
):
    deleted = conversation_service.delete_conversation(db=db, conversation_id=conversation_id, user_id=user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Conversation not found.")