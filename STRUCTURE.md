# DocuFlow Project Structure

```
DocuFlow/
├── api/                          # API endpoints and routing
│   ├── __init__.py
│   └── v1/                       # API v1
│       ├── __init__.py
│       ├── dependencies.py       # Dependency injection
│       ├── routes/
│       │   ├── __init__.py
│       │   └── conversations.py  # Conversation endpoints
│       └── schemas/
│           ├── __init__.py
│           └── conversations.py  # Data schemas
│
├── ingestion/                    # Document ingestion pipeline
│   ├── chunker.py               # Text chunking logic
│   ├── loader.py                # Document loading
│   └── vector_store.py          # Vector database operations
│
├── prompts/                      # Prompt templates
│   ├── chat.py                  # Chat prompts
│   └── rag.py                   # RAG prompts
│
├── providers/                    # LLM provider implementations
│   ├── base.py                  # Base provider class
│   ├── factory.py               # Provider factory pattern
│   └── google_provider.py       # Google AI provider
│
├── services/                     # Business logic services
│   ├── chat_service.py          # Chat service
│   ├── conversation_service.py  # Conversation management
│   └── rag_service.py           # RAG service
│
├── storage/                      # Data persistence
│   └── conversation.py          # Conversation storage models
│
├── main.py                       # Application entry point
├── config.py                     # Configuration settings
├── pyproject.toml               # Project metadata & dependencies
├── Design.md                    # Design documentation
├── README.md                    # Project documentation
├── Notes.md                     # Development notes
├── practices.md                 # Best practices guide
└── sample.json                  # Sample data
```

## Module Overview

| Module | Purpose |
|--------|---------|
| **api/** | RESTful API endpoints, routing, and request/response schemas |
| **ingestion/** | Document processing, chunking, and vector store integration |
| **prompts/** | LLM prompt templates for different use cases |
| **providers/** | Abstraction layer for different LLM providers |
| **services/** | Business logic and orchestration |
| **storage/** | Data models and persistence layer |

