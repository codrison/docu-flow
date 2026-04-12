from fastapi import FastAPI
import uvicorn

from api.v1.routes.conversations import router


# Environment
import os
from dotenv import load_dotenv

load_dotenv(".env.local")

google_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Imports
from storage.conversation import InMemory
from ingestion.vector_store import VectorStore
from services.chat_service import ChatService
from services.rag_service import RAGService
from services.conversation_service import ConversationService


from config import VectorStoreConfig

app = FastAPI()


# register your router here
app.include_router(router)


# Configurations
config = VectorStoreConfig(api_key=pinecone_api_key)

# Calling Dependencies
store = InMemory()
vector_store = VectorStore(config)

chat_service = ChatService()
rag_service = RAGService(vector_store=vector_store, 
                         chat_service=chat_service)

conversation_service = ConversationService(store=store,
                                           chat_service=chat_service,
                                           rag_service=rag_service)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)