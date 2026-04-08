from providers.factory import ProvideFactory

class ChatService:

    def chat(self, messages: list, model_name: str = None, api_key: str = None) -> str:
        model = ProvideFactory.get_provider(model_name, api_key).get_model()
        response =  model.invoke(messages)
        return response.content


