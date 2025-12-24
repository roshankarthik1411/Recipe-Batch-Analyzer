# 🍲 Recipe Batch Analyzer

## 📌 Overview
The Recipe Batch Analyzer is an AI-powered application designed to analyze multiple recipes in a single batch and extract structured insights such as ingredients, cooking time, difficulty level, calories, and dietary tags. It helps users efficiently understand and compare recipes without manually reviewing each one.

This project demonstrates how AI can be used to automate content analysis and transform unstructured recipe data into meaningful, organized information.

---

## 🎯 Problem Statement
Analyzing recipes manually is time-consuming, especially when dealing with multiple recipes at once. Users often need to:
- Compare cooking time and difficulty
- Identify dietary suitability (vegetarian, vegan, etc.)
- Estimate nutritional information
- Extract key ingredients quickly  

Doing this manually for large recipe sets is inefficient and error-prone.

---

## 💡 Solution
The Recipe Batch Analyzer allows users to input a batch of recipes and automatically generates structured analysis for each recipe. The system processes each recipe individually and returns key insights in a clean and readable format.

This makes it easier to compare recipes, plan meals, and make informed cooking decisions.

---

## ✨ Key Features
- Batch processing of multiple recipes  
- Automatic extraction of ingredients and cooking time  
- Difficulty level estimation  
- Calorie and nutrition insights  
- Dietary tags (vegetarian, vegan, etc.)  
- Clean and structured output  

---

## 🧠 How It Works
1. The user provides multiple recipes as input.
2. Each recipe is processed independently.
3. AI-driven logic analyzes the recipe text.
4. Structured insights are generated for every recipe.
5. Results are returned in an organized format for easy comparison.

This modular approach ensures scalability and maintainability.

---

## 🛠 Tech Stack
- Python  
- Prompt-based AI / LLM integration  
- Batch processing logic  
- Environment-based configuration for API keys  

---

## 📂 Project Structure
Recipe-Batch-Analyzer/
│
├── main.py # Application entry point
├── batch_analyzer.py # Core batch analysis logic
├── utils/ # Helper functions
├── data/ # Sample recipe inputs
├── requirements.txt # Project dependencies
├── .env.example # Environment variable template
├── README.md # Project documentation


---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of running Python scripts

### Installation
```bash
pip install -r requirements.txt
