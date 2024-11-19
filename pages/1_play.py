import streamlit as st
import random



# Liste - Knowledgebase
Gods = ["Zeus", "Hera", "Poseidon", "Hades", "Athena", "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaistos", "Hermes", "Demeter", "Hestia"]
Hero = ["Herakles", "Achilles", "Odysseus", "Perseus", "Theseus", "Jason", "Atalante", "Orpheus"]
Creature = ["Medusa", "Minotaurus", "Pegasus", "Sphinx", "Zentauren", "Hydra", "Chimäre", "Harpien", "Sirenen"]
Titan = ["Gaia", "Uranos", "Kronos", "Rhea", "Nyx", "Erebos", "Prometheus", "Atlas"]

# Hinweise - die dem Spieler gegeben werden sollen
# - WAS MICH STÖRT:
# Ändere zu Englisch

# BISHER nur Götter, Frage: Alles zu einer Liste/ Mehrere Listen gestalten?) - geht auch schnell, mit Gruppe besprechen
hinweise = {
    # Götter
    "Zeus": ["Herrscher des Olymp", "Beherrsche den Blitz", "Vater von Herakles"],
    "Hera": ["Göttin der Ehe", "Eifersüchtig auf Zeus' Liebschaften", "Beschützerin der Frauen"],
    "Poseidon": ["Gott des Meeres", "Erzeuger von Erdbeben", "Trage einen Dreizack"],
    "Hades": ["Herrscher der Unterwelt", "Habe einen Helm der Unsichtbarkeit", "Entführte Persephone"],
    "Athena": ["Göttin der Weisheit", "Entsprang aus Zeus' Kopf", "Symbol: die Eule"],
    "Apollo": ["Gott der Musik", "Führer der Musen", "Gott des Lichts und der Prophezeiung"],
    "Artemis": ["Göttin der Jagd", "Zwilling von Apollo", "Schütze die Wälder"],
    "Ares": ["Gott des Krieges", "Symbol: Speer und Helm", "Verhasst von fast allen Göttern"],
    "Aphrodite": ["Göttin der Schönheit", "Geboren aus dem Meeresschaum", "Symbol: die Taube"],
    "Hephaistos": ["Gott der Schmiedekunst", "Entstellt und hinke", "Schmiedete die Waffen der Götter"],
    "Hermes": ["Götterbote", "Trage geflügelte Sandalen", "Beschützer von Reisenden"],
    "Demeter": ["Göttin der Ernte", "Mutter von Persephone", "Symbol: der Weizenkranz"],
    "Hestia": ["Göttin des Herdfeuers", "Symbol der Häuslichkeit", "Werde oft mit einem Herd dargestellt"],

    # Helden
    "Herakles": ["Stärkster Held", "Bekannt für 12 Aufgaben", "Tötete den Nemeischen Löwen"],
    "Achilles": ["Größter Held des Trojanischen Krieges", "Seine Ferse war verwundbar", "Getötet von Paris"],
    "Odysseus": ["König von Ithaka", "Listig und klug", "Baute das Trojanische Pferd"],
    "Perseus": ["Held, der Medusa tötete", "Sohn von Zeus und Danaë", "Rettete Andromeda vor einem Seeungeheuer"],
    "Theseus": ["Tötete den Minotaurus", "Führte Athen", "Benutzte einen Faden im Labyrinth"],
    "Jason": ["Anführer der Argonauten", "Suchte das Goldene Vlies", "Hatte Medea als Gefährtin"],
    "Atalante": ["Schnelle Läuferin", "Jägerin des Kalydonischen Ebers", "Bekannt für ihre Wettläufe"],
    "Orpheus": ["Berühmter Musiker", "Reiste in die Unterwelt", "Versuchte, Eurydike zu retten"],

    # Wesen
    "Medusa": ["Gorgone mit Schlangenhaaren", "Versteinert Menschen mit ihrem Blick", "Getötet von Perseus"],
    "Minotaurus": ["Halb Mensch, halb Stier", "Lebte im Labyrinth", "Besiegt von Theseus"],
    "Pegasus": ["Geflügeltes Pferd", "Entstand aus Medusas Blut", "Hilfte Bellerophon im Kampf"],
    "Sphinx": ["Löwenkörper und Menschenkopf", "Stellte Rätsel", "Besiegt von Ödipus"],
    "Zentauren": ["Halb Mensch, halb Pferd", "Wilde Natur", "Bekannt: Cheiron, ein weiser Lehrer"],
    "Hydra": ["Vielköpfiges Monster", "Jeder abgeschlagene Kopf wuchs nach", "Besiegt von Herakles"],
    "Chimäre": ["Mischwesen aus Löwe, Ziege und Schlange", "Feuerspeiend", "Besiegt von Bellerophon"],
    "Harpien": ["Geflügelte Frauen", "Symbol für Plagen und Diebstahl", "Belästigten König Phineus"],
    "Sirenen": ["Verführerische Sängerinnen", "Lockten Seefahrer ins Verderben", "Von Odysseus überlistet"],

    # Titanen
    "Gaia": ["Urmutter der Erde", "Mutter der Titanen", "Gegen Uranos rebelliert"],
    "Uranos": ["Personifikation des Himmels", "Gatte von Gaia", "Von Kronos gestürzt"],
    "Kronos": ["Titan der Zeit", "Verschlang seine Kinder", "Von Zeus gestürzt"],
    "Rhea": ["Titanin der Mutterschaft", "Rettete Zeus vor Kronos", "Mutter der Olympischen Götter"],
    "Nyx": ["Göttin der Nacht", "Mutter vieler Götter", "Symbol für Geheimnis und Dunkelheit"],
    "Erebos": ["Personifikation der Dunkelheit", "Gatte von Nyx", "Symbol der Schatten"],
    "Prometheus": ["Gab den Menschen das Feuer", "Wurde von Zeus bestraft", "Gilt als Wohltäter der Menschheit"],
    "Atlas": ["Trägt den Himmel auf seinen Schultern", "Titan des Widerstands", "Bruder von Prometheus"]
}

# Lösung erschaffen
def ziel_figur(theme):
    if theme == "Gods":
        return random.choice(Gods)
    elif theme == "Titan": 
        return random.choice(Titan)
    elif theme == "Creature": 
        return random.choice(Creature)
    else:
        return random.choice(Hero)


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
    option = st.selectbox( "What would you like to guess", ("Gods", "Hero", "Creature", "Titan"))
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
        else:
            st.write("Sorry, you Lost!, the solution was:", st.session_state.goal)
            st.session_state.over = True
if __name__ == '__main__':
    main()