import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# mp: tab name and icon
st.set_page_config(page_title="Game Statistics", page_icon="📊")


#- The "Stats" page displays some stats about playing like the number of games played, the average number of guesses per game. 
#- The "Stats" page displays a bar chart showing he number of guesses for each game
st.write("# Your Statistics \U0001F4CA")  #unicode for bar chart


#games per session

if "input" not in st.session_state:
    st.session_state.input = 0
games = st.session_state.input
if "attempt" not in st.session_state:
    st.session_state.attempt = 0
#attempts per game
attempts = st.session_state.attempt

data = {
    "games": games,
    "attempts": attempts
}

if "attempts_per_game" not in st.session_state:
    st.write("You haven't played any game yet)")
else:
    attempts_data = st.session_state.attempts_per_game
    st.write(attempts_data)
    dfs = pd.DataFrame(attempts_data, columns=["Attempts"])
    st.write(dfs)
   
    # Plotting the attempts per game
    fig, ax = plt.subplots()
    ax.bar(dfs.index + 1, dfs["Attempts"], color='purple')
    ax.set_title("Attempts per Game")
    ax.set_xlabel("Game Number")
    ax.set_ylabel("Attempts")
    
    st.pyplot(fig)


