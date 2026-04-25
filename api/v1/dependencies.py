# api/v1/dependencies.py

import os
from dotenv import load_dotenv

load_dotenv(".env.local")

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError

from storage.database import get_db
from storage.models import User
from api.v1.auth_utils import decode_access_token
from services.conversation_service import ConversationService
from services.chat_service import ChatService
from services.rag_service import RAGService
from ingestion.vector_store import VectorStore
from config import VectorStoreConfig

# ---------- Vector store (Pinecone) ----------
_pinecone_api_key = os.getenv("PINECONE_API_KEY")

vector_store = VectorStore(
    config=VectorStoreConfig(api_key=_pinecone_api_key, model_name="llama-text-embed-v2")
)

# ---------- Services ----------
chat_service = ChatService()
rag_service = RAGService(vector_store=vector_store, chat_service=chat_service)
conversation_service = ConversationService(chat_service=chat_service, rag_service=rag_service)

# ---------- Auth guard ----------
_bearer = HTTPBearer()


def current_user(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
    db: Session = Depends(get_db),
) -> User:
    """Inject this into any route that requires authentication."""
    try:
        user_id = decode_access_token(credentials.credentials)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token.")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found.")
    return user