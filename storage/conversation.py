from datetime import datetime

class InMemory:
    def __init__(self):
        self.conversations = {}
    
    def create_conversation(self, conversation_id, created_at: datetime = None, kb_ids: list[str] = None, model: str = None, title: str = None):
        if conversation_id in self.conversations:
            raise ValueError("Conversation ID already exists.")
        self.conversations[conversation_id] = { "kb_ids": kb_ids or [], "title": title, "created_at": created_at, "messages": []}
    
    def add_message(self, conversation_id, model: str = None, role: str = None, content: str = None):
        if conversation_id not in self.conversations:
            raise ValueError("Conversation ID does not exist.")
        self.conversations[conversation_id]["messages"].append({"role": role, "content": content, "model": model})

    def get_conversation(self, conversation_id):
        if conversation_id not in self.conversations:
            raise ValueError("Conversation does not exist.")
        return self.conversations[conversation_id]
    


if __name__ == "__main__":
    memory = InMemory()
    memory.create_conversation("test_conversation")
    # memory.add_message("test_conversation", "user", "Hello, how are you?")
    # memory.add_message("test_conversation", "assistant", "I'm good, thank you! How can I assist you today?")
    print(memory.get_conversation("test_conversation"))
