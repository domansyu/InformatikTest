import streamlit as st

st.set_page_config(page_title="Notenrechner", layout="wide")

st.title("📘 Notenrechner – Mehrere Fächer")

st.markdown(
    """
**Gewichtung:**
- 📝 3 Klassenarbeiten: **40 %**
- 🗣️ Mündliche Note: **50 %**
- 🎤 Referat: **10 %**
"""
)

# Session State
if "faecher" not in st.session_state:
    st.session_state.faecher = []

if "fach_counter" not in st.session_state:
    st.session_state.fach_counter = 0

# Button oben
col_add, col_space = st.columns([1, 5])
with col_add:
    if st.button("➕ Fach hinzufügen"):
        st.session_state.faecher.append(st.session_state.fach_counter)
        st.session_state.fach_counter += 1

st.divider()

ergebnisse = {}

# Fächer anzeigen
for i in st.session_state.faecher:
    with st.container(border=True):
        st.subheader(f"📚 Fach {i + 1}")

        fachname = st.text_input(
            "Fachname",
            placeholder="z. B. Mathematik",
            key=f"name_{i}"
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            k1 = st.number_input("Klassenarbeit 1", 0.0, 15.0, 0.0, 0.1, key=f"k1_{i}")
        with col2:
            k2 = st.number_input("Klassenarbeit 2", 0.0, 15.0, 0.0, 0.1, key=f"k2_{i}")
        with col3:
            k3 = st.number_input("Klassenarbeit 3", 0.0, 15.0, 0.0, 0.1, key=f"k3_{i}")

        col4, col5 = st.columns(2)
        with col4:
            muendlich = st.number_input("Mündliche Note", 0.0, 15.0, 0.0, 0.1, key=f"m_{i}")
        with col5:
            referat = st.number_input("Referat", 0.0, 15.0, 0.0, 0.1, key=f"r_{i}")

        schnitt_klassenarbeiten = (k1 + k2 + k3) / 3
        endnote = (
            schnitt_klassenarbeiten * 0.40 +
            muendlich * 0.50 +
            referat * 0.10
        )

        ergebnisse[fachname if fachname else f"Fach {i + 1}"] = endnote

        st.markdown(f"**➡️ Aktueller Durchschnitt:** `{endnote:.2f}`")

# Ergebnisbereich
if st.session_state.faecher:
    st.divider()
    st.header("📊 Übersicht")

    cols = st.columns(len(ergebnisse))
    for col, (fach, note) in zip(cols, ergebnisse.items()):
        col.metric(label=fach, value=f"{note:.2f}")
