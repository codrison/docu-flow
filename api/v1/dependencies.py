# Environment and Configuration
import os
from dotenv import load_dotenv


load_dotenv(".env.local")

gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")




# Import Imports

# Conversation Manager
from services.conversation_service import ConversationService

# Memory Store
from storage.conversation import InMemory

# Vector Store
from ingestion.vector_store import VectorStore

# Chat Service
from services.chat_service import ChatService

# RAG Service
from services.rag_service import RAGService

# Config File
from config import VectorStoreConfig


store = InMemory()
vector_store = VectorStore(config=VectorStoreConfig(api_key=pinecone_api_key,
                                                    model_name="llama-text-embed-v2"))
chat_service = ChatService()
rag_service = RAGService(vector_store=vector_store, 
                         chat_service=chat_service)

conversation_service = ConversationService(store=store, 
                                           chat_service=chat_service,
                                           rag_service=rag_service)


