def parse_batch_response(raw_response: dict, total_recipes: int) -> dict:
    if not raw_response or "analysis" not in raw_response:
        return {
            "batch_id": "batch_error",
            "total_recipes": 0,
            "analysis": []
        }

    return {
        "batch_id": raw_response.get("batch_id", "batch_unknown"),
        "total_recipes": total_recipes,
        "analysis": raw_response["analysis"]
    }
