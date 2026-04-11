from services.conversation_service import ConversationService

conversation_service : ConversationService = None


def get_conversation_service() -> ConversationService:
    return conversation_service