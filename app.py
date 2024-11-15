import streamlit as st
import base64

st.title("Welcome to the _fruit Guessing Game_ :lemon:")

#encodes picture to binary data and encodes it in base 64 text format
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("./fruits.jpeg")

#altering background image 
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;

}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

#adds a centered button to the play page
col1, col2, col3 = st.columns(3)
with col2:
    st.page_link("pages/1_play.py", label="Start Guessing", icon="🍓")