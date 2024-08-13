import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

st.title("Glowscript 임베드하기 🌐")

st.write("아래에 Glowscript 웹사이트가 임베드되어 있습니다. 로그인하려면 페이지 내에서 직접 로그인하세요.")

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




# Google Sheets API 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)
client = gspread.authorize(creds)

# Google 스프레드시트 열기
spreadsheet = client.open("스프레드시트 이름")
sheet = spreadsheet.sheet1  # 첫 번째 시트를 선택합니다.

# 데이터 가져오기
data = sheet.get_all_records()

# Streamlit UI 구성
st.title("학생 제출 URL 목록")

# 데이터 출력
if data:
    st.write("제출된 학생 목록:")
    for entry in data:
        학번 = entry.get("학번")
        이름 = entry.get("이름")
        url = entry.get("url")

        # 학생 정보 출력
        st.write(f"학번: {학번}, 이름: {이름}")
        st.markdown(f"[제출한 링크]({url})")
else:
    st.write("제출된 데이터가 없습니다.")

