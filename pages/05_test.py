import streamlit as st

st.title("Glowscript 임베드하기 🌐")

st.write("아래에 Glowscript 웹사이트가 임베드되어 있습니다. 로그인하려면 페이지 내에서 직접 로그인하세요.")

# Glowscript 사이트를 iframe으로 임베드
glowscript_url = "https://glowscript.org/"
st.components.v1.iframe(glowscript_url, width=800, height=600)
