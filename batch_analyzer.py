# utils/batch_analyzer.py

from utils.llm_client import LLMClient


class RecipeBatchAnalyzer:
    def __init__(self):
        self.llm = LLMClient()

    def analyze_batch(self, recipes: list) -> dict:
        """
        Analyze up to 5 recipes in a single batch.
        """
        if not recipes:
            return {
                "batch_id": "batch_empty",
                "total_recipes": 0,
                "analysis": []
            }

        # Enforce max 5 recipes per batch
        payload = {
            "recipes": recipes[:5]
        }

        return self.llm.analyze(payload)
