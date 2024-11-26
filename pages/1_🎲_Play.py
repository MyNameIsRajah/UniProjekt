import streamlit as st
import random
from openai import OpenAI
import base64
# mp: tab name and icon
st.set_page_config(page_title="Play", page_icon="🎲")


# mp: initialize chat AI for hints
# mp: our API key stored in .streamlit/secrets.toml and added to gitignore file to prevent it to be uploaded in github
# mp checks and gives notification about valid/wrong/missing API key 
api_key_valid = False # mp: variable for checking if the API key is valid
info_bottom = "" # mp: text variable for the bottom info area
model = "gpt-4o-mini" # mp: model for OpenAI chat
# mp: function to check if the API key is valid
def is_api_key_valid(api_key):
    try:
        test_client = OpenAI(api_key=api_key)
        # mp: Makes simple request to test the key
        test_client.chat.completions.create(  
            model=model,
            #messages=[]
            messages=[
                {"role": "system", "content": "You are an expert on Greek mythology. Provide creative hints about Greek mythology characters."},
                {"role": "user", "content": "Give me a hint about Zeus."}
            ]
        )
        return True
    except: 
        return False
    
if "OPENAI_API_KEY" in st.secrets and st.secrets["OPENAI_API_KEY"]:
    if is_api_key_valid(st.secrets["OPENAI_API_KEY"]): # mp: checks if the key is valid
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) 
        api_key_valid = True # mp: set variable to true if the key is valid
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
#TO BE DONE : AESTHETIK - HINTERGRUND- THEMATISCH ANPASSEN
#TO BE DONE: STATISTIK
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
        return random.choice(Heroes) ##Gruppe fragen: Warum heroes? als else?, d.h. wenn ich kein Thema aussuche wird mir Heroes vorgeschlagen/ nicht lieber god? Oder sollte der Spieler nicht gezwungen sein ein Thema auszuwählen? 
    #else weil das die letzte option ist zuerst ist Gott ausgewählt. 


# Aufbau für ein neues spiel
def initial_state(post_init=False): #initial_state() dient dazu, den Anfangszustand deines Spiels zu definiere
    if not post_init: ##Woher kommt das post_init?
        # st.session_state.update (
        #     {
        #         "games played": 0,
        #         "attempt": 0,
        #         "over": False,
        #         "hint_index": 2,
        #         "maxattempts": 4,
        #         "input": 0, # Initialisierung von Input
        #     }
        # )
    # neues spiel neue Lösung - AUSKOMMENTIERT UM KOMPAKTE VERSION AUSZUPROBIEREN 
    # #mp 24/11: voherige version wieder hergestellt
        st.session_state.input = 0
    st.session_state.games_played = 0 #von Hajar
    st.session_state.attempt = 0  # zählt die attempts pro spiel
    st.session_state.over = False
    st.session_state.hint_index = 2  # index = 2 um mit dem 3. hint zu starten
    st.session_state.maxattempts = 4  # max number of attempts 4
    st.session_state.hint_counter = 0 # Counting hints -- TODO: still to include in stats!! if we want to
    st.session_state.maxhints = 3  # Maximum number of hints

# neues spiel wird gestartet, input +1 (indem benötigte Variablen in st.session aktualisiert)
#def restart_game():
#    if "attempts_per_game" not in st.session_state:
#        st.session_state.attempts_per_game = []
#        st.session_state.attempts_per_game.append(st.session_state.attempt)
#    theme = st.session_state.option  # Access the theme directly from session state
#    st.session_state.goal = ziel_figur(theme)  # This line changes the goal
#    initial_state(post_init=True)
#    st.session_state.input += 1  # counts how many games have been played - IN TOTAL?


def restart_game(): 
    if "attempts_per_game" not in st.session_state:
        st.session_state.attempts_per_game = []
        st.session_state.attempts_per_game.append(st.session_state.attempt)
    else :
        st.session_state.attempts_per_game.append(st.session_state.attempt)

    theme = st.session_state.option # Access the theme directly from session state
    st.session_state.goal = ziel_figur(theme) # This line changes the goal
    initial_state(post_init=True)

    # Anzahl der Spiele erhöhen:
    st.session_state.input += 1


    # hinweis aus der Liste
# warum wird hier goal geändert?!?!?
# mp: this function can be removed, fctnality moved to def main to enable streaming AI hints
# def get_hint(hint_index):  
   
#     chat_completion = client.chat.completions.create(  
#         model=model,
#         messages=[
#                     {"role": "system", "content": "You are an expert on Greek mythology. Provide creative hints about Greek mythology characters."},
#                     {"role": "user", "content": f"Give me a hint about {st.session_state.goal}."}
#                 ]
#     )   
#     return chat_completion.choices[0].message.content
    # if goal in hinweise:
    #     #Zugriff aus Hinweis in umgekehrter Reihenfolge (3-2-1)
    #     return hinweise [goal][2 - hint_index]
    # else:
    #     return "Für dieses Ziel sind keine Hinweise verfügbar." # wird doch eigentlich nie erreicht oder? Schafft ihr es den dude zusowas zu bringen?

# ALSOOO zum Verständnis, as far as i understood:
#Hier greifst du auf hinweise[st.session_state.goal] zu, um den Hinweis für das aktuelle Ziel abzurufen. Wenn der Schlüssel st.session_state.goal nicht im Dictionary hinweise existiert, wird ein neuer Eintrag erstellt, und dies könnte die unerwartete Änderung von session.state.goal verursachen.
# Änderung: st.session_state.goal immer im Dictionary hinweise vorhanden ist, bevor du darauf zugreifs


#mp function to handle category/option/theme change
def on_option_change():
    note = st.empty()
    if st.session_state.attempt == 0: ### If no attempts have been made in this game, then change the goal (hints are still countig down)
        st.session_state.goal = ziel_figur(st.session_state.option)
        st.session_state.hint_index = 2  # mp index = 2 um mit dem 3. hint zu starten
    elif st.session_state.over: #mp start new game if the current game is over and the user selects a new option        
        note_text = f"New Game started with theme {st.session_state.option} - good luck! 🍀"
        note.warning(note_text)
        restart_game()
    else: #mp if attempts have already been made and the user selects a new option, then restart the game. Current game will count as lost      
        note_text = f"Game restarted with new theme {st.session_state.option} - previous game counted as lost. 😢"
        note.warning(note_text)
        restart_game()



def main():
    global info_bottom # mp: global variable for the bottom note
    # before the first game
    if "goal" not in st.session_state:
        initial_option = 'Gods' #mp: initial theme
        st.session_state.goal = ziel_figur(initial_option)
        st.session_state.option = initial_option
        initial_state()
    st.write(
        """
        # :blue[Guess Figures of Greek Mythology]
        """
    )
    #mp enables user to choose theme/option
    st.markdown("<h3 style='font-size:16px;'>Choose a Figure you would like to guess to get started<br>(Do not change Figure during a game round to avoid inconveniences.)</h3>", unsafe_allow_html=True)
    st.selectbox(
        label="What would you like to guess? (Do not change during a game round to avoid inconveniences.)", 
        options=("Gods", "Heroes", "Creatures", "Titans"), 
        label_visibility="collapsed", #mp hides the label
        key = "option", #mp This ensures that the selected option is stored in st.session_state.option
        # disabled = st.session_state.over, ### st.session_state.attempt > 0, ### If attempts have been made, then disable the selectbox
        on_change = on_option_change #mp: this function will be called when the option/theme is changed
        )
    
    # enables user to choose a theme, on_change a new game is automatically initialized
    #PROBLEM: es wird immernoch die letzte figur benutzt ##mp auskommentiert, siehe st.selectbox oben
    #option = st.selectbox(" :grey[Choose a Figure you would like to guess to get started]", ("Gods", "Heroes", "Creatures", "Titans"), on_change =restart_game)
    # Save the selected option to session state
    #st.session_state.option = option  # Store the option in session state
  
    # before the first game mp: auskommentiert - moved and edited at the beginning of def main
    #if "goal" not in st.session_state:
     #   st.session_state.goal = ziel_figur(option)
      #  initial_state()

    # button to start a new game
    # st.button('New game', on_click=restart_game) #mp: TODO move to other place
    #hint_text = st.empty()

    # mp: puts divider between selectbox and chat
    st.divider()

    # mp: Container for the chat
    with st.container(): 
        if not st.session_state.over: # mp when game is over, container is gone
            user_input = st.chat_input("Type your guess or type 'hint'")
            if user_input:
                # mp: Game-chat logic
                if user_input.lower() == "hint":
                    st.session_state.hint_index = (st.session_state.hint_index + 1) % 3 #mp iterating through knowledgebase hints, only required if openai not responding
                     # mp: display user msg
                    with st.chat_message("user"):
                        st.write(user_input)
                    # mp: AI hint response provided as a stream to simulate chatGPT-like appearance
                    with st.chat_message("assistant"):
                        #mp added max hint logic
                        if st.session_state.hint_counter < st.session_state.maxhints: 
                            st.session_state.hint_counter += 1 
                            if st.session_state.hint_counter > st.session_state.maxhints: 
                                st.session_state.hint_counter = st.session_state.maxhints 
                            # mp: define user message and LLM system
                            system_message = {"role": "system", "content": "You are an expert on Greek mythology. Provide creative hints about Greek mythology characters."}
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
                                hint_response = hinweise [st.session_state.goal][2 - st.session_state.hint_index]
                                st.write(hint_response)
                                if api_key_valid: ### mp: if the key is valid, then the error is not due to the key
                                    info_bottom = "Connection error. Hints will be generated from knowledge base instead of LLM."
                        else: # mp max hints reached
                            # mp: if max hints reached, display message
                            st.write("You have used up your allowed hints!")
                else: #mp user types a guess in chat 
                    # mp: Display user chat (streamlit chat component)
                    with st.chat_message("user"):
                        st.write(user_input)
                    # mp: user did win
                    if user_input.lower() == st.session_state.goal.lower():
                        with st.chat_message("assistant"):
                            st.write("\U0001F389 Correct! You've guessed it!") #mp unicode for emoji party popper
                        st.balloons()
                        st.session_state.over = True
                        # Automatischer Wechsel zur nächsten Frage ##mp auskommentiert bc doesnt work 
                        #theme = st.session_state.option
                        #st.session_state.goal = ziel_figur(theme)
                    # mp: user did not win, attempts 4 
                    else:
                        st.session_state.attempt += 1
                        #mp limit st.session_state.attempt to st.session_state.maxattempts 
                        if st.session_state.attempt > st.session_state.maxattempts:
                            st.session_state.attempt = st.session_state.maxattempts

                        if st.session_state.attempt < st.session_state.maxattempts:
                            with st.chat_message("assistant"):
                                st.write(" :blue[Nope, try again!]")
                        else:
                            with st.chat_message("assistant"):
                                st.write(f" :blue[Sorry, you lost! The correct answer was:] {st.session_state.goal}")
                            st.session_state.over = True   
                             
      # Display attempts left
    # #if 'attempt' in st.session_state:
    #mp if game is not over
    if not st.session_state.over:
        max_attempts = st.session_state.maxattempts
        attempts_left = max_attempts - st.session_state.attempt
        max_hints = st.session_state.maxhints
        hints_left = max_hints - st.session_state.hint_counter
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f":blue[Attempts left: {attempts_left} of {max_attempts}]")
        with col2:
            #mp slider: counts down hints and attempts, visualisation of it
            st.slider("Attempts left", 0, max_attempts, (0, attempts_left), disabled=True, label_visibility="collapsed", key="attempts_slider")
        with col3:
            st.write(f":blue[Hints left: {hints_left} of {max_hints}]")   
        with col4:
            st.slider("Hints left", 0, max_hints, (0, hints_left), disabled=True, label_visibility="collapsed", key="hints_slider")  
    #mp if game is over 
    else:                    
        col1, _, col2 = st.columns(3)
        with col1:
            st.button('Start a New Game', on_click=restart_game) 
            #if 'attempt' in st.session_state:
             #   st.write(f" :blue[Attempts Left: {st.session_state.maxattempts - st.session_state.attempt}]")

        with col2: #button to stats page
            if st.button("Check your game statistics") :
                st.switch_page("pages/2_📊_Game_Statistics.py")


    # Display the bottom info message
    info_area_bottom = st.empty()
    if info_bottom: 
        info_area_bottom.info(info_bottom)
    
 #set background image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("./image.png")
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

