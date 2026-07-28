import streamlit as st

from chatbot import ask_cosmo

st.title("✨ Cosmo")

st.write(
    "Your personal beauty, fashion, and pop culture assistant."
)

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input(
    "Ask Cosmo something:"
)

if st.button("Ask Cosmo"):

    if question:

        st.session_state.history.append(
            f"User: {question}"
        )

        answer = ask_cosmo(
            question,
            st.session_state.history
        )

        st.session_state.history.append(
            f"Cosmo: {answer}"
        )

        st.write(answer)