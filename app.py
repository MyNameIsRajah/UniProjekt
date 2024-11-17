import streamlit as st
import random #SEE IF THATS GOOD

st.title("Greek Mythology")
#test
st.write("This is my first web app.")
# Unterüberschrift - Font ändern
st.markdown ("Welcome to our guessing game about the greek mythology. Can you guess the mythological figures I am thinking about?")

# Initialisieurngen
#versuche = 0


# Liste - Knowledgebase
goetter = ["Zeus", "Hera", "Poseidon", "Hades", "Athena", "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaistos", "Hermes", "Demeter", "Hestia"]
helden = ["Herakles", "Achilles", "Odysseus", "Perseus", "Theseus", "Jason", "Atalante", "Orpheus"]
wesen = ["Medusa", "Minotaurus", "Pegasus", "Sphinx", "Zentauren", "Hydra", "Chimäre", "Harpien", "Sirenen"]
titanen = ["Gaia", "Uranos", "Kronos", "Rhea", "Nyx", "Erebos", "Prometheus", "Atlas"]

# Hinweise - die dem Spieler gegeben werden sollen
# - WAS MICH STÖRT:
# Ändere zu Englisch
# Das system soll mit dem Schwierigsten (3. Position) beginnen und nicht random - schaue unten in main-Funktion - Ansatz: hinweis index auf 2 ändern?
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

# Zielfigur auswahl - noch auskommentieren
if "ziel_figur" not in st.session_state:
  st.session_state.ziel_figur = random.choice(goetter)  # Beispiel: Götterliste - schauen ob noch von anderen / zusammenstellen? (siehe oben - Gruppenbesprechung dafür)
  st.session_state.hinweis_index = 2
  st.session_state.versuche = 0

def check_answer():
    if antwort.lower() == st.session_state.ziel_figur.lower(): # Antwort eingabe
        st.write("Sehr gut, du liegst richtig! Wer bin ich jetzt? ...")   ###HIER Liegt ein Problem vor -> Wenn ich richtig liege, aktualisiert es nicht zum nächsten Gott, stattdessen muss ich wieder eine falsche Eingabe machen, bis es den nächsten zeigt; Interface: 'Wer bin ich' und 'wer bin ich jetzt' vedoppeln sich an der stelle, ästhetisches Probelm
        st.session_state.ziel_figur = random.choice(goetter)  # Beispiel: Götterliste
        st.session_state.hinweis_index = 0
        st.session_state.versuche = 0
   # st.experimental_rerun() -> Wurde das nicht vom Tobi genutzt?!
##HIER Liegt ein Problem -> Die website lässt mich nicht raten sondern sagt mir sofort dass ich falsch liege, d.h.es wird erst gar nicht auf meine Antwort gewartet
    else:
        st.session_state.versuche += 1
        if st.session_state.versuche < 3:
            st.write("Nein, du liegst falsch.")
            st.session_state.hinweis_index -= 1
            st.write(hinweise[st.session_state.ziel_figur][st.session_state.hinweis_index])

        else:
            st.write("Du hast verloren! Ich bin", st.session_state.ziel_figur)
            st.session_state.ziel_figur = random.choice(goetter)  # Beispiel: Götterliste
            st.session_state.hinweis_index = 0
            st.session_state.versuche = 0
        #st.experimental_rerun() # auskommentieren

## An Nutzer:
st.write("Wer bin ich?")
#st.write(hinweise[st.session_state.ziel_figur][st.session_state.hinweis_index])
antwort = st.text_input("Antwort: ",key ="answer",on_change=check_answer)



#button to get a hint (hinweis index needs to change)
if st.button("I need a hint"):
    st.write("Here is a hint: ", hinweise[st.session_state.ziel_figur][st.session_state.hinweis_index])


