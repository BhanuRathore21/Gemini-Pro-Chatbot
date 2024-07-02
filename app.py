import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
    
st.set_page_config("Gimini-LLM-Chatbot")
st.title("Q&A LLM Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
 

input = st.text_input("Ask me the question here",key="Input")
button = st.button("Search")

if input or button:
    response = gemini_response(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("Chat History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")






