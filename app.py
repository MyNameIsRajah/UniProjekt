import streamlit as st
import base64

st.title("Welcome to the _fruit Guessing Game_ :lemon:")

st.write("This is my first web app.")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("./fruits.jpeg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;

}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)