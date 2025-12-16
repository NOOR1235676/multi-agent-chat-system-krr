# src/coordinator.py

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent


class Coordinator:
    """
    Coordinator acts as the Manager agent.
    It decomposes tasks, coordinates agents,
    and synthesizes final responses.
    """

    def __init__(self):
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.memory_agent = MemoryAgent()
        self.conversation_history = []

    def handle_query(self, user_query: str) -> dict:
        """
        Handle user query by deciding which agents to invoke.
        """
        self.conversation_history.append(user_query)

        # 1. Check memory first (avoid redundant work)
        memory_hits = self.memory_agent.search_by_topic(user_query)
        if memory_hits:
            return {
                "source": "memory",
                "response": memory_hits
            }

        # 2. Decide task complexity
        if self._is_complex_query(user_query):
            return self._handle_complex_query(user_query)
        else:
            return self._handle_simple_query(user_query)

    def _handle_simple_query(self, query: str) -> dict:
        """
        Handle simple queries using ResearchAgent only.
        """
        research_output = self.research_agent.search(query)

        # Store in memory
        for item in research_output["results"]:
            self.memory_agent.store(
                topic=item["topic"],
                content=item["content"],
                source_agent="ResearchAgent",
                confidence=item["confidence"]
            )

        return {
            "source": "research",
            "response": research_output["results"]
        }

    def _handle_complex_query(self, query: str) -> dict:
        """
        Handle complex queries using Research + Analysis.
        """
        research_output = self.research_agent.search(query)
        analysis_output = self.analysis_agent.analyze(research_output)

        # Store analysis results in memory
        for item in analysis_output["analysis_results"]:
            self.memory_agent.store(
                topic=item["topic"],
                content=item["summary"],
                source_agent="AnalysisAgent",
                confidence=item["confidence"]
            )

        return {
            "source": "analysis",
            "response": analysis_output["analysis_results"]
        }

    def _is_complex_query(self, query: str) -> bool:
        """
        Simple rule-based complexity analysis.
        """
        complex_keywords = [
            "analyze", "compare", "efficiency",
            "trade-off", "summarize", "recommend"
        ]
        return any(word in query.lower() for word in complex_keywords)
