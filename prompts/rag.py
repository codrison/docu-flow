from langchain_core.documents import Document

class RAG:
    def build_messages(self, relevant_docs, query, history):
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        prompt = f"Context: \n{context}\n\n Question: {query}"

        return [
            {"role": "system", "content": "system_prompt"},
            *history,
            {"role": "user", "content": prompt}
        ]
