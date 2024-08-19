import streamlit as st
from transformers import pipeline

# Load the text generation pipeline with a lightweight model
text_generator = pipeline("text-generation", model="distilgpt2")

# Streamlit app
def main():
    st.title("Hugging Face Text Generation")
    st.write("Enter some text and let the model generate a continuation.")

    # Text input
    input_text = st.text_input("Enter your text here:")

    if st.button("Generate"):
        if input_text:
            # Generate text
            generated_text = text_generator(input_text, max_length=50, num_return_sequences=1)
            st.write("Generated Text:")
            st.write(generated_text[0]['generated_text'])
        else:
            st.write("Please enter some text to generate.")

if __name__ == "__main__":
    main()

