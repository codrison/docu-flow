from base import BaseProvider
from config import ModelConfig

from langchain_google_genai import ChatGoogleGenerativeAI


class GoogleProvider(BaseProvider):
    def __init__(self, config: ModelConfig):
        super().__init__(config)

    def get_model(self):
        return ChatGoogleGenerativeAI(model=self.config.model_name, api_key=self.config.api_key)

