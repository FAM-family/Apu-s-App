import streamlit as st
from transformers import pipeline

# Initialize the text generation pipeline with a lightweight model
text_generator = pipeline("text-generation", model="distilgpt2")

# Streamlit app
st.title("Lightweight Text Generation App")

prompt = st.text_input("Enter a prompt for text generation:")

if prompt:
    with st.spinner('Generating text...'):
        # Generate text with the lightweight model
        generated_text = text_generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
        st.write(generated_text)
