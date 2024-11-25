import streamlit as st
import base64
# import random #SEE IF THATS GOOD

#mp: tab name and icon 
st.set_page_config(page_title="Greek Mythology", page_icon="⚡")

#black rgb 0,0,0 
#white 255,255,255, orange : rgba(248, 193, 29, 0.5)
# Define your custom CSS
custom_css = """
<style>
.my-container {
 background: rgba(255, 255, 255, 0.5);
 padding: 10px;
 border-radius: 5px;
 color: rgba(7, 69, 110, 1);
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Use the custom class in a container
st.markdown('''
<div class = "my-container">
    <h1>Greek Mythology 🏛️⚡</h1>
    <h2>Welcome to our guessing game about greek mythology. Can you guess the mythological figures I am thinking about?</h2>
    <p>You will have 4 attempts and 3 possible hints if you need them.</p>
    <p>You can choose between guessing a greek God (for example Zeus), a hero (Herakles), a creature (Medusa) or a titan (Gaia)</p>
</div>
''', unsafe_allow_html=True)


   
# st.title("Greek Mythology \u26A1 \U0001F3DB") #unicode for bolt icon and building
#mp: "####"" eingefügt für markdown
#st.markdown ("#### Welcome to our guessing game about greek mythology. Can you guess the mythological figures I am thinking about?", unsafe_allow_html=True)
 #st.write("You will have 4 attempts and 3 possible hints if you need them.")
#st.write("You can choose between guessing a greek God (for example _Zeus_), a hero (_Herakles_), a creature (_Medusa_) or a titan (_Gaia_)")


#button to the play page
if st.button("Start Guessing 🪽") :
    st.switch_page("pages/1_🎲_Play.py")

#code to use background image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("./background.png")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: contain;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)





