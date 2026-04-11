from pydantic import BaseModel
from datetime import datetime


class ConversationCreate(BaseModel):
    model: str
    kb_ids: list[str] = []

class ConversationResponse(BaseModel):
    title: str | None = None
    conversation_id: str
    model: str
    kb_ids: list[str] = []
    created_at: datetime
