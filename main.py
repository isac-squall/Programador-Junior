import streamlit as st
import random

st.title("Jogo da Adivinhação")

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.tentativas = 0

palpite = st.number_input("Digite seu palpite:", min_value=1, max_value=100, step=1)

if st.button("Enviar palpite"):
    st.session_state.tentativas += 1
    if palpite < st.session_state.numero_secreto:
        st.warning("Muito baixo!")
    elif palpite > st.session_state.numero_secreto:
        st.warning("Muito alto!")
    else:
        st.success(f"Parabéns! Você acertou em {st.session_state.tentativas} tentativas.")
        if st.button("Jogar novamente"):
            st.session_state.numero_secreto = random.randint(1, 100)
            st.session_state.tentativas = 0