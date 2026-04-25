# services/conversation_service.py

from sqlalchemy.orm import Session
from storage.models import Conversation, Message, KnowledgeBase
from services.chat_service import ChatService
from services.rag_service import RAGService
from datetime import datetime
from uuid import uuid4


class ConversationService:
    def __init__(self, chat_service: ChatService, rag_service: RAGService):
        # No store injected — receives db session per call instead
        self.chat_service = chat_service
        self.rag_service = rag_service

    # ---- Conversation CRUD ----

    def create_conversation(self, db: Session, user_id: str, title: str, model_name: str) -> Conversation:
        conv = Conversation(
            id=str(uuid4()),
            user_id=user_id,
            title=title,
            model_name=model_name,
        )
        db.add(conv)
        db.commit()
        db.refresh(conv)
        return conv

    def get_conversation(self, db: Session, conversation_id: str, user_id: str) -> Conversation:
        conv = db.query(Conversation).filter(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id,      # users can only access their own
        ).first()
        return conv

    def list_conversations(self, db: Session, user_id: str) -> list[Conversation]:
        return (
            db.query(Conversation)
            .filter(Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
            .all()
        )

    def delete_conversation(self, db: Session, conversation_id: str, user_id: str) -> bool:
        conv = self.get_conversation(db, conversation_id, user_id)
        if not conv:
            return False
        db.delete(conv)
        db.commit()
        return True

    # ---- Chat ----

    def chat(
        self,
        db: Session,
        conversation_id: str,
        user_id: str,
        query: str,
        api_key: str,
        kb_id: str | None = None,
    ) -> str:
        conv = self.get_conversation(db, conversation_id, user_id)
        if not conv:
            raise ValueError(f"Conversation '{conversation_id}' not found.")

        # Build history from DB messages (role + content only, what the LLM needs)
        history = [
            {"role": m.role, "content": m.content}
            for m in conv.messages
        ]

        if kb_id:
            # Validate KB belongs to this user
            kb = db.query(KnowledgeBase).filter(
                KnowledgeBase.id == kb_id,
                KnowledgeBase.user_id == user_id,
            ).first()
            if not kb:
                raise ValueError(f"Knowledge base '{kb_id}' not found.")

            response = self.rag_service.chat(
                query=query,
                history=history,
                namespace=kb.namespace,
                model_name=conv.model_name,
                api_key=api_key,
            )
        else:
            response = self.chat_service.chat(
                query=query,
                history=history,
                model_name=conv.model_name,
                api_key=api_key,
            )

        # Persist both turns
        db.add(Message(conv_id=conversation_id, role="user", content=query, kb_id=kb_id))
        db.add(Message(conv_id=conversation_id, role="assistant", content=response, kb_id=kb_id))
        db.commit()

        return response