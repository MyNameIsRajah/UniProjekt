import streamlit as st
# import random #SEE IF THATS GOOD

st.title("Greek Mythology \u26A1 \U0001F3DB") #unicode for bolt icon and building

#mp: "####"" eingefügt für markdown
st.markdown ("#### Welcome to our guessing game about greek mythology. Can you guess the mythological figures I am thinking about?", unsafe_allow_html=True)

st.write("You will have 4 attempts and 3 possible hints if you need them.")

st.write("You can choose between guessing a greek God (for example _Zeus_), a hero (_Herakles_), a creature (_Medusa_) or a titan (_Gaia_)")
#button to the play page
if st.button("Start Guessing"):
    st.switch_page("pages/1_play.py")
