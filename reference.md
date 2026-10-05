# Reference
<details><summary><code>client.<a href="src/supermemory/client.py">add</a>(...) -> DocumentRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Turn text or a supported URL into searchable, evolving memory. Supply a new ID to create a document, or reuse an existing ID to append new information while preserving its history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.add(
    namespace="user_alex",
    content="Supermemory turns unstructured content into evolving memory.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — The content to process. This may be plaintext or a URL to supported rich content.
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` — Processing pipeline. "memory" builds durable learned context; "superrag" optimizes the document for retrieval without generating memories.
    
</dd>
</dl>

<dl>
<dd>

**dreaming:** `typing.Optional[DreamingMode]` — Processing mode. "dynamic" (default) groups related documents so memories form from coherent context. "instant" processes each document independently right away and bills one extra operation per document.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — An optional caller-defined document ID
    
</dd>
</dl>

<dl>
<dd>

**supporting_context:** `typing.Optional[str]` — Context used to guide memory extraction within this namespace. Max 1500 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, MetadataValue]]` — Arbitrary metadata attached to the document and derived data
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[typing.Dict[str, MetadataValue]]` — Metadata values that isolate related context within the namespace
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[str]` — When the source content is from, in ISO 8601 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/supermemory/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Recall the most relevant learned context and source passages from a namespace. Hybrid search combines memories with document chunks by default, with optional query rewriting, reranking, and supporting context attachments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.search(
    namespace="user_alex",
    limit=10,
    query="what are the API rate limits",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace to search. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — Natural-language question, topic, or phrase to retrieve relevant context for. Replaces the v4 `q` field.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[SearchMode]` — Search surface. "hybrid" combines learned memories with source chunks, "memories" returns learned context, and "chunks" returns source passages.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[FilterExpression]` — Type-safe metadata conditions applied before ranking results. Replaces the v4 `filters` field and unifies both legacy filter formats into one expression type.
    
</dd>
</dl>

<dl>
<dd>

**attach:** `typing.Optional[SearchRequestAttach]` — Optional context to include alongside each matching result
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `typing.Optional[float]` — Minimum relevance score from 0 to 1. Raise it for precision (fewer, accurate results) or lower it for broader recall (more results).
    
</dd>
</dl>

<dl>
<dd>

**rerank:** `typing.Optional[SearchRequestRerank]` — Post-retrieval ranking. "order" improves result ordering; "aggregate" also combines overlapping context into cleaner answers. This is helpful if you want to ensure the most relevant results are returned.
    
</dd>
</dl>

<dl>
<dd>

**rewrite_query:** `typing.Optional[bool]` — Expand and clarify the query before retrieval to improve recall for conversational or underspecified prompts. This increases the latency by about 400ms.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/supermemory/client.py">profile</a>(...) -> ProfileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a continuously maintained understanding of the subject represented by this namespace. Stable facts, evolving context, and selected custom buckets are returned together without requiring a search query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.profile(
    namespace="user_alex",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace to search. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[FilterExpression]` — Type-safe metadata conditions that limit which memories contribute to the profile
    
</dd>
</dl>

<dl>
<dd>

**buckets:** `typing.Optional[typing.List[str]]` — Custom buckets to return. Omit to return every effective bucket.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/supermemory/client.py">list</a>(...) -> ListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Browse documents, source chunks, or learned memories through one predictable paginated contract. Choose the collection in the path; the other collection arrays remain empty for a stable response shape.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.list(
    namespace="user_alex",
    type="documents",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace containing the resources to list. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope resources.
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` — Resource collection to list: source documents, extracted chunks, or learned memories
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[ListRequestPage]` — One-based page number
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[ListRequestLimit]` — Maximum resources to return per page
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListSort]` — Field used to order results. Position is available only when listing chunks.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SortOrder]` — Ascending or descending sort direction
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[FilterExpression]` — Type-safe metadata conditions applied before pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">delete</a>(...) -> DeleteDocumentsResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently remove documents and their derived knowledge by document ID or caller-defined ID. Each requested ID is handled independently so successful deletions are preserved when another ID fails.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.delete(
    namespace="user_alex",
    ids=[
        "my-doc-123"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.List[str]` — Document identifiers to permanently delete from this namespace
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">batch_add</a>(...) -> BatchAddResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Build a knowledge base efficiently by ingesting up to 600 text or URL documents at once. Existing caller-defined IDs append new information using the same semantics as single-document ingestion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.batch_add(
    namespace="user_alex",
    documents=[
        {
            "content": "Supermemory turns unstructured content into evolving memory."
        }
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.List[DocumentInput]` — Documents to ingest or append in one request
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` — Processing pipeline. "memory" builds durable learned context; "superrag" optimizes the document for retrieval without generating memories.
    
</dd>
</dl>

<dl>
<dd>

**dreaming:** `typing.Optional[DreamingMode]` — Processing mode. "dynamic" (default) groups related documents so memories form from coherent context. "instant" processes each document independently right away and bills one extra operation per document.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">get</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a document's canonical content, metadata, and processing state by document ID or caller-defined ID. Optionally attach its source chunks, derived memories, or both in the same response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.get(
    namespace="user_alex",
    id="my-doc-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The public document ID
    
</dd>
</dl>

<dl>
<dd>

**attach:** `typing.Optional[typing.Union[DocumentAttachment, typing.Sequence[DocumentAttachment]]]` — Child resources to include. Repeat the parameter to attach chunks, memories, or both.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">update</a>(...) -> DocumentRef</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh an existing document without changing its stable ID. Supplied content replaces the canonical content and is reprocessed; omitted fields remain unchanged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.update(
    namespace="user_alex",
    id="my-doc-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The public document ID
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` — Processing pipeline. "memory" builds durable learned context; "superrag" optimizes the document for retrieval without generating memories.
    
</dd>
</dl>

<dl>
<dd>

**dreaming:** `typing.Optional[DreamingMode]` — Processing mode. "dynamic" (default) groups related documents so memories form from coherent context. "instant" processes each document independently right away and bills one extra operation per document.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — The content to process. This may be plaintext or a URL to supported rich content.
    
</dd>
</dl>

<dl>
<dd>

**supporting_context:** `typing.Optional[str]` — Context used to guide memory extraction within this namespace. Max 1500 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, MetadataValue]]` — Arbitrary metadata attached to the document and derived data
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[typing.Dict[str, MetadataValue]]` — Metadata values that isolate related context within the namespace
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[str]` — When the source content is from, in ISO 8601 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">upload_file</a>(...) -> FileUploadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transform an uploaded file into searchable knowledge and learned memory. The response returns as soon as ingestion is safely queued while extraction and memory formation continue asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.upload_file(
    namespace="user_alex",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — File contents to upload
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` — Processing pipeline. "memory" builds durable learned context; "superrag" optimizes the document for retrieval without generating memories.
    
</dd>
</dl>

<dl>
<dd>

**dreaming:** `typing.Optional[DreamingMode]` — Processing mode. "dynamic" (default) groups related documents so memories form from coherent context. "instant" processes each document independently right away and bills one extra operation per document.
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `typing.Optional[FileType]` — Explicit source type used when automatic inference is insufficient
    
</dd>
</dl>

<dl>
<dd>

**mime_type:** `typing.Optional[str]` — Explicit MIME type used when upload metadata is insufficient
    
</dd>
</dl>

<dl>
<dd>

**supporting_context:** `typing.Optional[str]` — Context used to guide memory extraction within this namespace. Max 1500 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[str]` — JSON-encoded metadata to attach to the document and its derived memories
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[str]` — JSON-encoded metadata used to keep related context isolated during processing and recall
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[str]` — When the source content is from, in ISO 8601 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">replace_with_file</a>(...) -> FileUploadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace an existing document with a new file while keeping its stable document ID. Content and caller metadata are overwritten, then the document is reprocessed asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.replace_with_file(
    namespace="user_alex",
    id="my-doc-123",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The public document ID
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — File contents to upload
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` — Processing pipeline. "memory" builds durable learned context; "superrag" optimizes the document for retrieval without generating memories.
    
</dd>
</dl>

<dl>
<dd>

**dreaming:** `typing.Optional[DreamingMode]` — Processing mode. "dynamic" (default) groups related documents so memories form from coherent context. "instant" processes each document independently right away and bills one extra operation per document.
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `typing.Optional[FileType]` — Explicit source type used when automatic inference is insufficient
    
</dd>
</dl>

<dl>
<dd>

**mime_type:** `typing.Optional[str]` — Explicit MIME type used when upload metadata is insufficient
    
</dd>
</dl>

<dl>
<dd>

**supporting_context:** `typing.Optional[str]` — Context used to guide memory extraction within this namespace. Max 1500 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[str]` — JSON-encoded metadata to attach to the document and its derived memories
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[str]` — JSON-encoded metadata used to keep related context isolated during processing and recall
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[str]` — When the source content is from, in ISO 8601 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/supermemory/documents/client.py">update_file</a>(...) -> FileUploadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh only the file-backed fields you provide. Supplying a file replaces the canonical content; omitted metadata and processing context remain unchanged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.documents.update_file(
    namespace="user_alex",
    id="my-doc-123",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The public document ID
    
</dd>
</dl>

<dl>
<dd>

**task_type:** `typing.Optional[TaskType]` — Processing pipeline. "memory" builds durable learned context; "superrag" optimizes the document for retrieval without generating memories.
    
</dd>
</dl>

<dl>
<dd>

**dreaming:** `typing.Optional[DreamingMode]` — Processing mode. "dynamic" (default) groups related documents so memories form from coherent context. "instant" processes each document independently right away and bills one extra operation per document.
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `typing.Optional[FileType]` — Explicit source type used when automatic inference is insufficient
    
</dd>
</dl>

<dl>
<dd>

**mime_type:** `typing.Optional[str]` — Explicit MIME type used when upload metadata is insufficient
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — File contents to upload
    
</dd>
</dl>

<dl>
<dd>

**supporting_context:** `typing.Optional[str]` — Context used to guide memory extraction within this namespace. Max 1500 characters.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[str]` — JSON-encoded metadata to attach to the document and its derived memories
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[str]` — JSON-encoded metadata used to keep related context isolated during processing and recall
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[str]` — When the source content is from, in ISO 8601 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Profiles
<details><summary><code>client.profiles.<a href="src/supermemory/profiles/client.py">get_buckets</a>(...) -> ProfileBuckets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the profile taxonomy active in this namespace. The response combines organization-wide buckets with namespace-owned additions as a concise name-to-description map.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.profiles.get_buckets(
    namespace="user_alex",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace to search. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/supermemory/profiles/client.py">set_buckets</a>(...) -> ProfileBuckets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Teach Supermemory new ways to organize this namespace's profile, or refine how existing namespace-owned buckets are classified. Omitted buckets remain unchanged and organization-wide buckets stay protected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.profiles.set_buckets(
    namespace="user_alex",
    buckets={
        "interests": "Topics the subject actively follows"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace to search. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**buckets:** `typing.Dict[str, str]` — Namespace-owned bucket names mapped to descriptions that guide memory classification. Existing names are updated; new names are added.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/supermemory/profiles/client.py">delete_buckets</a>(...) -> ProfileBuckets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove profile categories created specifically for this namespace. Unknown names are safely ignored, while organization-wide buckets remain protected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.profiles.delete_buckets(
    namespace="user_alex",
    buckets=[
        "interests"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — The isolated namespace to search. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**buckets:** `typing.List[str]` — Namespace-owned bucket names to delete. Organization-level buckets are protected and cannot be removed here.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Memories
<details><summary><code>client.memories.<a href="src/supermemory/memories/client.py">forget</a>(...) -> ForgetResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove exact memories from normal recall while preserving their audit history. Each ID is handled independently and any missing or ineligible memory is reported without rolling back successful changes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.memories.forget(
    namespace="user_alex",
    ids=[
        "mem_abc123"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace containing the memories to forget. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.List[str]` — Memory identifiers to remove from normal recall
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memories.<a href="src/supermemory/memories/client.py">forget_matching</a>(...) -> ForgetResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describe what should be forgotten in natural language, then preview or apply the matching set. Use dry-run results with the exact-ID endpoint when you need a reviewable, drift-free workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.memories.forget_matching(
    namespace="user_alex",
    query="everything about the old pricing plans",
    dry_run=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace containing the memories to forget. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope memories.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — Natural-language description of the memories that should be forgotten
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `bool` — When true, preview matching memories without changing their recall state
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connectors
<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">list_all</a>(...) -> ConnectorList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List connectors across every namespace this key can read. Use it for admin views that span users or projects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.list_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `typing.Optional[ConnectorProvider]` — Only return connectors for this provider
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum connectors to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">list</a>(...) -> ConnectorList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the connectors that sync into this namespace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.list(
    namespace="user_alex",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[ConnectorProvider]` — Only return connectors for this provider
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum connectors to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">create</a>(...) -> ConnectorSetupResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect an external source to this namespace. OAuth providers return an authUrl to send the user to; providers that authenticate with config start syncing right away.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.create(
    namespace="user_alex",
    request={
        "provider": "notion"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ConnectorSetup` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">get</a>(...) -> Connector</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one connector. Add attach=syncs to include its recent sync runs and the items that failed. attach=picker needs an admin with write access, since the link changes what syncs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.get(
    namespace="user_alex",
    id="PTzGiUYei7pgzg5buzZHgA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Connector identifier returned when the connector was created
    
</dd>
</dl>

<dl>
<dd>

**attach:** `typing.Optional[str]` — Comma-separated extras. syncs: the 10 most recent sync runs with their failed items. picker: a one-time hosted picker URL.
    
</dd>
</dl>

<dl>
<dd>

**return_url:** `typing.Optional[str]` — Where the hosted picker sends the user when they finish
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">delete</a>(...) -> ConnectorDeleted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect a connector and stop its webhooks. Its imported documents are deleted too unless deleteDocuments is false.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.delete(
    namespace="user_alex",
    id="PTzGiUYei7pgzg5buzZHgA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Connector identifier returned when the connector was created
    
</dd>
</dl>

<dl>
<dd>

**delete_documents:** `typing.Optional[DeleteConnectorsRequestDeleteDocuments]` — Also delete documents this connector imported. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">update</a>(...) -> Connector</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change what a connector syncs. A new selection replaces the old one and starts a sync.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.update(
    namespace="user_alex",
    id="PTzGiUYei7pgzg5buzZHgA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Connector identifier returned when the connector was created
    
</dd>
</dl>

<dl>
<dd>

**selection:** `typing.Optional[ConnectorSelection]` — What to sync, as ids grouped by kind. GitHub takes repos, Gmail takes labels, Google Drive takes files and folders. Replaces the current selection.
    
</dd>
</dl>

<dl>
<dd>

**document_limit:** `typing.Optional[int]` — Maximum documents this connector imports
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors.<a href="src/supermemory/connectors/client.py">sync</a>(...) -> ConnectorSyncStarted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a sync now. Returns 409 while a sync for this connector is already running.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.connectors.sync(
    namespace="user_alex",
    id="PTzGiUYei7pgzg5buzZHgA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Connector identifier returned when the connector was created
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Namespaces
<details><summary><code>client.namespaces.<a href="src/supermemory/namespaces/client.py">list</a>() -> typing.List[Namespace]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discover every namespace available to the caller, including its purpose, document volume, memory count, and lifecycle timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.namespaces.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.namespaces.<a href="src/supermemory/namespaces/client.py">get</a>(...) -> NamespaceDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the supporting context that helps Supermemory understand content and form better memories inside this namespace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.namespaces.get(
    namespace="user_alex",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.namespaces.<a href="src/supermemory/namespaces/client.py">delete</a>(...) -> NamespaceDeleted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retire a namespace by permanently deleting its content, or preserve that knowledge by moving everything into another namespace first. Moves are queued and complete asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.namespaces.delete(
    namespace="user_alex",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**move_to:** `typing.Optional[str]` — Destination namespace that should receive this namespace's content before deletion. Omit to permanently delete the content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.namespaces.<a href="src/supermemory/namespaces/client.py">update</a>(...) -> NamespaceDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Shape how Supermemory understands an existing namespace by updating the background context used during ingestion and memory formation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.namespaces.update(
    namespace="user_alex",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**namespace:** `str` — Namespace identifier. This can be an ID for your user, a project ID, or any other identifier you wish to use to scope documents and memories.
    
</dd>
</dl>

<dl>
<dd>

**supporting_context:** `typing.Optional[str]` — Background that guides how Supermemory interprets documents and forms memories. Max 1500 characters. Set null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization
<details><summary><code>client.organization.<a href="src/supermemory/organization/client.py">get</a>() -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the shared background that guides memory formation across the organization, together with the number of active namespaces.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.organization.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/supermemory/organization/client.py">update</a>(...) -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Give Supermemory organization-wide background that improves how content is interpreted across every namespace. Send null to remove the existing context.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from supermemory import Supermemory
from supermemory.environment import SupermemoryEnvironment

client = Supermemory(
    api_key="<token>",
    environment=SupermemoryEnvironment.DEFAULT,
)

client.organization.update(
    organizational_context=None,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organizational_context:** `typing.Optional[str]` — Shared background that guides memory formation across every namespace. Set null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

