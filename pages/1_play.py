import streamlit as st

st.title("Play game")

users_guess = st.text_input("your guess", value="", max_chars=20)