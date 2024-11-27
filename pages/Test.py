import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import category

##STATISTIK ERST AKTUALISIERT WENN AUF "NEW GAME" GEKLICKT WIRD

# mp: tab name and icon
st.set_page_config(page_title="Game Statistics", page_icon="📊")

st.subheader ("Your Statistics")

if "input" not in st.session_state:
    st.session_state.input = 0

# Anzahl der Spiele
if "input" in st.session_state:
    number_games = st.session_state.input
    st.write(f"Number of games played: {number_games}") # "f" für f-string -> ermöglicht, Variablen direkt in Strings einzubetten.
else:
    st.write("No games were played yet.")

#if "rounds_per_category" not in st.session_state:
 #   st.session_state.rounds_per_category = {"Gods": 0, "Titans": 0, "Creatures": 0, "Heroes": 0}

#if "games_per_category" not in st.session_state:
#    st.session_state.games_per_category = {"Gods": 0, "Titans": 0, "Creatures": 0, "Heroes": 0}


# Tabelleninhalte initialisieren
tabellen_daten = {
    'Gesamtzahl der Spiele': [number_games],
    #'Category': [st.session_state.games_per_category["Gods", "Titans", "Creatures", "Heroes"]],
}

# Durchschnittliche Rateversuche pro Spiel
if "attempts_per_game" in st.session_state:
    average_attempts = np.mean(st.session_state.attempts_per_game)
    st.write(
        f"Average number of guesses per game: {average_attempts:.2f}"
    )

    # Spalte zur Tabelle hinzufügen
    tabellen_daten['Durchschnittliche Rateversuche'] = [average_attempts]
###
# Tabelle
chart_data = pd.DataFrame(tabellen_daten, columns = ["Gods","Titans","Heroes","Creatures"])
#chart_data = pd.DataFrame({
#    "Kategorie": ["Gods", "Titans", "Heroes", "Creatures"],
#    "Anzahl Spiele": [st.session_state.games_per_category[kategorie] for kategorie in ["Gods", "Titans", "Heroes", "Creatures"]]
#})

st.dataframe(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data, y_label = 'Rounds played', stack = False)




# bei dem stack dann halt die verschiedenen Kategorien
# Durchschnittliche Rateversuche pro Spiel
#if "attempts_per_game" in st.session_state:  # Überprüfen, ob 'attempts_per_game' existiert
#    average_attempts = np.mean(st.session_state.attempts_per_game)  # Berechnung des Durchschnitts; np -> Durchschnitt der Rateversuche pro Spiel zu berechnen.
#    st.write(
#        f"Average number of guesses per game: {average_attempts:.2f}")  # Anzeige mit zwei Nachkommastellen (deshalb 2f)
#else:
#    st.write("No games were played yet.")

# Tabelle

#    df_uebersicht = pd.DataFrame({
#        'Gesamtzahl der Spiele': [number_games],
#        'Durchschnittliche Rateversuche': [average_attempts],
#    })

#    st.dataframe(df_uebersicht)

    #Tabelle
   # df_table = pd.DataFrame({
    #    'Number of games played' : [number_games],
     #   'Average number of guesses per game': [average_attempts],
  #  })

# Grafische Darstellung (Balkendiagramm)
#if "attempts_per_game" in st.session_state:
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

#- The "Stats" page displays some stats about playing like the number of games played, the average number of guesses per game.
#- The "Stats" page displays a bar chart showing he number of guesses for each game
#st.write("# Your Statistics \U0001F4CA")  #unicode for bar chart


#games per session

#if "input" not in st.session_state:
 #   st.session_state.input = 0
#games = st.session_state.input
#if "attempt" not in st.session_state:
 #   st.session_state.attempt = 0
#attempts per game
#attempts = st.session_state.attempt

#data = {
 #   "games": games,
  #  "attempts": attempts
#}

#if "attempts_per_game" not in st.session_state:
 #   st.write("You haven't played any game yet)")
#else:
 #   attempts_data = st.session_state.attempts_per_game
  #  st.write(attempts_data)
   # dfs = pd.DataFrame(attempts_data, columns=["Attempts"])
   # st.write(dfs)

    # Plotting the attempts per game
    #fig, ax = plt.subplots()
    #ax.bar(dfs.index + 1, dfs["Attempts"], color='purple')
    #ax.set_title("Attempts per Game")
    #ax.set_xlabel("Game Number")
    #ax.set_ylabel("Attempts")

    #st.pyplot(fig)