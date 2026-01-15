import streamlit as st
import random

st.title("🎯 Zahlenratespiel")

# Spielzustand initialisieren
if "geheimzahl" not in st.session_state:
    st.session_state.geheimzahl = random.randint(1, 100)
    st.session_state.versuche = 0
    st.session_state.beendet = False

st.write("Ich habe mir eine Zahl zwischen **1 und 100** ausgedacht.")

# Eingabe
tipp = st.number_input(
    "Dein Tipp:",
    min_value=1,
    max_value=100,
    step=1
)

# Button zum Raten
if st.button("Raten") and not st.session_state.beendet:
    st.session_state.versuche += 1

    if tipp < st.session_state.geheimzahl:
        st.warning("Zu klein!")
    elif tipp > st.session_state.geheimzahl:
        st.warning("Zu groß!")
    else:
        st.success(
            f"🎉 Richtig! Du hast {st.session_state.versuche} Versuche gebraucht."
        )
        st.session_state.beendet = True

# Neustart-Button
if st.session_state.beendet:
    if st.button("🔄 Neues Spiel"):
        st.session_state.geheimzahl = random.randint(1, 100)
        st.session_state.versuche = 0
        st.session_state.beendet = False
        st.experimental_rerun()
