import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# API KEY 정보로드
# load_dotenv()  # 필요에 따라 환경 변수를 로드합니다.
openai_api_key = "your-openai-api-key"  # 여기서 API 키를 설정하거나 환경변수를 사용할 수 있습니다.

st.title("ChatGPT와 대화하기 💬")

# 처음 1번만 실행하기 위한 코드
if "messages" not in st.session_state:
    # 대화기록을 저장하기 위한 용도로 생성합니다.
    st.session_state["messages"] = []

# 사이드바 생성
with st.sidebar:
    # 초기화 버튼 생성
    clear_btn = st.button("초기화")
    
    # 모델 선택 메뉴
    selected_model = st.selectbox(
        "LLM 선택", ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"], index=0
    )
    
    update_btn = st.button("설정 업데이트")

# 이전 대화를 출력
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)

# 새로운 메시지를 추가
def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))

# 초기화 버튼이 눌리면...
if clear_btn:
    st.session_state["messages"] = []

if update_btn:
    st.success("설정이 업데이트되었습니다!")

# 이전 대화 기록 출력
print_messages()

# 사용자의 입력
user_input = st.chat_input("궁금한 내용을 물어보세요!")

# 경고 메시지를 띄우기 위한 빈 영역
warning_msg = st.empty()

# 만약에 사용자 입력이 들어오면...
if user_input:
    # OpenAI LLM 생성
    llm = ChatOpenAI(model_name=selected_model, temperature=0.7, openai_api_key=openai_api_key)

    # 사용자의 입력
    st.chat_message("user").write(user_input)
    
    # LLM에 사용자 질문 전달하고 응답 받기
    response = llm(user_input)

    # 응답을 화면에 출력
    with st.chat_message("assistant"):
        st.markdown(response.content)

    # 대화기록을 저장합니다.
    add_message("user", user_input)
    add_message("assistant", response.content)
