from config import ModelConfig
import os
from dotenv import load_dotenv

load_dotenv(".env.local")
google_api_key = os.getenv("GEMINI_API_KEY")

# config = ModelConfig(provider="google", model_name="gemini-2.5-flash", api_key=google_api_key)


# if __name__ == "__main__":
#     from services.chat_service import ChatService

#     chat_service = ChatService(config)
#     output = chat_service.chat("How are you?")
#     print(output)




# from ingestion.loader import DataLoader
# from ingestion.chunker import Chunker
# from config import IngestionConfig

# if __name__ == "__main__":
#     data_loader = DataLoader("./sample.json")
#     documents = data_loader.load()
#     chunker = Chunker(IngestionConfig())
#     chunks = chunker.chunk(documents)
#     print(chunks)   

# ........................................................


# from config import IngestionConfig, VectorStoreConfig
# from ingestion.loader import DataLoader
# from ingestion.chunker import Chunker
# from ingestion.vector_store import VectorStore


# if __name__ == "__main__":
#     print("Starting ingestion process...")


#     print("Loading documents...")
#     loader = DataLoader("./sample.json")
#     documents = loader.load()
#     print("Documents", documents)


#     print("Chunking documents...")
#     chunker = Chunker(IngestionConfig(chunk_size=1000, chunk_overlap=200))
#     chunks = chunker.chunk(documents)
#     print("Chunks", chunks)

#     print("Storing embeddings in vector store...")
#     vector_store = VectorStore(VectorStoreConfig(provider="pinecone"))
#     vector_store.add_documents(chunks, namespace="test_namespace")
#     print("Ingestion process completed.")



from services.rag_service import RAGService
from services.chat_service import ChatService
from storage.conversation import InMemory
from ingestion.vector_store import VectorStore
from config import VectorStoreConfig, ModelConfig

import os
from dotenv import load_dotenv

load_dotenv(".env.local")
google_api_key = os.getenv("GEMINI_API_KEY")
api_key = os.getenv("PINECONE_API_KEY")

if __name__ == "__main__":
    # print("Starting RAG service...")

    # # Initialize vector store
    # vector_store = VectorStore(VectorStoreConfig(api_key=api_key))

    # # Initialize chat service
    # chat_service = ChatService(ModelConfig(provider="google", model_name="gemini-2.5-flash", api_key=google_api_key))

    # # Initialize RAG service
    # rag_service = RAGService(vector_store, chat_service, ConversationService())

    # # Test RAG service
    # query = "What is DocuFlow?"
    # response = rag_service.chat(query, namespace="test_namespace")
    # print("Response:", response)

    conversation_service = InMemory()
    print(conversation_service.conversations)