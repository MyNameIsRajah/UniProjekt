import streamlit as st
import base64

# tab name and icon
st.set_page_config(page_title="Greek Mythology", page_icon="⚡")

# black rgb 0,0,0
# white 255,255,255, orange : rgba(248, 193, 29, 0.5)
# Define custom CSS

custom_css = """
<head>
<link href="https://fonts.googleapis.com/css2?family=Caesar+Dressing&display=swap" rel="stylesheet">
<style>
.my-container {
 background: rgba(255, 255, 255, 0.0);
 padding: 100px;
 border-radius: 5px;
 color: rgba(7, 69, 110, 1);
 text-align: center;
 font-family: "sophia", sans serif;
h1 {font-family: "Caesar Dressing", system-ui;}
}
</style>
</head>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Use the custom class in a container
st.markdown('''
<div class = "my-container">
    <h1>Greek Mythology 🏛️⚡</h1>
    <h2>Welcome to our guessing game about Greek Mythology. Can you guess the mythological figures I am thinking about?</h2>
    <p>You will have 4 attempts and 3 possible hints if you need them.</p>
    <p>Choose between guessing a greek god (for example Zeus), a hero (e.g. Herakles), a creature (e.g. Medusa) or a titan (e.g. Gaia)</p>
</div>
''', unsafe_allow_html=True)

# centered button to start guessing and go to play plage
_, col1, _ = st.columns(3)
with col1:
    if st.button("Start Guessing"):
        st.switch_page("pages/1_🎲_Play.py")


# code to use background image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("./hintergrund.png")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
