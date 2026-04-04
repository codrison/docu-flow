from config import ModelConfig

from abc import ABC, abstractmethod 

class BaseProvider(ABC):
    def __init__(self, config: ModelConfig):
        self.config = config

    @abstractmethod
    def get_model(self):
        pass