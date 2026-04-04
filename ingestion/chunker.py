from config import IngestionConfig
from langchain_text_splitters import RecursiveCharacterTextSplitter



class Chunker:
    def __init__(self, config: IngestionConfig):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap
        )

    def chunk(self, documents):
        return self.text_splitter.split_documents(documents)
