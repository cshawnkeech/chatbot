import streamlit as st
from transformers import pipeline

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

st.title("Open Source Language Model Deployment")

user_input = st.text_input("Enter a prompt:")

if st.button("Generate"):
    if user_input:

        generated_text = generator(
            user_input,
            max_length=50,
            num_return_sequences=1)[0]['generated_text']

        st.text(generated_text)
    else:
        st.warning("Please enter a prompt.")
