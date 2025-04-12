import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://api-inference.modelscope.cn/v1/", 
    api_key="954a12f1-1c3f-4756-b133-248866adfd7b"
)
def generate_response(messages):
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=messages,
        stream=True
    )
    return response

st.title("AI 助手")

# 初始化消息列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示消息列表（应用启动时）
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 1.获取用户输入，并添加到消息列表中 2.复制用户输入作为助手回复
prompt = st.chat_input("给AI发消息")
if prompt:
    # 打印用户输入
    with st.chat_message("user"):
        st.markdown(prompt)
    # 将用户输入添加到消息列表中
    st.session_state.messages.append({"role": "user", "content": prompt})

    stream = generate_response(st.session_state.messages)
    # 打印助手回复
    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    # 将助手回复添加到消息列表中
    st.session_state.messages.append({"role": "assistant", "content": response})