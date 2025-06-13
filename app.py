import streamlit as st
from openai import OpenAI

# Initialisierung des Clients mit deinem API-Key aus Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit Interface
st.title("🧠 LernCoach – Dein KI-basierter Lernpartner")
st.header("📚 Lerntext eingeben")
lerntext = st.text_area("Füge hier deinen Lernstoff ein:")

if st.button("Lernen starten (GPT)") and lerntext.strip():
    try:
        # Anfrage an OpenAI (Chat API)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher, geduldiger Lerncoach für Schüler:innen."},
                {"role": "user", "content": f"Erkläre folgendes Thema anschaulich und in einfachen Worten: {lerntext}"}
            ],
            temperature=0.7
        )

        st.markdown("### 🧾 Erklärung von GPT:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Fehler bei der GPT-Anfrage: {e}")
