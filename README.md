# Langchain RAG Tutorial

### Install dependencies

```python
pip install -r requirements.txt
```

### Create the Chroma DB.

```python
python main_setup_db.py
```

### Query the Chroma DB.

Modify the query_text in query_data.py

```python
python main_setup_db.py
```

### Current status:

- Support markdown format
- will need to re-write the db for each loading
- Utiize chromedb
- use OpenAI for embeddings and Chat

### Future add on:

- add support for other formats
- logics to update the database, instead of rewrite 
- test other databases for better scaling
- test other llm for better accuracy
- test Ollama for local dev which can be used for local data
