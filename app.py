import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000/greet/"

# Streamlit frontend
st.title("Hello User App")

# Input field for user name
name = st.text_input("Enter your name")

# When button is pressed, send name to FastAPI backend
if st.button("Say Hello"):
    if name:
        response = requests.post(FASTAPI_URL, json={"name": name})
        if response.status_code == 200:
            result = response.json()
            st.success(result["message"])
        else:
            st.error("Error in communication with the FastAPI server.")
    else:
        st.warning("Please enter a name.")
