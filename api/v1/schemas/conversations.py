from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict

class CreateConversation(BaseModel):
    title: Optional[str] = None
    model_name: str
    api_key: str
    kb_ids: Optional[list[str]] = None


class ResponseConversation(BaseModel):
    conversation_id: str
    title: Optional[str] = None
    model_name: str
    created_at: datetime = Field(default_factory=datetime.now) # Need to understand the use of Field()


class SendMessage(BaseModel):
    query: str
    model_name = str
    api_key: str  # Temporary, remove when auth is added
    name_space: Optional[str] = None



