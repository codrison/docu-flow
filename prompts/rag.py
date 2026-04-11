def build_messages(relevant_docs, query, history, system_prompt):
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Context: \n{context}\n\n Question: {query}"

    return [
        {"role": "system", "content": system_prompt},
        *history,
        {"role": "user", "content": prompt}
    ]
