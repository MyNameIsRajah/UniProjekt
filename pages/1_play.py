import streamlit as st
import random



# Liste - Knowledgebase
Gods = ["Zeus", "Hera", "Poseidon", "Hades", "Athena", "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaestus", "Hermes", "Demeter", "Hestia"]
Heroes = ["Heracles", "Achilles", "Odysseus", "Perseus", "Theseus", "Jason", "Atalanta", "Orpheus"]
Creatures = ["Medusa", "Minotaur", "Pegasus", "Sphinx", "Centaurs", "Hydra", "Chimera", "Harpies", "Sirens"]
Titans = ["Gaia", "Uranus", "Cronus", "Rhea", "Nyx", "Erebus", "Prometheus", "Atlas"]

# Hinweise - die dem Spieler gegeben werden sollen
# - WAS MICH STÖRT:
# Ändere zu Englisch

# BISHER nur Götter, Frage: Alles zu einer Liste/ Mehrere Listen gestalten?) - geht auch schnell, mit Gruppe besprechen
hinweise = {
    # Gods
    "Zeus": ["Ruler of Olympus", "Controls lightning", "Father of Heracles"],
    "Hera": ["Goddess of marriage", "Jealous of Zeus' affairs", "Protector of women"],
    "Poseidon": ["God of the sea", "Creator of earthquakes", "Carries a trident"],
    "Hades": ["Ruler of the underworld", "Has a helmet of invisibility", "Kidnapped Persephone"],
    "Athena": ["Goddess of wisdom", "Sprang from Zeus' head", "Symbol: the owl"],
    "Apollo": ["God of music", "Leader of the Muses", "God of light and prophecy"],
    "Artemis": ["Goddess of the hunt", "Twin of Apollo", "Protector of the forests"],
    "Ares": ["God of war", "Symbol: spear and helmet", "Hated by almost all gods"],
    "Aphrodite": ["Goddess of beauty", "Born from sea foam", "Symbol: the dove"],
    "Hephaestus": ["God of blacksmiths", "Crippled and lame", "Forged the weapons of the gods"],
    "Hermes": ["Messenger of the gods", "Wears winged sandals", "Protector of travelers"],
    "Demeter": ["Goddess of the harvest", "Mother of Persephone", "Symbol: the wheat wreath"],
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
    "Centaurs": ["Half man, half horse", "Wild nature", "Famous: Chiron, a wise teacher"],
    "Hydra": ["Many-headed monster", "Each severed head grew back", "Defeated by Heracles"],
    "Chimera": ["Hybrid of lion, goat, and snake", "Breathes fire", "Defeated by Bellerophon"],
    "Harpies": ["Winged women", "Symbol of plagues and theft", "Tormented King Phineus"],
    "Sirens": ["Seductive singers", "Lured sailors to their doom", "Outwitted by Odysseus"],

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

# Lösung erschaffen
def ziel_figur(theme):
    if theme == "Gods":
        return random.choice(Gods)
    elif theme == "Titan": 
        return random.choice(Titans)
    elif theme == "Creature": 
        return random.choice(Creatures)
    else:
        return random.choice(Heroes)


#Aufbau für ein neues spiel
def initial_state(post_init=False):
    if not post_init:
        st.session_state.input = 0
    #neues spiel neue Lösung
    
    st.session_state.attempt = 0 # zählt die attempts pro spiel
    st.session_state.over = False
    st.session_state.hint_index = 2 #index = 2 um mit dem 3. hint zu starten

#neues spiel wird gestartet, input +1
def restart_game():
    if "attempts_per_game" not in st.session_state:
            st.session_state.attempts_per_game = []
            st.session_state.attempts_per_game.append(st.session_state.attempt)
    theme = st.session_state.option  # Access the theme directly from session state
    
    st.session_state.goal = ziel_figur(theme)  # This line changes the goal
    
    initial_state(post_init=True)
    st.session_state.input += 1  # counts how many games have been played
#hinweis aus der Liste
#warum wird hier goal geändert?!?!?
def get_hint(hint_index):
    
     return hinweise[st.session_state.goal][hint_index]

def main():
    st.write(
        """
        # Guess The God !!
        """
    )
    #enables user to choose a theme
    option = st.selectbox( "What would you like to guess", ("Gods", "Heroes", "Creatures", "Titans"))
     # Save the selected option to session state
    st.session_state.option = option  # Store the option in session state



    #before the first game
    if "goal" not in st.session_state:
        st.session_state.goal = ziel_figur(option)
        initial_state()
        

    #button to start a new game
        

    st.button('New game', on_click=restart_game)
    hint_text = st.empty()
    #User can try to guess here
    users_guess = st.text_input("Antwort: ",key ="guess")

    col1, _, _, _, col2 = st.columns(5)
    with col1:
        hint = st.button('I need a Hint')

    with col2:
        #before first guess
        if not users_guess:
            st.write(f"Attempt Left : 4")
        # after 1st guess
        if users_guess:
            st.write(f"Attempt Left : {3-st.session_state.attempt}")
    #if the hint button was clicked give a hint, first the last one of the list, then 2nd and so on, aber momentan wird dann session.state.goal geändert cih weiß nicht wieso
    if hint:  
        hint_response = get_hint(st.session_state.hint_index)
        if st.session_state.hint_index == 2:
            st.session_state.hint_index = 0
        elif st.session_state.hint_index == 0:
            st.session_state.hint_index = 1
        else :
            st.session_state.hint_index = 2
        hint_text.info(f'{hint_response}')
    #if the user guessed something check for correctnes:
    if users_guess:

        if st.session_state.attempt < 3:
            st.session_state.attempt += 1
            if users_guess.lower() != st.session_state.goal.lower():
                st.write("Nope, try again.")
            else:
                st.write("Nice, you are correct!")
                st.balloons()
                st.session_state.over = True
                # Store the number of attempts for the current game
                if "attempts_per_game" not in st.session_state:
                    st.session_state.attempts_per_game = []
                st.session_state.attempts_per_game.append(st.session_state.attempt)
        else:
            st.write("Sorry, you Lost!, the solution was:", st.session_state.goal)
            st.session_state.over = True
            if "attempts_per_game" not in st.session_state:
                st.session_state.attempts_per_game = []
            st.session_state.attempts_per_game.append(st.session_state.attempt)
if __name__ == '__main__':
    main()