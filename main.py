import streamlit as st
import random

# 🎨 페이지 기본 설정
st.set_page_config(page_title="가위✌️ 바위✊ 보🖐️ 게임", page_icon="🎮", layout="centered")

# 🌟 타이틀 및 설명
st.markdown("""
# 🎮 **가위✌️ 바위✊ 보🖐️ 챌린지!**
## 🤖 나와 대결해볼래? 운을 시험해보자!
""", unsafe_allow_html=True)

# 🔧 옵션 설정
choices = {
    "✌️ 가위": "scissors",
    "✊ 바위": "rock",
    "🖐️ 보": "paper"
}

# 🎨 사용자 입력
user_choice = st.radio("👇 선택하세요!", list(choices.keys()), horizontal=True)

if st.button("🎯 대결 시작!"):
    # 💻 컴퓨터의 선택
    comp_choice = random.choice(list(choices.keys()))
    
    # 🎲 결과 판별
    result = ""
    if user_choice == comp_choice:
        result = "🤝 무승부!"
    elif (user_choice == "✌️ 가위" and comp_choice == "🖐️ 보") or \
         (user_choice == "✊ 바위" and comp_choice == "✌️ 가위") or \
         (user_choice == "🖐️ 보" and comp_choice == "✊ 바위"):
        result = "🎉 승리! 너가 이겼어!"
    else:
        result = "😢 패배! 내가 이겼지롱~"

    # 🎆 결과 출력
    st.markdown(f"""
    ---
    ### 🙋‍♂️ 당신의 선택: {user_choice}  
    ### 🤖 컴퓨터의 선택: {comp_choice}
    ---
    ## 🏆 **{result}**
    """, unsafe_allow_html=True)

    st.balloons()
