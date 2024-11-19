import streamlit as st
import random #SEE IF THATS GOOD

st.title("Greek Mythology")
#test
# Unterüberschrift - Font ändern 
#mp: "####"" eingefügt für markdown
st.markdown ("#### Welcome to our guessing game about the greek mythology. Can you guess the mythological figures I am thinking about?", unsafe_allow_html=True)

st.write("You will have 4 attempts and 3 possible hints if you need them.")

st.write("You can choose between guessing a greek God (for example _Zeus_), a hero (_Herakles_), a creature (_Medusa_) or a titan (_Gaia_)")
#button to the play page
if st.button("Start Guessing"):
    st.switch_page("pages/1_play.py")


#Create a more visible button, its not working
# if st.button("Start Guessing"):
    # Navigate to the next page
    # st.switch_page = "pages/1_play.py"
    # st.experimental_rerun()  # This will rerun the app, allowing you to handle the new page logic

# opens a new tab, we dont want that
# st.link_button(
#     label="Start Guessing", 
#     url="play", 
#     type="primary"
# )