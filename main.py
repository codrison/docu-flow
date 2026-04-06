# from config import ModelConfig


# config = ModelConfig(provider="google", model_name="gemini-2.5-flash", api_key=api_key)


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

from config import EmbeddingConfig, IngestionConfig, VectorStoreConfig
from ingestion.embedder import Embedder
from ingestion.loader import DataLoader
from ingestion.chunker import Chunker
from ingestion.vector_store import VectorStore


if __name__ == "__main__":
    print("Starting ingestion process...")


    print("Loading documents...")
    loader = DataLoader("./sample.json")
    documents = loader.load()
    print("Documents", documents)


    print("Chunking documents...")
    chunker = Chunker(IngestionConfig(chunk_size=1000, chunk_overlap=200))
    chunks = chunker.chunk(documents)
    print("Chunks", chunks)

    print("Storing embeddings in vector store...")
    vector_store = VectorStore(VectorStoreConfig(provider="pinecone", api_key="pcsk_37VQ9v_PE1gFCN6aFXo5WfcNjHK1Pf1QWm7VEn5hpCAcuNb76AG2g9TdCpv8B3GMFh83Da"))
    vector_store.add_documents(chunks, namespace="test_namespace")
    print("Ingestion process completed.")