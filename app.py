import streamlit as st
from openai import OpenAI
import datetime

# API-Key aus secrets.toml laden
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="LernCoach", page_icon="🧠")
st.title("🧠 LernCoach – Dein KI-basierter Lernpartner")

# Punktesystem initialisieren
if "points" not in st.session_state:
    st.session_state.points = 0
    st.session_state.streak = 1
    st.session_state.last_date = str(datetime.date.today())

# Liga-Logik
def get_league(points):
    if points < 200:
        return "🥉 Bronze"
    elif points < 500:
        return "🥈 Silber"
    elif points < 1000:
        return "🥇 Gold"
    elif points < 2000:
        return "💎 Platin"
    else:
        return "👑 Diamant"

# Texteingabe
st.subheader("📚 Lerntext eingeben")
text = st.text_area("Füge hier deinen Lernstoff ein:")

# GPT-Analyse
if st.button("Lernen starten (GPT)"):
    if not text.strip():
        st.warning("Bitte gib einen Text ein.")
    else:
        with st.spinner("GPT analysiert deinen Text..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Du bist ein geduldiger Lerncoach."},
                        {"role": "user", "content": f"""Hier ist ein Lerntext:

{text}

Bitte:
1. Erkläre den Text in einfachen Worten.
2. Stelle 2 Quizfragen mit je 3 Antwortoptionen (markiere die richtige).
3. Gib einen Vorschlag, wie ich den Stoff effektiv lernen kann (inkl. Pausen, Methoden, Wiederholungen).
Antworte im Stil eines motivierenden Coaches."""}
                    ],
                    temperature=0.7,
                    max_tokens=800,
                )
                result = response.choices[0].message.content
                st.markdown("### 🧾 Erklärung & Quiz")
                st.markdown(result)

                # Punkte zählen
                st.session_state.points += 50

                # Streak prüfen
                today = str(datetime.date.today())
                if today != st.session_state.last_date:
                    st.session_state.streak += 1
                    st.session_state.last_date = today

            except Exception as e:
                st.error(f"Fehler bei der GPT-Anfrage: {e}")

# Sidebar: Fortschritt
st.sidebar.title("🎮 Dein Fortschritt")
st.sidebar.markdown(f"**Punkte:** {st.session_state.points}")
st.sidebar.markdown(f"**Streak:** {st.session_state.streak} Tage")
st.sidebar.markdown(f"**Liga:** {get_league(st.session_state.points)}")
st.sidebar.caption("Täglich lernen = mehr Punkte & bessere Liga!")

st.sidebar.markdown("---")
st.sidebar.info("Mehr Features bald: 🏆 Ranglisten, 📅 Lernpläne, 🎯 Prüfungsmodus")
