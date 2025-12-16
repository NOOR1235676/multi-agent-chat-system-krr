# src/agents/research_agent.py

from datetime import datetime


class ResearchAgent:
    """
    ResearchAgent simulates information retrieval
    using a pre-loaded knowledge base (mock web search).
    """

    def __init__(self):
        # Mock knowledge base (can be expanded)
        self.knowledge_base = {
            "neural networks": [
                "Neural networks are computational models inspired by the human brain.",
                "Common types include CNNs, RNNs, and Transformers."
            ],
            "transformer architectures": [
                "Transformers use self-attention mechanisms instead of recurrence.",
                "They are highly parallelizable but computationally expensive."
            ],
            "reinforcement learning": [
                "Reinforcement learning is based on agents learning via rewards.",
                "Common algorithms include Q-learning and Policy Gradients."
            ]
        }

    def search(self, query: str) -> dict:
        """
        Perform a mock search over the knowledge base.
        """
        query_lower = query.lower()
        results = []

        for topic, facts in self.knowledge_base.items():
            if topic in query_lower:
                for fact in facts:
                    results.append({
                        "topic": topic,
                        "content": fact,
                        "source": "mock_knowledge_base",
                        "timestamp": datetime.utcnow().isoformat(),
                        "confidence": 0.8
                    })

        return {
            "agent": "ResearchAgent",
            "query": query,
            "results": results
        }
