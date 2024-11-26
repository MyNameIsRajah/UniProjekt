import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import columns

st.title("Test the Stats")

# Collecting the Datas
df_datacollection = pd.DataFrame ({
    'Games Played': [3,5,10,2],
    'Average Guesses': [2,3,1,4],
    'Categories': ['Heores','Titans','Creatures','Gods']
})

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns = ['Heroes', 'Titans', 'Creatures', 'Gods']
)

st.dataframe(df_datacollection)

st.subheader("Bar Chart")
st.bar_chart(df_datacollection)

st.subheader("Area Chart")
st.area_chart(df_datacollection)