import streamlit as st
import random
from openai import OpenAI
import base64
import time

# mp: tab name and icon
st.set_page_config(page_title="Play", page_icon="🎲")

# mp: initialize chat AI for hints
# mp: our API key stored in .streamlit/secrets.toml and added to gitignore file to prevent it to be uploaded in github
# mp checks and gives notification about valid/wrong/missing API key
api_key_valid = False  # mp: variable for checking if the API key is valid
info_bottom = ""  # mp: text variable for the bottom info area
model = "gpt-4o-mini"  # mp: model for OpenAI chat


# mp: function to check if the API key is valid
def is_api_key_valid(api_key):
    try:
        test_client = OpenAI(api_key=api_key)
        # mp: Makes simple request to test the key
        test_client.chat.completions.create(
            model=model,
            # messages=[]
            messages=[
                {"role": "system",
                 "content": "You are an expert on Greek mythology. Provide creative hints about Greek mythology characters."},
                {"role": "user", "content": "Give me a hint about Zeus."}
            ]
        )
        return True
    except:
        return False


if "OPENAI_API_KEY" in st.secrets and st.secrets["OPENAI_API_KEY"]:
    if is_api_key_valid(st.secrets["OPENAI_API_KEY"]):  # mp: checks if the key is valid
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        api_key_valid = True  # mp: set variable to true if the key is valid
        info_bottom = "Valid OpenAI API key found. Hints will be generated from LLM."
    else:
        info_bottom = "Invalid OpenAI API key. Hints will be generated from knowledge base instead of LLM"
else:
    client = OpenAI(api_key="invalid key")
    info_bottom = "Missing OpenAI API key. Hints will be generated from knowledge base instead of LLM."

##WAS MICH STÖRT!: Die pages App und Play sind basically die gleichen. Können wir das beheben? Ist eine von den beiden nicht zu viel?
## GIVE ME THE SOLUTION RIGHT AWAY EINBAUEN?
# FRAGE AN DIE GRUPPE: Hint lieber ausschreiben oder doch button?
## FRAGE AN DIE GRUPPE: Should we include a possibility that if the player doesnt want to guess this god to write out / press the button "give me another one" and he will get the answer and jump to the other?
## FRAGE AN DIE GRUPPE: Sollten wir dem Benutzer sagen, dass er nach auswahl der Kategorie auf "new game" drücken soll da sonst automatisch mit gott weitergespielt?
# FRAGE AN DIE GRUPPE : "Whar would you like to guess?" etwas größer machen die Schrift?
# TO BE DONE : AESTHETIK - HINTERGRUND- THEMATISCH ANPASSEN
# TO BE DONE: STATISTIK
# TO BE DONE: CHATBOT


# Liste - Knowledgebase
Gods = ["Zeus", "Hera", "Poseidon", "Hades", "Athena", "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaestus", "Hermes",
        "Demeter", "Hestia"]
Heroes = ["Heracles", "Achilles", "Odysseus", "Perseus", "Theseus", "Jason", "Atalanta", "Orpheus"]
Creatures = ["Medusa", "Minotaur", "Pegasus", "Sphinx", "Centaur", "Hydra", "Chimera", "Harpy", "Siren"]
Titans = ["Gaia", "Uranus", "Cronus", "Rhea", "Nyx", "Erebus", "Prometheus", "Atlas"]

# Hinweise - die dem Spieler gegeben werden sollen
# mp: hints from knowledgebase that will be given in case the API is not responding
hinweise = {
    # Gods
    "Zeus": ["Ruler of Olympus", "Controls lightning", "Father of Heracles"],
    "Hera": ["Goddess of marriage", "Jealous of Zeus' affairs", "Protector of women"],
    "Poseidon": ["God of the sea", "Creator of earthquakes", "Carries a trident"],
    "Hades": ["Ruler of the underworld", "Has a helmet of invisibility", "Kidnapped Persephone"],
    "Athena": ["Goddess of wisdom", "Sprang from Zeus' head", "Symbol = the owl"],
    "Apollo": ["God of music", "Leader of the Muses", "God of light and prophecy"],
    "Artemis": ["Goddess of the hunt", "Twin of Apollo", "Protector of the forests"],
    "Ares": ["God of war", "Symbol = spear and helmet", "Hated by almost all gods"],
    "Aphrodite": ["Goddess of beauty", "Born from sea foam", "Symbol = the dove"],
    "Hephaestus": ["God of blacksmiths", "Crippled and lame", "Forged the weapons of the gods"],
    "Hermes": ["Messenger of the gods", "Wears winged sandals", "Protector of travelers"],
    "Demeter": ["Goddess of the harvest", "Mother of Persephone", "Symbol = the wheat wreath"],
    "Hestia": ["Goddess of the hearth", "Symbol of domesticity", "Often depicted with a hearth"],

    # Heroes
    "Heracles": ["Strongest hero", "Known for 12 labors", "Killed the Nemean lion"],
    "Achilles": ["Greatest hero of the Trojan War", "His heel was vulnerable", "Killed by Paris"],
    "Odysseus": ["King of Ithaca", "Cunning and clever", "Built the Trojan Horse"],
    "Perseus": ["Hero who killed Medusa", "Son of Zeus and Danaë", "Saved Andromeda from a sea monster"],
    "Theseus": ["Killed the Minotaur", "Led Athens", "Used a thread in the labyrinth"],
    "Jason": ["Leader of the Argonauts", "Sought the Golden Fleece", "Had Medea as a companion"],
    "Atalanta": ["Fast runner", "Hunter of the Calydonian boar", "Known for her races"],
    "Orpheus": ["Famous musician", "Traveled to the underworld", "Tried to save Eurydice"],

    # Creatures
    "Medusa": ["Gorgon with snake hair", "Turns people to stone with her gaze", "Killed by Perseus"],
    "Minotaur": ["Half man, half bull", "Lived in the labyrinth", "Defeated by Theseus"],
    "Pegasus": ["Winged horse", "Born from Medusa's blood", "Helped Bellerophon in battle"],
    "Sphinx": ["Lion's body and human head", "Posed riddles", "Defeated by Oedipus"],
    "Centaur": ["Half man, half horse", "Wild nature", "Famous: Chiron, a wise teacher"],
    "Hydra": ["Many-headed monster", "Each severed head grew back", "Defeated by Heracles"],
    "Chimera": ["Hybrid of lion, goat, and snake", "Breathes fire", "Defeated by Bellerophon"],
    "Harpy": ["Winged women", "Symbol of plagues and theft", "Tormented King Phineus"],
    "Siren": ["Seductive singers", "Lured sailors to their doom", "Outwitted by Odysseus"],

    # Titans
    "Gaia": ["Primordial mother of the earth", "Mother of the Titans", "Rebelled against Uranus"],
    "Uranus": ["Personification of the sky", "Husband of Gaia", "Overthrown by Cronus"],
    "Cronus": ["Titan of time", "Swallowed his children", "Overthrown by Zeus"],
    "Rhea": ["Titaness of motherhood", "Saved Zeus from Cronus", "Mother of the Olympian gods"],
    "Nyx": ["Goddess of the night", "Mother of many gods", "Symbol of mystery and darkness"],
    "Erebus": ["Personification of darkness", "Husband of Nyx", "Symbol of shadows"],
    "Prometheus": ["Gave fire to humans", "Punished by Zeus", "Considered a benefactor of humanity"],
    "Atlas": ["Carries the sky on his shoulders", "Titan of endurance", "Brother of Prometheus"]
}


# Lösung erschaffen - Greift auf die verschiedenen Listen zu
def ziel_figur(theme):
    if theme == "Gods":
        return random.choice(Gods)
    elif theme == "Titans":
        return random.choice(Titans)
    elif theme == "Creatures":
        return random.choice(Creatures)
    else:
        return random.choice(
            Heroes)  ##Gruppe fragen: Warum heroes? als else?, d.h. wenn ich kein Thema aussuche wird mir Heroes vorgeschlagen/ nicht lieber god? Oder sollte der Spieler nicht gezwungen sein ein Thema auszuwählen?
    # else weil das die letzte option ist zuerst ist Gott ausgewählt.


# Aufbau für ein neues spiel
def initial_state(post_init=False):  # initial_state() dient dazu, den Anfangszustand deines Spiels zu definiere
    if not post_init:
        st.session_state.input = 0
        if "list_quality" not in st.session_state:
            st.session_state.list_quality = []
    st.session_state.games_played = 0  # von Hajar
    st.session_state.attempt = 0  # zählt die attempts pro spiel
    st.session_state.over = False
    st.session_state.hint_index = 2  # index = 2 um mit dem 3. hint zu starten
    st.session_state.maxattempts = 4  # max number of attempts 4
    st.session_state.hint_counter = 0  # Counting hints -- TODO: still to include in stats!! if we want to
    st.session_state.maxhints = 3  # Maximum number of hints


# mp collect data for statistics
def collect_stats():
    st.session_state.time = (time.time() - st.session_state.time_start)
    st.session_state.time_start = time.time()  # gives current date and time!

    if "time_per_game" not in st.session_state:
        st.session_state.time_per_game = []
        st.session_state.time_per_game.append(st.session_state.time)
    else:
        st.session_state.time_per_game.append(st.session_state.time)

    if "attempts_per_game" not in st.session_state:
        st.session_state.attempts_per_game = []
        st.session_state.attempts_per_game.append(st.session_state.attempt)
    else:
        st.session_state.attempts_per_game.append(st.session_state.attempt)
    # st.session_state.theme_per_game.append(st.session_state.option) #liste mit den themes per game
    if "theme_per_game" not in st.session_state:
        st.session_state.theme_per_game = []
        st.session_state.theme_per_game.append(st.session_state.option)
    else:
        st.session_state.theme_per_game.append(st.session_state.option)

    # Anzahl der Spiele erhöhen:
    st.session_state.input += 1


def restart_game():
    theme = st.session_state.option  # Access the theme directly from session state
    st.session_state.goal = ziel_figur(theme)  # This line changes the goal
    initial_state(post_init=True)


# mp function to handle category/option/theme change
def on_option_change():
    note = st.empty()
    if st.session_state.attempt == 0:  # If no attempts have been made in this game, then change the goal (hints are still counting down)
        st.session_state.goal = ziel_figur(st.session_state.option)
        st.session_state.hint_index = 2  # mp index = 2 um mit dem 3. hint zu starten
    elif st.session_state.over:  # mp start new game if the current game is over and the user selects a new option
        note_text = f"New Game started with theme {st.session_state.option} - good luck! 🍀"
        note.warning(note_text)
        restart_game()
    else:  # mp if attempts have already been made and the user selects a new option, then restart the game. Current game will count as lost
        note_text = f"Game restarted with new theme {st.session_state.option} - previous game discarded. 😢"
        note.warning(note_text)
        restart_game()


def main():
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
    global info_bottom  # mp: global variable for the bottom note
    # before the first game

    # Apply the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    if "goal" not in st.session_state:
        initial_option = 'Gods'  # mp: initial theme
        st.session_state.goal = ziel_figur(initial_option)
        st.session_state.option = initial_option
        st.session_state.time_start = time.time()  # gives current date and time!
        initial_state()

    st.markdown('''
    <div class = "my-container">
        <h1>Guess Figures of Greek Mythology 🏛️⚡</h1>
    </div>
    ''', unsafe_allow_html=True)
    # mp enables user to choose theme/option
    st.markdown(
        "<h3 style='font-size:16px;'>Choose a Figure you would like to guess to get started<br>(Do not change Figure during a game round to avoid inconveniences.)</h3>",
        unsafe_allow_html=True)
    st.selectbox(
        label="What would you like to guess? (Do not change during a game round to avoid inconveniences.)",
        options=("Gods", "Heroes", "Creatures", "Titans"),
        label_visibility="collapsed",  # mp hides the label
        key="option",  # mp This ensures that the selected option is stored in st.session_state.option
        # disabled = st.session_state.over, ### st.session_state.attempt > 0, ### If attempts have been made, then disable the selectbox
        on_change=on_option_change  # mp: this function will be called when the option/theme is changed
    )

    # mp: puts divider between selectbox and chat
    st.divider()

    # mp: Container for the chat
    with st.container():
        if not st.session_state.over:  # mp when game is over, container is gone
            user_input = st.chat_input("Type your guess or type 'hint'")

            if st.button("I give up"):
                st.session_state.over = True
                st.write(f" :blue Die richtige Antwort war: {st.session_state.goal}")

            if user_input:
                # mp: Game-chat logic
                if user_input.lower() == "hint":
                    st.session_state.hint_index = (
                                                              st.session_state.hint_index + 1) % 3  # mp iterating through knowledgebase hints, only required if openai not responding
                    # mp: display user msg
                    with st.chat_message("user"):
                        st.write(user_input)
                    # mp: AI hint response provided as a stream to simulate chatGPT-like appearance
                    with st.chat_message("assistant"):
                        # mp added max hint logic
                        if st.session_state.hint_counter < st.session_state.maxhints:
                            st.session_state.hint_counter += 1
                            if st.session_state.hint_counter > st.session_state.maxhints:
                                st.session_state.hint_counter = st.session_state.maxhints
                                # mp: define user message and LLM system
                            system_message = {"role": "system",
                                              "content": "You are an expert on Greek mythology. Provide creative hints about Greek mythology characters."}
                            user_message = {"role": "user", "content": f"Give me a hint about {st.session_state.goal}."}
                            # mp: Initialize response container
                            hint_response = ""
                            hint_container = st.empty()
                            # mp get AI hint as a stream
                            # mp "try" catch block to react to system error eg api is not responding
                            # mp response = result from openai api call as a stream, stream = true
                            try:
                                response = client.chat.completions.create(
                                    model=model,
                                    messages=[system_message, user_message],
                                    stream=True
                                )
                                # mp display response in chunks from stream
                                for chunk in response:
                                    delta = chunk.choices[0].delta
                                    if hasattr(delta, "content") and delta.content:
                                        hint_response += delta.content  # mp Accumulate the content
                                        hint_container.write(f"Hint: {hint_response}")
                            except:
                                # mp: if error occures eg api server done, fall back to knowledge base hints & provides note that KB instead of LLM is active
                                hint_response = hinweise[st.session_state.goal][2 - st.session_state.hint_index]
                                st.write(hint_response)
                                if api_key_valid:  ### mp: if the key is valid, then the error is not due to the key
                                    info_bottom = "Connection error. Hints will be generated from knowledge base instead of LLM."
                        else:  # mp max hints reached
                            # mp: if max hints reached, display message
                            st.write("You have used up your allowed hints!")
                else:  # mp user types a guess in chat
                    # mp: Display user chat (streamlit chat component)
                    with st.chat_message("user"):
                        st.write(user_input)
                    # mp: user did win
                    if user_input.lower() == st.session_state.goal.lower():
                        st.session_state.quality = "4"  # correct #jv: rates quality of guess, if correct: 4 points
                        st.session_state.list_quality.append(st.session_state.quality)
                        with st.chat_message("assistant"):
                            st.write("\U0001F389 Correct! You've guessed it!")  # mp unicode for emoji party popper
                        st.balloons()
                        st.session_state.over = True
                        collect_stats()
                    # mp: user did not guess correct, attempts 4
                    else:

                        # jv: check quality of guesses
                        # jv: save current themelist in categorie
                        if st.session_state.option == "Gods":
                            categorie = Gods
                        elif st.session_state.option == "Titans":
                            categorie = Titans
                        elif st.session_state.option == "Creatures":
                            categorie = Creatures
                        else:
                            categorie = Heroes
                        # jv: compare theme list to users input if user input for example: the goal is hera, theme is therefore gods, if the user guesses Zeus which is in Gods it is a good guess
                        if user_input.capitalize() in categorie:
                            st.session_state.quality = "3"
                        # jv: if the users input is in any theme just not the right one the guess is ok: the goal is hera, theme is god but the user guesses medusa
                        elif user_input.capitalize() in Gods:
                            st.session_state.quality = "2"
                        elif user_input.capitalize() in Heroes:
                            st.session_state.quality = "2"
                        elif user_input.capitalize() in Titans:
                            st.session_state.quality = "2"
                        elif user_input.capitalize() in Creatures:
                            st.session_state.quality = "2"
                        # jv: guess doesnt exist in our knowledge base guess is bad
                        else:
                            st.session_state.quality = "1"
                        st.session_state.list_quality.append(st.session_state.quality)

                        st.session_state.attempt += 1
                        # mp limit st.session_state.attempt to st.session_state.maxattempts
                        if st.session_state.attempt > st.session_state.maxattempts:
                            st.session_state.attempt = st.session_state.maxattempts

                        if st.session_state.attempt < st.session_state.maxattempts:
                            with st.chat_message("assistant"):
                                st.write(" :blue[Nope, try again!]")
                        else:  # mp user did not win
                            with st.chat_message("assistant"):
                                st.write(f" :blue[Sorry, you lost! The correct answer was:] {st.session_state.goal}")
                            st.session_state.over = True
                            collect_stats()

                            # Display attempts left
    # #if 'attempt' in st.session_state:
    # mp if game is not over
    if not st.session_state.over:
        max_attempts = st.session_state.maxattempts
        attempts_left = max_attempts - st.session_state.attempt
        max_hints = st.session_state.maxhints
        hints_left = max_hints - st.session_state.hint_counter
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f":blue[Attempts left: {attempts_left} of {max_attempts}]")
        with col2:
            # mp slider: counts down hints and attempts, visualisation of it
            st.slider("Attempts left", 0, max_attempts, (0, attempts_left), disabled=True, label_visibility="collapsed",
                      key="attempts_slider")
        with col3:
            st.write(f":blue[Hints left: {hints_left} of {max_hints}]")
        with col4:
            st.slider("Hints left", 0, max_hints, (0, hints_left), disabled=True, label_visibility="collapsed",
                      key="hints_slider")
            # mp if game is over
    else:
        col1, _, col2 = st.columns(3)
        with col1:
            st.button('Start a New Game', on_click=restart_game)
            # if 'attempt' in st.session_state:
            #   st.write(f" :blue[Attempts Left: {st.session_state.maxattempts - st.session_state.attempt}]")

        with col2:  # button to stats page
            if st.button("Check your game statistics"):
                st.switch_page("pages/2_📊_Game_Statistics.py")

    # Display the bottom info message
    info_area_bottom = st.empty()
    if info_bottom:
        info_area_bottom.info(info_bottom)


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

if __name__ == '__main__':
    main()






