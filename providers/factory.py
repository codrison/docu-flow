from providers.base import BaseProvider
from providers.google_provider import GoogleProvider


MODEL_PROVIDER_MAP = {
    "gemini-1.5-pro": "google",
    "gemini-2.0-flash": "google",
    "gemini-2.5-flash": "google",
    "gpt-4o": "openai",
    "gpt-4o-mini": "openai",
}

PROVIDERS = {
    "google": GoogleProvider,
    # "openai": OpenAIProvider,
}


class ProvideFactory:
    @staticmethod
    def get_provider(model_name: str, api_key: str) -> BaseProvider:
        provider_name = MODEL_PROVIDER_MAP.get(model_name.lower())
        print(f"Provider name: {provider_name}")
        if not provider_name:
            raise ValueError(f"Unsupported model: {model_name}")
        provider_class = PROVIDERS.get(provider_name)
        print(f"Provider class: {provider_class}")
        return provider_class(model_name=model_name, api_key=api_key)
        