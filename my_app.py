# Import necessary libraries
import streamlit as st

# Define chatbot logic
def get_medical_response(user_input):
    # A simple mock response generator for now; you can add more complex responses or integrate a medical API
    if "headache" in user_input.lower():
        return "For a headache, staying hydrated and resting in a quiet place may help. You could consider taking a mild pain reliever. If it persists, consult a healthcare professional."
    elif "fever" in user_input.lower():
        return "For a fever, staying hydrated and resting is essential. Take a fever reducer if necessary, and see a doctor if it lasts more than two days."
    else:
        return "I'm here to help with basic health advice. Please describe your symptoms."

# Streamlit UI
st.set_page_config(page_title="Healthcare Assistant", page_icon="🩺", layout="centered")

# Header section
st.title("Healthcare Chatbot")
st.markdown("Hello! I'm here to assist you with basic health advice. Please describe your symptoms, and I'll do my best to help.")

# Input and chatbot interaction
user_input = st.text_input("You: ", placeholder="Describe your symptoms...")
if st.button("Send") and user_input:
    response = get_medical_response(user_input)
    st.write("Healthcare Assistant:", response)

# Styling the UI for healthcare theme
st.markdown("""
    <style>
    body { font-family: Arial, sans-serif; background-color: #f0f8ff; }
    .stTextInput { border: 1px solid #4CAF50; padding: 10px; width: 100%; }
    .stButton { background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)
