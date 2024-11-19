import streamlit as st
import random #SEE IF THATS GOOD

st.title("Greek Mythology")
#test
# Unterüberschrift - Font ändern
st.markdown ("Welcome to our guessing game about the greek mythology. Can you guess the mythological figures I am thinking about?")

st.write("You will have 4 attempts and 3 possible hints if you need them.")

st.write("You can choose between guessing a greek God (for example _Zeus_), a hero (_Herakles_), a creature (_Medusa_) or a titan (_Gaia_)")


st.page_link("pages/1_play.py", label="Start Guessing")