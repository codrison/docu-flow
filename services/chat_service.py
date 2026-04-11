from providers.factory import ProvideFactory
from prompts.chat import build_messages


class ChatService:

    def chat(self, query: str, history: list, model_name: str, api_key: str) -> str:
        messages = build_messages(query, history)
        model = ProvideFactory.get_provider(model_name, api_key).get_model()
        response =  model.invoke(messages)
        return response.content
