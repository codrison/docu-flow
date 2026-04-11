from fastapi import APIRouter, Depends
from api.v1.schemas.conversations import ConversationCreate, ConversationResponse
from api.v1.dependencies import get_conversation_service
from services.conversation_service import ConversationService
from datetime import datetime
from uuid import uuid4

router = APIRouter(prefix="/conversations", tags=["conversations"])

@router.post("/", response_model=ConversationResponse)
async def create_conversation(
    conversation: ConversationCreate,
    service: ConversationService = Depends(get_conversation_service)
):
    conversation_id = str(uuid4())
    created_at = datetime.now()

    service.create_conversation(
        conversation_id=conversation_id,
        created_at=created_at,
        kb_ids=conversation.kb_ids,
        title=None
    )

    return ConversationResponse(
        conversation_id=conversation_id,
        model=conversation.model,
        kb_ids=conversation.kb_ids,
        created_at=created_at,
        title=None
    )