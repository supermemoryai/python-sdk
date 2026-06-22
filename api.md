# Supermemory

Types:

```python
from supermemory.types import AddResponse, ProfileResponse
```

Methods:

- <code title="post /v3/documents">client.<a href="./src/supermemory/_client.py">add</a>(\*\*<a href="src/supermemory/types/client_add_params.py">params</a>) -> <a href="./src/supermemory/types/add_response.py">AddResponse</a></code>
- <code title="post /v4/profile">client.<a href="./src/supermemory/_client.py">profile</a>(\*\*<a href="src/supermemory/types/client_profile_params.py">params</a>) -> <a href="./src/supermemory/types/profile_response.py">ProfileResponse</a></code>

# Memories

Types:

```python
from supermemory.types import MemoryForgetResponse, MemoryUpdateMemoryResponse
```

Methods:

- <code title="delete /v4/memories">client.memories.<a href="./src/supermemory/resources/memories.py">forget</a>(\*\*<a href="src/supermemory/types/memory_forget_params.py">params</a>) -> <a href="./src/supermemory/types/memory_forget_response.py">MemoryForgetResponse</a></code>
- <code title="patch /v4/memories">client.memories.<a href="./src/supermemory/resources/memories.py">update_memory</a>(\*\*<a href="src/supermemory/types/memory_update_memory_params.py">params</a>) -> <a href="./src/supermemory/types/memory_update_memory_response.py">MemoryUpdateMemoryResponse</a></code>

# Documents

Types:

```python
from supermemory.types import (
    DocumentUpdateResponse,
    DocumentListResponse,
    DocumentAddResponse,
    DocumentBatchAddResponse,
    DocumentDeleteBulkResponse,
    DocumentGetResponse,
    DocumentListProcessingResponse,
    DocumentUploadFileResponse,
)
```

Methods:

- <code title="patch /v3/documents/{id}">client.documents.<a href="./src/supermemory/resources/documents.py">update</a>(id, \*\*<a href="src/supermemory/types/document_update_params.py">params</a>) -> <a href="./src/supermemory/types/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="post /v3/documents/list">client.documents.<a href="./src/supermemory/resources/documents.py">list</a>(\*\*<a href="src/supermemory/types/document_list_params.py">params</a>) -> <a href="./src/supermemory/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /v3/documents/{id}">client.documents.<a href="./src/supermemory/resources/documents.py">delete</a>(id) -> None</code>
- <code title="post /v3/documents">client.documents.<a href="./src/supermemory/resources/documents.py">add</a>(\*\*<a href="src/supermemory/types/document_add_params.py">params</a>) -> <a href="./src/supermemory/types/document_add_response.py">DocumentAddResponse</a></code>
- <code title="post /v3/documents/batch">client.documents.<a href="./src/supermemory/resources/documents.py">batch_add</a>(\*\*<a href="src/supermemory/types/document_batch_add_params.py">params</a>) -> <a href="./src/supermemory/types/document_batch_add_response.py">DocumentBatchAddResponse</a></code>
- <code title="delete /v3/documents/bulk">client.documents.<a href="./src/supermemory/resources/documents.py">delete_bulk</a>(\*\*<a href="src/supermemory/types/document_delete_bulk_params.py">params</a>) -> <a href="./src/supermemory/types/document_delete_bulk_response.py">DocumentDeleteBulkResponse</a></code>
- <code title="get /v3/documents/{id}">client.documents.<a href="./src/supermemory/resources/documents.py">get</a>(id) -> <a href="./src/supermemory/types/document_get_response.py">DocumentGetResponse</a></code>
- <code title="get /v3/documents/processing">client.documents.<a href="./src/supermemory/resources/documents.py">list_processing</a>() -> <a href="./src/supermemory/types/document_list_processing_response.py">DocumentListProcessingResponse</a></code>
- <code title="post /v3/documents/file">client.documents.<a href="./src/supermemory/resources/documents.py">upload_file</a>(\*\*<a href="src/supermemory/types/document_upload_file_params.py">params</a>) -> <a href="./src/supermemory/types/document_upload_file_response.py">DocumentUploadFileResponse</a></code>

# Search

Types:

```python
from supermemory.types import SearchDocumentsResponse, SearchExecuteResponse, SearchMemoriesResponse
```

Methods:

- <code title="post /v3/search">client.search.<a href="./src/supermemory/resources/search.py">documents</a>(\*\*<a href="src/supermemory/types/search_documents_params.py">params</a>) -> <a href="./src/supermemory/types/search_documents_response.py">SearchDocumentsResponse</a></code>
- <code title="post /v3/search">client.search.<a href="./src/supermemory/resources/search.py">execute</a>(\*\*<a href="src/supermemory/types/search_execute_params.py">params</a>) -> <a href="./src/supermemory/types/search_execute_response.py">SearchExecuteResponse</a></code>
- <code title="post /v4/search">client.search.<a href="./src/supermemory/resources/search.py">memories</a>(\*\*<a href="src/supermemory/types/search_memories_params.py">params</a>) -> <a href="./src/supermemory/types/search_memories_response.py">SearchMemoriesResponse</a></code>

# Settings

Types:

```python
from supermemory.types import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="patch /v3/settings">client.settings.<a href="./src/supermemory/resources/settings.py">update</a>(\*\*<a href="src/supermemory/types/setting_update_params.py">params</a>) -> <a href="./src/supermemory/types/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="get /v3/settings">client.settings.<a href="./src/supermemory/resources/settings.py">get</a>() -> <a href="./src/supermemory/types/setting_get_response.py">SettingGetResponse</a></code>
