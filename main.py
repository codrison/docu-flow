from config import ModelConfig

api_key = "AIzaSyC5SmZITz7OHNFoLC4znygVDE7WmcOOL4w"

config = ModelConfig(provider="google", model_name="gemini-2.5-flash", api_key=api_key)


if __name__ == "__main__":
    from services.chat_service import ChatService

    chat_service = ChatService(config)
    output = chat_service.chat("How are you?")
    print(output)