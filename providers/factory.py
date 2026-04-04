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