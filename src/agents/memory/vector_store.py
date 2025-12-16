# src/memory/vector_store.py

import math


class SimpleVectorStore:
    """
    Lightweight in-memory vector store using cosine similarity.
    Acts as an equivalent alternative to FAISS/Chroma.
    """

    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, vector: list, meta: dict):
        self.vectors.append(vector)
        self.metadata.append(meta)

    def search(self, query_vector: list, top_k: int = 3) -> list:
        scores = []

        for idx, stored_vector in enumerate(self.vectors):
            similarity = self._cosine_similarity(query_vector, stored_vector)
            scores.append((similarity, self.metadata[idx]))

        scores.sort(reverse=True, key=lambda x: x[0])
        return scores[:top_k]

    def _cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot / (mag1 * mag2)
