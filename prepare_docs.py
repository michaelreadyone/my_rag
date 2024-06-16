from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv
from get_embedding import embeddings

load_dotenv()
DOC_PATH = os.getenv("DOC_PATH")


# load documents
def load_documents():
    loader = DirectoryLoader(DOC_PATH, glob="*.md")
    documents = loader.load()
    return documents


# prepare into chunks
def create_chunks(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    return text_splitter.split_documents(documents)


if __name__ == "__main__":
    documents = load_documents()
    chunks = create_chunks(documents)
