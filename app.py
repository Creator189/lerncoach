import streamlit as st
import requests

st.set_page_config(page_title="LernCoach", page_icon="🧠", layout="centered")

st.markdown("## 🧠 LernCoach – Dein KI-basierter Lernpartner")
st.markdown("### 📚 Lerntext eingeben")
st.markdown("Füge hier deinen Lernstoff ein:")

user_input = st.text_area("", height=150)

if st.button("Lernen starten (GPT)"):
    with st.spinner("KI denkt nach..."):
        try:
            headers = {
                "Authorization": f"Bearer {st.secrets['TOGETHER_API_KEY']}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "mistralai/Mistral-7B-Instruct-v0.2",  # Oder: meta-llama/Llama-3-8b-chat-hf
                "messages": [
                    {"role": "system", "content": "Du bist ein Lerncoach und erklärst verständlich."},
                    {"role": "user", "content": user_input}
                ],
                "max_tokens": 512
            }
            response = requests.post(
                "https://api.together.xyz/v1/chat/completions",
                headers=headers,
                json=data
            )
            assistant_reply = response.json()["choices"][0]["message"]["content"]
            st.success("Antwort von der KI:")
            st.write(assistant_reply)

        except Exception as e:
            st.error(f"Fehler bei der GPT-Anfrage: {e}")
