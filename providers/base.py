from config import ModelConfig


class BaseProvider:
    def __init__(self, config: ModelConfig):
        self.config = config

    def get_model(self):
        raise NotImplementedError("Subclasses must implement this method")