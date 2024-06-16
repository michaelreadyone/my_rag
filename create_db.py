from langchain_community.vectorstores import Chroma
from langchain.schema import Document
import os
import shutil
from dotenv import load_dotenv
from get_embedding import embeddings

load_dotenv()
CHROMA_PATH = os.getenv("CHROMA_PATH")

"""
Input: chunks of data
Do: save chunks of data into a vector database
Output:
Note: Overwrite DB every time, don't support add functionality.
"""


def create_chroma_db(chunks: list[Document]):
    # clean out the existing DB
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new database
    db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)


if __name__ == "__main__":
    pass
