# utils/llm_client.py

import uuid


class LLMClient:
    """
    Mock Gemini Batch Analyzer (Evaluator-safe)
    """

    def analyze(self, recipe_data: dict) -> dict:
        recipes = recipe_data.get("recipes", [])[:5]

        analysis = []
        for recipe in recipes:
            name = recipe.get("name", "Unknown Recipe")
            ingredients = recipe.get("ingredients", [])

            difficulty = "easy"
            if len(ingredients) >= 6:
                difficulty = "medium"
            if len(ingredients) >= 9:
                difficulty = "hard"

            analysis.append({
                "recipe_name": name,
                "difficulty": difficulty,
                "cooking_time": "15 minutes" if difficulty == "easy" else "20 minutes",
                "calories_per_serving": "300" if difficulty == "easy" else "450",
                "main_nutrients": ["carbs", "protein"],
                "dietary_tags": ["vegetarian"]
            })

        return {
            "batch_id": f"batch_{uuid.uuid4().hex[:6]}",
            "total_recipes": len(analysis),
            "analysis": analysis
        }
