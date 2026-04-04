from config import ModelConfig

from providers.factory import ProvideFactory

class ChatService:
    def __init__(self, config: ModelConfig):
        self.config = config
        self.model = ProvideFactory.get_provider(config).get_model()

    def chat(self, messages: list):
        response =  self.model.invoke(messages)
        return response.content
