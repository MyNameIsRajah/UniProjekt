import streamlit as st
import random
from openai import OpenAI

# mp: tab name and icon
st.set_page_config(page_title="Play", page_icon="🎲")


# mp: initialize chat AI for hints
# mp: our API key stored in .streamlit/secrets.toml and gitignore file to prevent it to be uploaded in github
# mp: checks if the key OPENAI_API_KEY exists in screts.toml and if it has a value - prevents system/app error, provides dummy key(invalid key)
if "OPENAI_API_KEY" in st.secrets and st.secrets["OPENAI_API_KEY"]:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) 
else:
    client = OpenAI(api_key="invalid key") 
model = "gpt-4o-mini"


##WAS MICH STÖRT!: Die pages App und Play sind basically die gleichen. Können wir das beheben? Ist eine von den beiden nicht zu viel?
## FRAGE AN DIE GRUPPE: Hint lieber ausschreiben oder doch button?
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
Creatures = ["Medusa", "Minotaur", "Pegasus", "Sphinx", "Centaurs", "Hydra", "Chimera", "Harpies", "Sirens"]
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
    st.session_state.maxattempts = 4  # maxattempts 4


# neues spiel wird gestartet, input +1 (indem benötigte Variablen in st.session aktualisiert)
def restart_game():
    if "attempts_per_game" not in st.session_state:
        st.session_state.attempts_per_game = []
        st.session_state.attempts_per_game.append(st.session_state.attempt)
    theme = st.session_state.option  # Access the theme directly from session state
    st.session_state.goal = ziel_figur(theme)  # This line changes the goal
    initial_state(post_init=True)
    st.session_state.input += 1  # counts how many games have been played - IN TOTAL?


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

def main():
    st.write(
        """
        # Guess Figures of Greek Mythology
        """
    )
    # enables user to choose a theme
    option = st.selectbox("What would you like to guess", ("Gods", "Heroes", "Creatures", "Titans"))
    # Save the selected option to session state
    st.session_state.option = option  # Store the option in session state

    # before the first game
    if "goal" not in st.session_state:
        st.session_state.goal = ziel_figur(option)
        initial_state()

    # button to start a new game

    st.button('New game', on_click=restart_game)
    hint_text = st.empty()
    # User can try to guess here
    # users_guess = st.text_input("Antwort: ",key ="guess")

# mp: Container for the chat
    with st.container():  
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
                    except Exception as e:
                        # st.error(f"An error occurred: {e}") #mp: this was the error message but we dont need it anymore bc we use kb
                        # mp: if error occures eg api key not valid, fall back to knowledge base hints & provides note that KB instead of LLM is active
                        no_key_msg = "Note: Missing or invalid API key - hints from knowledge base instead of LLM"
                        hint_text.info(no_key_msg)
                        hint_response = hinweise [st.session_state.goal][2 - st.session_state.hint_index]
                        st.write(hint_response)

                ## mp: OPTIONAL version without streaming
                # mp: here chat.completion is basically response in the version with streaming
                # with st.chat_message("assistant"):
                #     chat_completion = client.chat.completions.create(  
                #         model=model,
                #         messages=[
                #         {"role": "system", "content": "You are an expert on Greek mythology. Provide creative hints about Greek mythology characters."},
                #         {"role": "user", "content": f"Give me a hint about {st.session_state.goal}."}
                #         ]
                #     )
                #     hint_response = chat_completion.choices[0].message.content 
                #     st.write(f"Hint:  {hint_response}")
            else:
                # mp: Display user chat (streamlit chat component)
                with st.chat_message("user"):
                    st.write(user_input)
                # mp: user did win
                if user_input.lower() == st.session_state.goal.lower():
                    with st.chat_message("assistant"):
                        st.write("\U0001F389 Correct! You've guessed it!") #mp unicode for emoji party popper
                    st.balloons()
                    st.session_state.over = True
                    # Automatischer Wechsel zur nächsten Frage
                    theme = st.session_state.option
                    st.session_state.goal = ziel_figur(theme)
                # mp: user did not win, attempts 4 
                else:
                    st.session_state.attempt += 1
                    if st.session_state.attempt < st.session_state.maxattempts:
                        with st.chat_message("assistant"):
                            st.write("Nope, try again!")
                    else:
                        with st.chat_message("assistant"):
                            st.write(f"Sorry, you lost! The correct answer was: {st.session_state.goal}")
                        st.session_state.over = True   
                        st.session_state.attempt = st.session_state.maxattempts 
                        # mp: todo, what happens after game over eg collecting stats and restart game?
                # mp : auskommentiert und oben neu verschachtelt um attempts zu fixen                    
                # elif st.session_state.attempt <= st.session_state.maxattempts:
                #     st.session_state.attempt += 1
                #     with st.chat_message("assistant"):
                #         st.write("Nope, try again!")
                # else:
                #     with st.chat_message("assistant"):
                #         st.write(f"Sorry, you lost! The correct answer was: {st.session_state.goal}")
                #     st.session_state.over = True

    # Display attempts left
    if 'attempt' in st.session_state:
        st.write(f"Attempts Left: {st.session_state.maxattempts - st.session_state.attempt}")

    # col1, _, _, _, col2 = st.columns(5)
    # with col1:
    #     hint = st.button('I need a Hint')

    # with col2:
    #     #before first guess
    #     if not users_guess:
    #         st.write(f"Attempt Left : 4")
    #     # after 1st guess
    #     if users_guess:
    #         st.write(f"Attempt Left : {3-st.session_state.attempt}")
    # #if the hint button was clicked give a hint, first the last one of the list, then 2nd and so on, aber momentan wird dann session.state.goal geändert cih weiß nicht wieso
    # if hint:
    #     hint_response = get_hint(st.session_state.hint_index)
    #     if st.session_state.hint_index == 2:
    #         st.session_state.hint_index = 0
    #     elif st.session_state.hint_index == 0:
    #         st.session_state.hint_index = 1
    #     else :
    #         st.session_state.hint_index = 2
    #     hint_text.info(f'{hint_response}')
    # #if the user guessed something check for correctnes:
    # if users_guess:

    #     if st.session_state.attempt < 3:
    #         st.session_state.attempt += 1
    #         if users_guess.lower() != st.session_state.goal.lower():
    #             st.write("Nope, try again.")
    #         else:
    #             st.write("Nice, you are correct!")
    #             st.balloons()
    #             st.session_state.over = True
    #             # Store the number of attempts for the current game
    #             if "attempts_per_game" not in st.session_state:
    #                 st.session_state.attempts_per_game = []
    #             st.session_state.attempts_per_game.append(st.session_state.attempt)
    #     else:
    #         st.write("Sorry, you Lost!, the solution was:", st.session_state.goal)
    #         st.session_state.over = True
    #         if "attempts_per_game" not in st.session_state:
    #             st.session_state.attempts_per_game = []
    #         st.session_state.attempts_per_game.append(st.session_state.attempt)


if __name__ == '__main__':
    main()