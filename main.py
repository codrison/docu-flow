import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(".env.local")

api_key = os.getenv("GEMINI_API_KEY")

model = init_chat_model("google_genai:gemini-2.5-flash-lite", api_key=api_key)

response = model.invoke("Hi, How are you?")
print(response.content)
