import streamlit as st
import requests

# FastAPI backend URL
backend_url = "http://127.0.0.1:8000/questions"

# Streamlit interface
st.title("Quiz Generator")

# User inputs for category and difficulty
category = st.selectbox("Select a Category", ["Linux", "DevOps", "Networking", "Programming"])
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

# Fetch questions on button click
if st.button("Generate Quiz"):
    params = {
        'category': category,
        'difficulty': difficulty
    }
    
    try:
        # Make request to FastAPI backend
        response = requests.get(backend_url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            questions = response.json()

            # Debug print to see the exact response format
            st.write("Raw Response:", questions)

            # Display each question with its possible answers
            if isinstance(questions, list):  # Ensure the response is a list
                for i, question in enumerate(questions):
                    # Check if 'question' and 'answers' keys exist in each item
                    if 'question' in question and 'answers' in question:
                        st.write(f"**Question {i+1}:** {question['question']}")
                        st.write("**Answers:**")
                        
                        # Safely loop through answers
                        for key, value in question['answers'].items():
                            if value:
                                st.write(f"{key}: {value}")
                    else:
                        st.write(f"Question {i+1} is missing data.")
                    st.write("\n")
            else:
                st.write("Error: Unexpected response format.")
        else:
            st.write(f"Error fetching questions. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.write(f"Error connecting to backend: {e}")
