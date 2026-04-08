from providers.base import BaseProvider
from langchain_google_genai import ChatGoogleGenerativeAI


class GoogleProvider(BaseProvider):
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def get_model(self) -> ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(model=self.model_name, api_key=self.api_key)