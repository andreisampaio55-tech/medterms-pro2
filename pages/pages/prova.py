import streamlit as st
import random
from data import termos

st.title("🧪 Prova")

t = random.choice(termos)

st.write(f"O que significa: {t['termo']}?")

resposta = st.text_input("Resposta")

if st.button("Ver resposta"):
    st.write(t["significado"])
