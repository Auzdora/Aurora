import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from plugin_base import BasePlugin
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from constants import *

class VectorDBSearch(BasePlugin):
    def __init__(self) -> None:
        super().__init__()
        self.embedding_model = OpenAIEmbeddings(
            openai_api_key=OPENAI_API_KEY,
            openai_api_base=OPENAI_API_BASE
        )

    def get_name(self) -> str:
        return "search_personal_vector_db"
    
    def get_description(self) -> str:
        return "Let GPT return a modified user query to search the local database \
    and answer local database information."

    def get_parameters(self):
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "User input query, GPT can modified for better similarity search",
                },
            },
            "required": ["query"]
        }
    
    def execute(self, **kwargs):
        print("searching your knowledge base ...")
        query = kwargs["query"]
        db = FAISS.load_local(
            configer.config["system"]["vector_db"]["store_path"], 
            embeddings=self.embedding_model
        )
        docs = db.similarity_search(query)
        answer = ""
        for doc in docs[:2]:
            answer += doc.page_content
        return answer
