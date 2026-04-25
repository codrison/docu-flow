# api/v1/schemas/conversations.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateConversation(BaseModel):
    title: Optional[str] = None
    model_name: str


class ConversationResponse(BaseModel):
    id: str
    title: Optional[str] = None
    model_name: str
    created_at: datetime

    model_config = {"from_attributes": True}


class SendMessage(BaseModel):
    query: str
    api_key: str                        # user provides their own key per message
    kb_id: Optional[str] = None        # null = plain chat, set = RAG against that KB


class MessageResponse(BaseModel):
    id: str
    role: str
    content: str
    kb_id: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}