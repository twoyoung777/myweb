import streamlit as st
st.sidebar.selectbox("MENU", ["로그인","회원가입"])

db_id="test"
db_pw="123"

if menu=="로그인":
    st.title("")
    id=st.text_input("아이디", placeholder="아이디를 입력하세요.")
    pw=st.text_input("패스워드", type="password")
    login=st.button("로그인")

    if login:
        if db_id==id and db_pw==pw:
            st.success("로그인 성공")
            st.balloons()
    else:
        st.error("로그인 실패")
elif menu=="회원가입":


# 과목 = st.selectbox("과목을 선택하세요",
#                     ["확률과 통계",
#                      "미분과 적분",
#                      "기하와 벡터"])
# st.subheader(f"당신이 선택한 과목은 {과목}입니다.")


# check1=st.checkbox("짜장면(5000원)")
# check2=st.checkbox("짬뽕(70000원)")
# check3=st.checkbox("탕수육(15000원)")
# sum=0
# if check1:
#     sum=sum+5000
# if check2:
#     sum=sum+7000
# if check3:
#     sum=sum+15000

# st.subheader(f"선택한 음식의 가격은 {sum}입니다.")
