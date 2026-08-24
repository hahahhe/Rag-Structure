# chunk -> vector
# 정규화 하기 L2

from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    # 문서
    def embed_documents(self, texts: list[str]) -> np.ndarray:
        embeddings = self.model.encode(texts, normalize_embeddings=True)

        return embeddings

    # 질의
    def embed_query(self, query: str) -> np.ndarray:
        embedding = self.model.encode(query, normalize_embeddings=True)

        return embedding