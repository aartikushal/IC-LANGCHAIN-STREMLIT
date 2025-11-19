if st.button("Send"):
    if user_msg.strip():
        with st.spinner("Generating response..."):
            reply = conversation_chain.predict(input=user_msg)

        st.session_state.chat_history.append(("You", user_msg))
        st.session_state.chat_history.append(("Bot", reply))

        st.rerun()


# Reset button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
