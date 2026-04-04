class ModelConfig:
    def __init__(self, provider: str, model_name: str, api_key: str):
        self.provider = provider
        self.model_name = model_name
        self.api_key = api_key


class IngestionConfig:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap


class EmbeddingConfig:
    def __init__(self, model_name: str, api_key: str, environment: str = None):
        self.model_name = model_name
        self.api_key = api_key
        self.environment = environment