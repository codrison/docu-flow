def build_messages(system_prompt, history, query, relevant_docs):
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Context:\n{context}\n\nQuestion: {query}"
    
    return [
        {"role": "system", "content": system_prompt},
        *history,
        {"role": "user", "content": prompt}
    ]