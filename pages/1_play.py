import streamlit as st

st.title("Play game")

#Display a single-line text input widget
users_guess = st.text_input("your guess", value="", max_chars=20)