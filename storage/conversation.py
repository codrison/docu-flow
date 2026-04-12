from storage.models import User, Conversation, Message

# ---------- Store ----------

class InMemory:
    def __init__(self):
        # "Table" 1: users — keyed by user_id
        self.users: dict = {}

        # "Table" 2: conversations — keyed by conversation_id
        # mirrors a real conversations table with user_id as foreign key
        self.conversations: dict = {}

        # Lightweight index: user_id -> list of conversation_ids
        # In a real DB this is just a WHERE clause — here we maintain it manually
        self._user_conversation_index: dict = {}

    # ---- User ----

    def create_user(self, user: User):
        if user.user_id in self.users:
            raise ValueError(f"User '{user.user_id}' already exists.")
        self.users[user.user_id] = {
            "name": user.name,
            "email": user.email,
        }
        self._user_conversation_index[user.user_id] = []

    def get_user(self, user_id: str) -> dict:
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' not found.")
        return self.users[user_id]

    # ---- Conversation ----

    def create_conversation(self, conversation: Conversation):
        if conversation.user_id not in self.users:
            raise ValueError(f"User '{conversation.user_id}' does not exist. Create user first.")
        if conversation.conversation_id in self.conversations:
            raise ValueError(f"Conversation '{conversation.conversation_id}' already exists.")

        self.conversations[conversation.conversation_id] = {
            "user_id": conversation.user_id,          # foreign key — mirrors real DB
            "title": conversation.title,
            "created_at": conversation.created_at or datetime.now(),
            "messages": [],                            # embedded — this is the MongoDB part
        }

        # Update manual index
        self._user_conversation_index[conversation.user_id].append(conversation.conversation_id)

    def get_conversation(self, conversation_id: str) -> dict:
        if conversation_id not in self.conversations:
            raise ValueError(f"Conversation '{conversation_id}' not found.")
        return self.conversations[conversation_id]

    def delete_conversation(self, conversation_id: str):
        if conversation_id not in self.conversations:
            raise ValueError(f"Conversation '{conversation_id}' not found.")

        user_id = self.conversations[conversation_id]["user_id"]

        # Keep both tables consistent — like a cascading delete
        del self.conversations[conversation_id]
        self._user_conversation_index[user_id].remove(conversation_id)

    # ---- Messages ----

    def add_message(self, conversation_id: str, message: Message):
        if conversation_id not in self.conversations:
            raise ValueError(f"Conversation '{conversation_id}' not found.")

        self.conversations[conversation_id]["messages"].append({
            "role": message.role,
            "content": message.content,
            "model_name": message.model_name,
        })

    def get_messages(self, conversation_id: str) -> list:
        if conversation_id not in self.conversations:
            raise ValueError(f"Conversation '{conversation_id}' not found.")
        return self.conversations[conversation_id]["messages"]

    # ---- User History ----

    def get_user_conversations(self, user_id: str) -> list:
        """All conversations for a user. Mirrors: SELECT * FROM conversations WHERE user_id = ?"""
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' not found.")

        conv_ids = self._user_conversation_index[user_id]
        return [
            {"conversation_id": cid, **self.conversations[cid]}
            for cid in conv_ids
        ]


# ---------- Main ----------

if __name__ == "__main__":
    store = InMemory()

    # Create user
    user = User(user_id="u001", name="Alice", email="alice@example.com")
    store.create_user(user)

    # Create conversations
    conv1 = Conversation(conversation_id="c001", user_id="u001", title="First Chat")
    conv2 = Conversation(conversation_id="c002", user_id="u001", title="Second Chat")
    store.create_conversation(conv1)
    store.create_conversation(conv2)

    # Add messages
    store.add_message("c001", Message(role="user", content="Hello!", model_name="claude-sonnet-4-6"))
    store.add_message("c001", Message(role="assistant", content="Hi Alice!", model_name="claude-sonnet-4-6"))
    store.add_message("c002", Message(role="user", content="New topic", model_name="claude-sonnet-4-6"))

    # Fetch
    print("=== Conversation c001 ===")
    print(store.get_conversation("c001"))

    print("\n=== Alice's Conversations ===")
    for c in store.get_user_conversations("u001"):
        print(c)

    # Delete
    store.delete_conversation("c001")
    print("\n=== After deleting c001 ===")
    print("Remaining conversations:", list(store.conversations.keys()))
    print("Index:", store._user_conversation_index)