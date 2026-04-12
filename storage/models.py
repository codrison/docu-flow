from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    user_id: str
    name: str
    email: str


class Conversation(BaseModel):
    conversation_id: str
    user_id: str
    title: str = None
    namespace: str = None
    created_at: datetime = None


class Message(BaseModel):
    role: str
    content: str
    model_name: str