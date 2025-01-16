"""
构建一个简单的机器人：从一组预先确定的回复中随机选择一条消息。
"""
import streamlit as st
import time
import random

st.title("🤖 Simple Bot")

# 创建一个会话状态变量，用于存储聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 定义一个生成器函数，用于生成回复
def response_generator():
    random_one = random.choice(
        [
            "你好，我可以帮你做什么？",
            "遇见你真高兴！",
            "今天天气真不错！",
        ]
    )
    for word in random_one:
        yield word + ""
        time.sleep(0.1)

prompt = st.chat_input("Input Something...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})