import streamlit as st



과목 = st.selectbox("과목을 선택하세요",
                    ["확률과 통계",
                     "미분과 적분",
                     "기하와 벡터"])
st.subheader(f"당신이 선택한 과목은 {과목}입니다.")


check1=st.checkbox("짜장면(5000원)")
check2=st.checkbox("짬뽕(70000원)")
check3=st.checkbox("탕수육(15000원)")
sum=0
if check1:
    sum=sum+5000
if check2:
    sum=sum+7000
if check3:
    sum=sum+15000

st.subheader(f"선택한 음식의 가격은 {sum}입니다.")

