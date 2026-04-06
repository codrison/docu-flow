class ConversationService:
    def __init__(self):
        self.conversations = {}
    
    def create_conversation(self, conversation_id):
        if conversation_id in self.conversations:
            raise ValueError("Conversation ID already exists.")
        self.conversations[conversation_id] = []
    
    def add_message(self, conversation_id, role, content):
        if conversation_id not in self.conversations:
            raise ValueError("Conversation ID does not exist.")
        self.conversations[conversation_id].append({"role": role, "content": content})

    def get_conversation(self, conversation_id):
        if conversation_id not in self.conversations:
            raise ValueError("Conversation does not exist.")
        return self.conversations[conversation_id]