"""
构建一个模仿用户输入的机器人：机器人将以相同的消息回应您的输入。
"""
import streamlit as st

st.title("🤖 Mirror Bot")

# 创建一个会话状态变量，用于存储聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Input Something...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"你的输入是：{prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})