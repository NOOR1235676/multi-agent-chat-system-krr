# src/agents/analysis_agent.py

from datetime import datetime


class AnalysisAgent:
    """
    AnalysisAgent performs reasoning, comparison,
    and simple analysis on research results.
    """

    def analyze(self, research_output: dict) -> dict:
        """
        Analyze research agent output and produce insights.
        """
        analyzed_results = []

        results = research_output.get("results", [])

        for item in results:
            summary = self._summarize(item["content"])

            analyzed_results.append({
                "topic": item["topic"],
                "summary": summary,
                "analysis": "Identified as a key concept in the topic.",
                "timestamp": datetime.utcnow().isoformat(),
                "confidence": 0.75
            })

        return {
            "agent": "AnalysisAgent",
            "input_query": research_output.get("query"),
            "analysis_results": analyzed_results
        }

    def _summarize(self, text: str) -> str:
        """
        Simple summarization logic (rule-based).
        """
        if len(text) <= 80:
            return text
        return text[:77] + "..."
