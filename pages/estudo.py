import streamlit as st
from data import termos

st.title("📚 Estudo")

for t in termos:
    st.write(f"### {t['termo']}")
    st.write(t["significado"])
    st.write(t["exemplo"])
