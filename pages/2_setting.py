import streamlit as st

name = st.text_input("Enter your username")
if st.button("Set name"):
    st.write(name)
    st.session_state['username'] = name
    