import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objs as go

# 🎨 페이지 설정
st.set_page_config(page_title="📈 함수 그래프 생성기", page_icon="📐", layout="centered")

# 🎉 타이틀
st.title("📈 수학 함수 그래프 자동 생성기")
st.markdown("함수를 입력하면 자동으로 그래프를 생성해드려요! ✨<br>예: `sin(x)`, `x**2 + 2*x - 1`, `exp(-x**2)`", unsafe_allow_html=True)

# ✍️ 사용자 입력
user_input = st.text_input("함수를 입력하세요 (변수는 x)", value="sin(x)")

# 🔧 범위 설정
col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("X 최소값", value=-10)
with col2:
    x_max = st.number_input("X 최대값", value=10)

# 📈 그래프 생성 버튼
if st.button("📌 그래프 그리기"):

    # ✅ 안전한 수식 파싱
    x = sp.Symbol('x')
    try:
        parsed_expr = sp.sympify(user_input)
        f_lambdified = sp.lambdify(x, parsed_expr, modules=["numpy"])

        # 📊 데이터 생성
        x_vals = np.linspace(x_min, x_max, 1000)
        y_vals = f_lambdified(x_vals)

        # 🖼️ Plotly를 사용한 그래프
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode="lines",
            name=f"y = {user_input}",
            line=dict(color='royalblue', width=2)
        ))

        # 🎯 좌표축 중심선 추가
        fig.add_shape(type="line", x0=x_min, x1=x_max, y0=0, y1=0,
                      line=dict(color="gray", width=1, dash="dot"))
        fig.add_shape(type="line", x0=0, x1=0, y0=min(y_vals), y1=max(y_vals),
                      line=dict(color="gray", width=1, dash="dot"))

        # 📏 레이아웃 설정
        fig.update_layout(
            title=f"📐 y = {user_input} 그래프",
            xaxis_title="x",
            yaxis_title="y",
            showlegend=True,
            width=800,
            height=500,
            template="plotly_white"
        )

        # 🖼️ 그래프 출력
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"⚠️ 오류 발생: {e}")

