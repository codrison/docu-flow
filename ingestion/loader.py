import os
from langchain_community.document_loaders import JSONLoader, CSVLoader,PyPDFLoader, TextLoader

LOADERS = {
    "json": JSONLoader,
    "csv": CSVLoader,
    "pdf": PyPDFLoader,
    "txt": TextLoader,
}

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        ext = os.path.splitext(file_path)[1].lower()
        data_type = ext[1:]  # Remove the dot
        self.loader_class = LOADERS.get(data_type)
        if not self.loader_class:
            raise ValueError(f"Unsupported data type: {data_type}")
        
    
    def load(self):
        if isinstance(self.loader_class, type) and self.loader_class.__name__ == "JSONLoader":
            loader = self.loader_class(self.file_path, jq_schema=".", text_content=False)
        else:
            loader = self.loader_class(self.file_path)
        return loader.load()