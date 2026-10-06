# Migrating from `supermemory` 3.x to 5.x

Starting with **5.0.0**, the Python SDK is generated from the Supermemory **v5 API** (`/v5/openapi`) using Fern's open-source generator instead of Stainless. The method names match the TypeScript SDK ([sdk-ts](https://github.com/supermemoryai/sdk-ts)) v5.

v5 is namespace-first. Every content operation is scoped to a namespace, which replaces container tags, and the namespace is passed as the first argument.

```sh
pip install --pre supermemory   # while 5.0 is in release candidate
```

## TL;DR

Only the API methods change. Everything around them works as before:

| | 3.x | 5.x |
|---|---|---|
| Import / auth / env vars | `from supermemory import Supermemory`, `SUPERMEMORY_API_KEY`, `SUPERMEMORY_BASE_URL` | unchanged |
| Client options | `api_key`, `base_url`, `timeout`, `max_retries`, `default_headers`, `default_query`, `http_client` | unchanged |
| Per-call options | `extra_headers`, `extra_query`, `extra_body`, `timeout`; `client.with_options(...)` | unchanged |
| Retries / timeout | 2 retries, 60s | unchanged |
| Errors | `supermemory.APIStatusError`, `NotFoundError`, `RateLimitError`, `APIConnectionError`, … | unchanged |
| Raw responses | `client.with_raw_response.<method>(...).parse()` | unchanged |
| Models | `.to_dict()`, `.to_json()` | unchanged |
| Scoping | `container_tag` / `container_tags` in the body | `namespace` positional argument (one per call) |
| Add | `client.add(content=..., container_tag="u")` | `client.add("u", content=...)` |
| Search | `client.search.memories(q=...)` | `client.search("u", query=...)` |
| Profile | profile + optional search (`q`) | profile only. Run `client.search` alongside it |
| Python | 3.9+ | 3.10+ |

## Method map

| 3.x call | 5.x call |
|---|---|
| `client.add(...)` / `client.documents.add(...)` | `client.add(namespace, content=...)` |
| `client.search.memories(...)` / `client.search.documents(...)` | `client.search(namespace, query=...)` |
| `client.profile(...)` | `client.profile(namespace)` |
| `client.documents.list(...)` / `client.memories.list(...)` | `client.list(namespace, "documents" \| "chunks" \| "memories")` |
| `client.documents.get(id)` | `client.documents.get(namespace, id)` |
| `client.documents.update(id, ...)` | `client.documents.update(namespace, id, ...)` |
| `client.documents.delete(...)` / `delete_bulk(...)` | `client.documents.delete(namespace, ids=[...])` |
| `client.documents.batch_add(...)` | `client.documents.batch_add(namespace, documents=[...])` |
| `client.documents.upload_file(...)` | `client.documents.upload_file(namespace, file=...)` |
| — | `client.documents.replace_with_file(...)`, `update_file(...)` |
| `client.memories.forget(...)` | `client.memories.forget(namespace, ids=[...])` |
| — | `client.memories.forget_matching(...)` |
| — | `client.profiles.{get_buckets, set_buckets, delete_buckets}` |
| `client.connections.*` | `client.connectors.{list_all, list, create, get, update, delete, sync}` |
| container tag management | `client.namespaces.{list, get, update, delete}` |
| `client.settings.{get, update}` | `client.organization.{get, update}` |

### Renamed request fields

| 3.x | 5.x |
|---|---|
| `container_tag` / `container_tags` | `namespace` (first argument) |
| `custom_id` | `id` |
| `q` | `query` |
| `filters` | `filter` (typed filter expression) |
| `include` | `include` (a list on GETs, a dict on search) |
| search `timing` / `total` | `search_time` |

## Profile no longer searches

```python
import asyncio
from supermemory import AsyncSupermemory

client = AsyncSupermemory()

profile, search = await asyncio.gather(
    client.profile("user_alex"),
    client.search("user_alex", query="upcoming meetings"),
)
```

## Several container tags

v5 operations take exactly one namespace. To search several, fan out and merge:

```python
responses = await asyncio.gather(*(client.search(ns, query="roadmap") for ns in ["user_alex", "team_design"]))
results = [r for resp in responses for r in resp.results]
```

## Smaller differences

- Response types are generated from the v5 spec, so their names changed (e.g. `SearchMemoriesResponse` became `SearchResponse`). Import them from `supermemory.types`.
- `client.with_streaming_response` is gone. None of the v5 endpoints stream.
- `NOT_GIVEN` is gone. Leave out an argument (or pass `None`) to omit it.

## Removed

These 3.x methods have no v5 endpoint yet. Stay on `supermemory<4` if you depend on them:

- `client.settings.{reset, suggest_buckets}` and chunking settings
- `client.conversations.add`
- `client.documents.{list_processing, chunks, file_url}`
- container tag merge
- `client.memories.{add, update_memory}`
