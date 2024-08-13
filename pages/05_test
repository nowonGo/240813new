import streamlit as st

st.title("Glowscript 임베드하기 🌐")

# 사이드바 생성
with st.sidebar:
    # 초기화 버튼 생성
    clear_btn = st.button("초기화")

    # 파일 업로드
    uploaded_file = st.file_uploader("파일업로드", type=["hwp","hwpx"])

    # 모델 선택 메뉴
    selected_model = st.selectbox(
        "LLM 선택", ["gpt-4o", "gpt-4-turbo", "gpt-4o-mini"], index=0
    )

    selected_prompt = st.selectbox(
        "프롬프트 선택",
        ["prompts/pdf-rag.yaml", "prompts/pdf-quiz.yaml"],
        index=0,
    )

    update_btn = st.button("설정 업데이트")

st.write("아래에 Glowscript 웹사이트가 임베드되어 있습니다. 로그인하려면 페이지 내에서 직접 로그인하세요.")

# Glowscript 사이트를 iframe으로 임베드
glowscript_url = "https://glowscript.org/"
st.components.v1.iframe(glowscript_url, width=800, height=600)
