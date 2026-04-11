def build_messages(query: str, history: list, system_prompt: str = "You are a helpful assistant."):
    return [
        {"role": "system", "content": system_prompt},
        *history,
        {"role": "user", "content": query}
    ]
