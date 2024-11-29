import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64

# tab name and icon
st.set_page_config(page_title="Game Statistics", page_icon="📊")
# cutsom css for the title font, colours etc.
custom_css = """
<head>
<link href="https://fonts.googleapis.com/css2?family=Caesar+Dressing&display=swap" rel="stylesheet">
<style>
.my-container {
 background: rgba(255, 255, 255, 0.0);
 padding: 20px;
 border-radius: 5px;
 color: rgba(7, 69, 110, 1);
 text-align: center;
 font-family: "sophia", sans serif;
h1 {font-family: "Caesar Dressing", system-ui;}
}
</style>
</head>
"""
# custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# set background image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("./Background_play.png")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('''
<div class = "my-container">
    <h1>⚡ Your statistics ⚡</h1>    
</div>
''', unsafe_allow_html=True)

if "input" not in st.session_state:
    st.session_state.input = 0

# number of games
if st.session_state.input > 0:
    number_games = st.session_state.input
    st.write(
        f"Number of games played: {number_games}") 
    # average guess attempts  per game
    if "attempts_per_game" in st.session_state:
        average_attempts = np.mean(st.session_state.attempts_per_game)
        st.write(
            f"Average number of guesses per game: {average_attempts:.2f}"
        )

# Dividing the list into rounds
    rounds = []
    index = 0
    for round_size in st.session_state.attempts_per_game:
        rounds.append(st.session_state.list_quality[index:index + round_size])
        index += round_size  # Move the index forward by the size of the current round

    
    attempts_data = st.session_state.attempts_per_game  # attempts per game
    attempts_df = pd.DataFrame(attempts_data, columns=["Attempts"])
    themes = st.session_state.theme_per_game
    data_cat = pd.DataFrame(themes, columns=["category"])
    # time tracker per game


    time_data = st.session_state.time_per_game
    time_df = pd.DataFrame(time_data, columns=['time(s)'])

    games_df = pd.DataFrame(
        {
            "games": [i for i in range(1, number_games + 1)]
        }
    )

    data = pd.concat([games_df, attempts_df, data_cat, time_df], axis=1)

    # show dataframe

    st.dataframe(data)

    st.subheader("Your games so far:")
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(
            data,
            x="games",
            y="Attempts",
            x_label="games played",
            y_label="attempts per game",
            color="category"
        )
        
    with col2:
        st.bar_chart(
            data,
            x="games",
            y="time(s)",
            x_label="games played",
            y_label="time(s) per game",
            color="category"
        )
        # quality of guesses
    st.subheader("Here you can see the quality of your guesses")
    #simple table guess quality per game
    guess_labels = {4: 'Excellent', 3: 'Good', 2: 'Ok', 1: 'Bad'}
    table_data = []
    for game_idx, guess_list in enumerate(rounds):
    # Count occurrences of each guess type (1, 2, 3, 4)
        counts = {label: guess_list.count(value) for value, label in guess_labels.items()}
        counts['Game'] = f'Game {game_idx + 1}'  # Add game number to the row
        table_data.append(counts)

    # Convert the data into a DataFrame
    df = pd.DataFrame(table_data)

    # Reorder columns to match the desired format
    df = df[['Game', 'Excellent', 'Good', 'Ok', 'Bad']]
    st.write("The table shows how many 'excellent', 'good', 'ok, 'bad'guesses you had per game.")
    dfs =st.dataframe(df, hide_index=True)



#graph of guess quality
    df = pd.DataFrame(
        {"game": [i for i in range(1, len(st.session_state.list_quality) + 1)],
         "Points for quality": st.session_state.list_quality})
    st.line_chart(df, x="game", y ="Points for quality")
    st.caption("4 points: You guessed correct. ")
    st.caption("3 points: Your guess was a mythological figure from the right category, just not the right one.")
    st.caption("2 points: Your guess was a mythological figure, just from the wrong category.")
    st.caption("1 points: Your guess was no mythological figure to our knowledge.")

    
# if no games were played yet display a button to the play page:
else:
    st.markdown('''
    <div class = "my-container">
        <h2>You need to play a game to see any statistics</h2> 
    </div>
    ''', unsafe_allow_html=True)

    _, col1, _ = st.columns(3)
    with col1:
        if st.button("Play a game", icon="🎲"):
            st.switch_page("pages/1_🎲_Play.py")

