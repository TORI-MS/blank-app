import streamlit as st
import pandas as pd
from datetime import date

# -------------------------------
# 1. 제목 / 설명
# -------------------------------
st.title("🥘 급식대가리 🥘")
st.write("😻 오늘의 급식을 확인해보세요! 😻")

# -------------------------------
# 2. CSV 데이터 불러오기
# -------------------------------
url = "https://github.com/teacher188-netizen/blank-app/blob/main/meals_data.csv?raw=true"
df = pd.read_csv(url, encoding="cp949")
st.dataframe(df)

# -------------------------------
# 3. 오늘의 메뉴
# -------------------------------
st.write("오늘의 메뉴를 표 형태로 확인할 수 있어요.")

# 오늘 날짜
dt = str(date.today())

# 오늘 날짜 데이터 추출
today_row = df.loc[df["급식일자"] == dt]

if not today_row.empty:
    menu = today_row["요리명"].iloc[0]
    kcal = today_row["칼로리정보(Kcal)"].iloc[0]
    carbo = today_row["탄수화물(g)"].iloc[0]

    # 오늘 급식 보여주기
    st.subheader(f"📅 {dt} 급식")
    st.title(menu)

    # metric 시각화
    st.metric("오늘의 메뉴", menu, border=True)

    # 칼로리 & 탄수화물
    a, b = st.columns(2)
    a.metric("칼로리(Kcal)", kcal, f"{1600-kcal} 남음", border=True)
    b.metric("탄수화물(g)", carbo, border=True)

else:
    st.warning(f"{dt} 날짜의 급식 데이터가 없습니다!")

# -------------------------------
# 4. 데이터 시각화
# -------------------------------
# 지도 시각화
map_data = pd.DataFrame({
    "lat": [37.485475, 37.497539, 37.498014],
    "lon": [126.501083, 126.486135, 126.569858],
    "school": ["인천영종고", "인천공항고", "인천중산고"],
    "students": [923, 662, 1109]
})
st.map(map_data, size="students")

# 선 그래프
st.line_chart(df, x="급식일자", y=["칼로리정보(Kcal)", "탄수화물(g)"])

# 막대 그래프
st.bar_chart(df, x="요일", y="칼로리정보(Kcal)", color="급식일자", horizontal=True)

# -------------------------------
# 5. 입력 기능
# -------------------------------
st.date_input("날짜 선택")
st.selectbox("요일 선택", ["월", "화", "수", "목", "금"])
st.text_input("급식 의견 작성", placeholder="여기에 입력하세요")
st.slider("만족도 (1~5)", 1, 5)
st.radio("추천 점수", ["1", "2", "3", "4", "5"])

# -------------------------------
# 6. 폼 (의견 제출)
# -------------------------------
with st.form("급식 의견 건의함"):
    date_selected = st.date_input("날짜")
    day_selected = st.selectbox("요일", ["월", "화", "수", "목", "금"])
    text_opinion = st.text_input("의견 작성", placeholder="급식에 대한 의견을 입력해주세요")
    slider_val = st.slider("만족도 (1~5)", 1, 5)
    radio_val = st.radio("추천 점수", ["1", "2", "3", "4", "5"])
    submitted = st.form_submit_button("제출")

if submitted:
    st.success("✅ 제출이 완료되었습니다!")
    st.write(f"""
    - 날짜: {date_selected}  
    - 요일: {day_selected}  
    - 의견: {text_opinion}  
    - 만족도: {slider_val}  
    - 추천 점수: {radio_val}  
    """)



#제출 내용 확인
if submitted:
    #제출내용을 웹에 바로 보여줍니다.
    st.write(f"""
            with st.form 안에 들어있는 변수를 중괄호 안에 넣으면 변수와 문자를 함께 출력할 수 있어요.\n
            날짜: {d}
            """)

