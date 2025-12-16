# src/agents/memory_agent.py

from datetime import datetime
from agents.memory.vector_store import SimpleVectorStore



class MemoryAgent:
    """
    MemoryAgent stores and retrieves structured knowledge.
    Supports both keyword-based and vector-based retrieval.
    """

    def __init__(self):
        self.memory_store = []
        self.vector_store = SimpleVectorStore()

    def _embed(self, text: str) -> list:
        """
        Simple deterministic embedding function.
        (Lightweight alternative to external embedding models)
        """
        # Convert characters to numeric values (stable & reproducible)
        return [ord(c) % 50 / 50 for c in text[:50]]

    def store(self, topic: str, content: str, source_agent: str, confidence: float) -> None:
        record = {
            "topic": topic,
            "content": content,
            "source_agent": source_agent,
            "timestamp": datetime.utcnow().isoformat(),
            "confidence": confidence
        }

        # Store structured record
        self.memory_store.append(record)

        # Store vector representation
        vector = self._embed(content)
        self.vector_store.add(vector, record)

    def search_by_topic(self, query: str, top_k: int = 3) -> list:
        """
        Hybrid retrieval:
        1. Keyword-based search
        2. Vector similarity search
        """
        query_lower = query.lower()

        # Keyword search
        keyword_hits = [
            record for record in self.memory_store
            if query_lower in record["topic"].lower()
        ]

        # Vector similarity search
        query_vector = self._embed(query)
        vector_hits = self.vector_store.search(query_vector, top_k=top_k)

        # Extract metadata from vector results
        vector_results = [meta for _, meta in vector_hits]

        # Merge results (avoid duplicates)
        combined = {id(r): r for r in keyword_hits + vector_results}

        return list(combined.values())
