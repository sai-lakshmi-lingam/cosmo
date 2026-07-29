import streamlit as st

with st.sidebar:

    st.title("✨ Cosmo")

    st.write("Knowledge Base")

    st.write("💄 Makeup")

    st.write("🧴 Skincare")

    st.write("👗 Fashion")

    st.write("🎬 Pop Culture")

    st.write("📺 TV & Movies")

    if st.button("Clear Conversation"):
        st.session_state.history = []
        st.rerun()

from chatbot import ask_cosmo

st.title("✨ Cosmo")

st.markdown("""
Welcome to **Cosmo**! ✨

Ask me about:

- 💄 Makeup
- 🧴 Skincare
- 👗 Fashion
- 🌟 Celebrities
- 📺 TV Shows
- 🎬 Movies
- 🎵 Pop Culture
""")

if "history" not in st.session_state:
    st.session_state.history = []

# Display previous messages
for message in st.session_state.history:

    if message.startswith("User:"):

        with st.chat_message("user"):
            st.write(message.replace("User: ", ""))

    elif message.startswith("Cosmo:"):

        with st.chat_message("assistant"):
            st.write(message.replace("Cosmo: ", ""))

question = st.chat_input(
    "Ask Cosmo something..."
)

if question:

    st.session_state.history.append(
        f"User: {question}"
    )

    with st.chat_message("user"):
        st.write(question)

    answer = ask_cosmo(
        question,
        st.session_state.history
    )

    st.session_state.history.append(
        f"Cosmo: {answer}"
    )

    with st.chat_message("assistant"):
        st.write(answer)