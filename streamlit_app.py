import streamlit as st
from transformers import pipeline

st.title("Lightweight Text Generation App")

try:
    # Initialize the text generation pipeline with a lightweight model
    text_generator = pipeline("text-generation", model="distilgpt2")
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

prompt = st.text_input("Enter a prompt for text generation:")

if prompt:
    with st.spinner('Generating text...'):
        try:
            # Generate text with the lightweight model
            generated_text = text_generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
            st.write(generated_text)
        except Exception as e:
            st.error(f"Text generation failed: {e}")
