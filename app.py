import streamlit as st
import openai
import datetime

# ✅ API-Key aus Streamlit Secrets laden
openai.api_key = st.secrets["TOGETHER_API_KEY"]

# ✅ Seitenlayout festlegen
st.set_page_config(
    page_title="LernCoach",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 LernCoach – Dein KI-basierter Lernpartner")

# ✅ Punktesystem starten
if "points" not in st.session_state:
    st.session_state.points = 0

if "streak" not in st.session_state:
    st.session_state.streak = 1

if "last_visit" not in st.session_state:
    st.session_state.last_visit = str(datetime.date.today())
