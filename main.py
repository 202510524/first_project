# color_matcher_app.py
import streamlit as st
import random

# 색상 조합 데이터 예시
color_combinations = {
    "red": ["white", "black", "denim blue", "beige"],
    "blue": ["white", "gray", "camel", "navy"],
    "green": ["brown", "white", "beige", "khaki"],
    "black": ["white", "gray", "red", "beige"],
    "white": ["black", "blue", "green", "camel"],
    "beige": ["white", "brown", "olive", "black"],
}

# Streamlit 앱 시작
st.title("👕 옷 색조합 추천기")
st.write("주요 색상을 선택하면 어울리는 색 조합을 추천해드립니다!")

# 사용자 입력 받기
selected_color = st.selectbox("상의 색상을 선택하세요:", list(color_combinations.keys()))

# 색조합 추천
if selected_color:
    recommended_colors = color_combinations.get(selected_color, [])
    st.subheader("추천 색조합:")
    for color in recommended_colors:
        st.markdown(f"- {color.capitalize()}")
    
    # 시각적 표시
    st.subheader("색상 미리보기")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**선택한 색상:** {selected_color}")
        st.markdown(
            f"<div style='background-color: {selected_color}; width:100px; height:100px;'></div>",
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown("**추천 색상 중 하나:**")
        preview_color = random.choice(recommended_colors)
        st.markdown(f"<div style='background-color: {preview_color}; width:100px; height:100px;'></div>",
                    unsafe_allow_html=True)

