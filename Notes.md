SSE VS WEB Sockets
Strategy Pattern
Use ABC for catching error immediatly rather then at run time.

## The patterns you used:
Strategy Pattern — swappable providers behind a common interface
Factory Pattern — one place to decide which provider to create
Utility Class or Helper Class - 


# DocuFlow Dev Notes

## Design Decisions

### Dependency Injection
**Date:** 2026-04-06
**Decision:** Always pass dependencies as parameters, don't instantiate inside classes.
**Why:** Loose coupling, easier to swap, easier to test.
**Example:** VectorStore receives Embedder, doesn't create it.

### Strategy + Factory Pattern
**Date:** 2026-04-06
**Decision:** Used for multi-provider LLM support.
**Why:** Adding new provider = one new class + one line in factory dict.

### SSE over WebSockets
**Date:** 2026-04-06
**Decision:** Used SSE for streaming AI responses.
**Why:** One directional only. Client asks once, server streams back. SSE is simpler.