import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")
google_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

from services.conversation_service import ConversationService
from storage.conversation import InMemory
from services.chat_service import ChatService
from services.rag_service import RAGService
from ingestion.vector_store import VectorStore
from config import VectorStoreConfig

if __name__ == "__main__":
    # 1. Setup Configuration
    config = VectorStoreConfig(api_key=pinecone_api_key)

    # 2. Initialize Core components
    vector_store = VectorStore(config)
    store = InMemory()
    
    # 3. Initialize Services
    chat_service = ChatService()
    rag_service = RAGService(vector_store, chat_service)
    
    # 4. Initialize Orchestrator
    conversation_service = ConversationService(store, chat_service, rag_service)

    # 5. Run Test Call (Standard Chat)
    print("--- Testing Standard Chat ---")
    response_1 = conversation_service.chat(
        conversation_id="test_session_001",
        query="Hi, I am Hanan. Please remember my name.",
        use_rag=False,
        model_name="gemini-2.0-flash",
        api_key=google_api_key
    )
    print(f"Assistant: {response_1}")

    # 6. Run Test Call (Follow-up to check history)
    print("\n--- Testing History Persistence ---")
    response_2 = conversation_service.chat(
        conversation_id="test_session_001",
        query="What is my name?",
        use_rag=False,
        model_name="gemini-2.0-flash",
        api_key=google_api_key
    )
    print(f"Assistant: {response_2}")