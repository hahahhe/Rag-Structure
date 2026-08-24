# numpy로 vector store 구현

import numpy as np

class VectorStore:
    def __init__(self):
        self.documents: list[str] = []
        self.embeddings: np.ndarray | None = None

    def add(self, documents: list[str], embeddings: np.ndarray) -> None:
        self.documents.extend(documents)

        if self.embeddings is None:
            self.embeddings = embeddings
        else:
            self.embeddings = np.vstack([self.embeddings, embeddings])

    def search(self, query_embedding: np.ndarray, top_k: int = 3) -> list[tuple[str, float]]:
        if self.embeddings is None:
            return []

        similarities = np.dot(self.embeddings, query_embedding)

        top = np.argsort(similarities)[::-1][:top_k]

        result = []

        for index in top:
            document = self.documents[index]
            score = similarities[index]

            result.append((document, score))

        return result

