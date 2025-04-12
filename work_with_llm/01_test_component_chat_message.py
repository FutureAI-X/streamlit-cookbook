import streamlit as st

with st.chat_message("user"):
    st.write("Hello 👋")
    
with st.chat_message("assistant"):
    st.write("你好，有什么可以帮忙的吗 🤗")