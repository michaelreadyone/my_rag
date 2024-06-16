from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


embedding_func_dict = {
    "openai": OpenAIEmbeddings(),
    "llama3": OllamaEmbeddings(),
}


def get_embeddings(embedding_type="openai"):
    return embedding_func_dict[embedding_type]


embeddings = get_embeddings("openai")
