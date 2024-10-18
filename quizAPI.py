import requests
import os

# Set up your QuizAPI key
# API_KEY = 'vMoiOl0xolo1hgRp2kFzC1XIUIoxCCwcl1AgtoO0'
API_KEY = os.getenv('QUIZ_API_KEY')


# Base URL for the QuizAPI
url = 'https://quizapi.io/api/v1/questions'

# Set headers with the API key
headers = {
    'X-Api-Key': API_KEY
}

# Parameters for the API call (you can modify them as needed)
params = {
    'limit': 10,  # Number of questions you want
    'category': 'Linux',  # Example category, you can change it
    'difficulty': 'Easy',  # Can be 'Easy', 'Medium', 'Hard'
}

# Make the request to the API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    questions = response.json()

    # Print out each question with its possible answers
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        print("Answers:")
        for key, value in question['answers'].items():
            if value:  # Some answers might be None
                print(f"  {key}: {value}")
        print("\n")
else:
    print(f"Failed to fetch questions. Status code: {response.status_code}")
