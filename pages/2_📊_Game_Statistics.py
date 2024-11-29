import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64

##STATISTIK ERST AKTUALISIERT WENN AUF "NEW GAME" GEKLICKT WIRD

# mp: tab name and icon
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
# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# set background image
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

st.markdown('''
<div class = "my-container">
    <h1>⚡ Your statistics ⚡</h1>    
</div>
''', unsafe_allow_html=True)

# Farbpalette für die Kategorien
# color_palette = {
#   "Gods": "blue",
#  "Creatures": "orange",
# "Titans": "green",
# "Heroes": "purple",
# }
if "input" not in st.session_state:
    st.session_state.input = 0

# Anzahl der Spiele
if st.session_state.input > 0:
    number_games = st.session_state.input
    st.write(
        f"Number of games played: {number_games}")  # "f" für f-string -> ermöglicht, Variablen direkt in Strings einzubetten.
    # Durchschnittliche Rateversuche pro Spiel
    if "attempts_per_game" in st.session_state:
        average_attempts = np.mean(st.session_state.attempts_per_game)
        st.write(
            f"Average number of guesses per game: {average_attempts:.2f}"
        )

    # Dividing the list into rounds
    # rounds = []
    # index = 0
    # for round_size in st.session_state.attempts_per_game:
    #   rounds.append(st.session_state.list_quality[index:index + round_size])
    #  index += round_size  # Move the index forward by the size of the current round

    # Display the rounds
    # st.write(rounds)

    # test jule
    attempts_data = st.session_state.attempts_per_game  # attempts per game
    attempts_df = pd.DataFrame(attempts_data, columns=["Attempts"])
    themes = st.session_state.theme_per_game
    data_cat = pd.DataFrame(themes, columns=["category"])
    # time tracker per game

    # TODO: nochmal checken obs wirklich sekunden oder sek sind, ggbfs umrechnen?
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
        # this looks shit maybe without this one??
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
    # vorhin wurde der noch richtig angezeigt, jetzt ist di eleine weird kp wiesoooooo
    df = pd.DataFrame(
        {"game": [i for i in range(1, len(st.session_state.list_quality) + 1)],
         "Points for quality": st.session_state.list_quality})
    st.line_chart(df, x="game", y="Points for quality")
    st.caption("4 points: You guessed correct.")
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

# Durchschnittliche Rateversuche pro Spiel
# if "attempts_per_game" in st.session_state:  # Überprüfen, ob 'attempts_per_game' existiert
#    average_attempts = np.mean(st.session_state.attempts_per_game)  # Berechnung des Durchschnitts; np -> Durchschnitt der Rateversuche pro Spiel zu berechnen.
#    st.write(
#        f"Average number of guesses per game: {average_attempts:.2f}")  # Anzeige mit zwei Nachkommastellen (deshalb 2f)
# else:
#    st.write("No games were played yet.")

# Tabelle

#    df_uebersicht = pd.DataFrame({
#        'Gesamtzahl der Spiele': [number_games],
#        'Durchschnittliche Rateversuche': [average_attempts],
#    })

#    st.dataframe(df_uebersicht)

# Tabelle
# df_table = pd.DataFrame({
#    'Number of games played' : [number_games],
#   'Average number of guesses per game': [average_attempts],
#  })

# Grafische Darstellung (Balkendiagramm)
# if "attempts_per_game" in st.session_state:
#        attempts_data = st.session_state.attempts_per_game  # Daten aus dem Session State
#        df_barchart = pd.DataFrame(attempts_data, columns=["Attempts"])  # Erstellt Dataframe)
#
#        fig, ax = plt.subplots()
#        #  Erstellung von Diagrammen mit Matplotlib -  Ezeugt zwei objekte Figure (fig -> Container für gesamtes Diagramm, enthält alle Elemente)) und Axes (ax -> Koordinatensystem) Objekt
#        ax.bar(dataframe.index + 1, df_barchart["Attempts"], color='purple')  # Balkendiagramm gezeichnet
#        ax.set_title("Attempts per Game")  # Titel Diagramm
#        ax.set_xlabel("Game Number")  # Beschriftung x-Achse
#        ax.set_ylabel("Attempts")  # Beschriftung y-Achse
#
#        st.pyplot(fig)  # => Diagramm in Streamlit anzeigen

# - The "Stats" page displays some stats about playing like the number of games played, the average number of guesses per game.
# - The "Stats" page displays a bar chart showing he number of guesses for each game
# st.write("# Your Statistics \U0001F4CA")  #unicode for bar chart


# games per session

# if "input" not in st.session_state:
#   st.session_state.input = 0
# games = st.session_state.input
# if "attempt" not in st.session_state:
#   st.session_state.attempt = 0
# attempts per game
# attempts = st.session_state.attempt

# data = {
#   "games": games,
#  "attempts": attempts
# }

# if "attempts_per_game" not in st.session_state:
#   st.write("You haven't played any game yet)")
# else:
#   attempts_data = st.session_state.attempts_per_game
#  st.write(attempts_data)
# dfs = pd.DataFrame(attempts_data, columns=["Attempts"])
# st.write(dfs)

# Plotting the attempts per game
# fig, ax = plt.subplots()
# ax.bar(dfs.index + 1, dfs["Attempts"], color='purple')
# ax.set_title("Attempts per Game")
# ax.set_xlabel("Game Number")
# ax.set_ylabel("Attempts")

# st.pyplot(fig)