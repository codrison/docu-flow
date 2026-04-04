# from config import ModelConfig


# config = ModelConfig(provider="google", model_name="gemini-2.5-flash", api_key=api_key)


# if __name__ == "__main__":
#     from services.chat_service import ChatService

#     chat_service = ChatService(config)
#     output = chat_service.chat("How are you?")
#     print(output)




from ingestion.loader import DataLoader

if __name__ == "__main__":
    data_loader = DataLoader("./sample.json")
    documents = data_loader.load()
    print(documents)