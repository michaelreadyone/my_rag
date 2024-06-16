from create_db import create_chroma_db
from prepare_docs import create_chunks, load_documents

# prepare docs
docs = load_documents()

# get chunks
chunks = create_chunks(docs)

# create db
create_chroma_db(chunks)
