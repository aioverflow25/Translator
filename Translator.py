import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq language model
model = ChatGroq(model="llama-3.1-8b-instant")

# Output parser for simple text response
parser = StrOutputParser()

# Supported languages
languages = [
    "English", "Chinese", "Hindi", "Spanish", "French", "German", "Arabic",
    "Portuguese", "Russian", "Japanese", "Korean", "Italian", "Turkish",
    "Vietnamese", "Urdu", "Bengali", "Malay", "Persian", "Thai", "Dutch",
    "Greek", "Polish", "Swedish", "Czech", "Hebrew", "Indonesian", "Romanian",
    "Ukrainian", "Hungarian", "Finnish", "Tamil", "Telugu", "Marathi", "Kannada"
]


# Streamlit app layout
st.set_page_config(page_title="🌐 Language Translator", layout="centered")
st.title("🌐 Multilingual Text Translator")

# Text input
input_text = st.text_area("✍️ Enter the text you want to translate:")

# Language selection dropdowns
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Translate from:", languages, index=1)  # Default: Chinese
with col2:
    target_lang = st.selectbox("Translate to:", languages, index=0)    # Default: English

# Trigger translation
if st.button("Translate") and input_text.strip():
    # Define the prompt
    template = PromptTemplate(
        template="Translate the following text from {source} to {target}:\n\n{text}",
        input_variables=["source", "target", "text"]
    )
    prompt = template.format(source=source_lang, target=target_lang, text=input_text)

    st.info("Translating... Please wait.")
    response = model.invoke(prompt)
    parsed_response = parser.parse(response.content)

    # Output result
    st.subheader("📝 Translated Text")
    st.write(parsed_response)





