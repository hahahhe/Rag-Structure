# 질문 -> embedding -> vector search -> 문서

from embedder import Embedder
from vector_store import VectorStore

class Retriever:
    def __init__(self, embedder: Embedder, vector_store: VectorStore):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 3) -> list[tuple[str, float]]:
        query_embedding = self.embedder.embed_query(query)

        results = self.vector_store.search(query_embedding, top_k=top_k)

        return results