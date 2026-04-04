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

from config import EmbeddingConfig, IngestionConfig
from ingestion.embedder import Embedder
from ingestion.loader import DataLoader
from ingestion.chunker import Chunker

if __name__ == "__main__":
    loader = DataLoader("./sample.json")
    documents = loader.load()
    chunker = Chunker(IngestionConfig())
    chunks = chunker.chunk(documents)
    embedding_config = EmbeddingConfig(model_name="llama-text-embed-v2", api_key="pcsk_37VQ9v_PE1gFCN6aFXo5WfcNjHK1Pf1QWm7VEn5hpCAcuNb76AG2g9TdCpv8B3GMFh83Da")
    embedder = Embedder(embedding_config)
    query_embedding = embedder.embed_documents(chunks)
    print(query_embedding)