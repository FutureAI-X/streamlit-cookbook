import streamlit as st

prompt = st.chat_input("给AI发消息")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")