import argparse
import os
from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from get_embedding import embeddings

load_dotenv()
CHROMA_PATH = os.getenv("CHROMA_PATH")

# Prepare the DB
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def cli():
    # create CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text


def similarity_search(query_text, k=3):
    return db.similarity_search_with_relevance_scores(query_text, k=k)


def prepare_prompt(question, similarity_search_results):
    context = "\n\n---\n\n".join(
        [doc.page_content for doc, _score in similarity_search_results]
    )
    return PROMPT_TEMPLATE.format(context=context, question=question)


def ask_llm(question, model=ChatOpenAI()):
    similarity_search_results = similarity_search(question)
    prompt = prepare_prompt(question, similarity_search_results)
    response_txt = model.invoke(prompt)

    sources = [
        doc.metadata.get("source", None) for doc, _score in similarity_search_results
    ]
    ans = f"Response: {response_txt}\n Sources: {sources}"
    print(ans)
    return ans


if __name__ == "__main__":
    query_text = "hello alice, how old are you?"
    ans = ask_llm(query_text)
