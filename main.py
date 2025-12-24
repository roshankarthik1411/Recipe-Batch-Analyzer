# main.py

from utils.batch_analyzer import RecipeBatchAnalyzer


def main():
    analyzer = RecipeBatchAnalyzer()

    recipes = [
        {
            "name": "Spaghetti Carbonara",
            "ingredients": ["spaghetti", "eggs", "bacon", "parmesan", "pepper"],
            "instructions": "Cook pasta, fry bacon, mix with eggs and cheese"
        },
        {
            "name": "Caesar Salad",
            "ingredients": ["lettuce", "croutons", "parmesan", "dressing"],
            "instructions": "Toss all ingredients"
        }
    ]

    result = analyzer.analyze_batch(recipes)
    print(result)


if __name__ == "__main__":
    main()
