from config import ModelConfig
from providers.base import BaseProvider
from providers.google import GoogleProvider

PROVIDERS = {
    "google": GoogleProvider,
}


class ProvideFactory:
    @staticmethod
    def get_provider(config: ModelConfig) -> BaseProvider:
        provider_class = PROVIDERS.get(config.provider.lower())
        if not provider_class:
            raise ValueError(f"Unsupported provider: {config.provider}")
        return provider_class(config)
    


config = ModelConfig(provider="google", model_name="gemini-1.5-pro", api_key="your_api_key")
provider = ProvideFactory.get_provider(config)
model = provider.get_model()
print(model)