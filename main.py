from fastapi import FastAPI, Query
import requests
import os

app = FastAPI()

# Get API key from environment variable
API_KEY = os.getenv('QUIZ_API_KEY')

# Base URL for the QuizAPI
quiz_api_url = 'https://quizapi.io/api/v1/questions'

@app.get("/questions")
def get_questions(category: str = Query(None), difficulty: str = Query(None)):
    # Check if the API key is available
    if not API_KEY:
        return {"error": "API key not found in environment variables."}

    # Set headers with the API key
    headers = {
        'X-Api-Key': API_KEY
    }
    
    # Parameters for the API call
    params = {
        'limit': 10,  # Fixed number of questions
        'category': category,  # Category from the query parameter
        'difficulty': difficulty  # Difficulty from the query parameter
    }

    try:
        # Make the request to the QuizAPI
        response = requests.get(quiz_api_url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Ensure response is a list and contains the expected fields
            if isinstance(data, list):
                validated_questions = []
                for item in data:
                    if 'question' in item and 'answers' in item:
                        validated_questions.append(item)
                
                return validated_questions
            else:
                return {"error": "Unexpected data format from QuizAPI."}
        else:
            return {"error": f"Failed to fetch questions. Status code: {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Error connecting to QuizAPI: {str(e)}"}
