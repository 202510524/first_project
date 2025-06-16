# main.py

import streamlit as st
import colorsys
from PIL import ImageColor

# 보색 계산 함수
def get_complementary_color(hex_color):
    rgb = ImageColor.getcolor(hex_color, "RGB")
    comp_rgb = tuple(255 - x for x in rgb)
    comp_hex = '#%02x%02x%02x' % comp_rgb
    return comp_hex

# 유사색 계산 함수
def get_analogous_colors(hex_color):
    r, g, b = [x / 255.0 for x in ImageColor.getcolor(hex_color, "RGB")]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    analogous_colors = []
    for shift in [-0.08, 0.08]:  # 약 ±30도
        new_h = (h + shift) % 1.0
        r2, g2, b2 = colorsys.hsv_to_rgb(new_h, s, v)
        analogous_hex = '#%02x%02x%02x' % (int(r2*255), int(g2*255), int(b2*255))
        analogous_colors.append(analogous_hex)

    return analogous_colors

# Streamlit UI
st.set_page_config(page_title="옷 색조합 추천기", page_icon="👕")

st.title("👕 옷 색조합 추천기")
st.markdown("주 색상을 선택하면 어울리는 색조합을 추천해드릴게요!")

# 사용자 색 선택
hex_input = st.color_picker("주 색상을 선택하세요:", "#3498db")

if hex_input:
    st.subheader("🎨 추천 색상 조합")

    comp = get_complementary_color(hex_input)
    analo = get_analogous_colors(hex_input)

    st.markdown(f"**보색 (Complementary Color)**: `{comp}`")
    st.color_picker("보색", comp, label_visibility="collapsed")

    st.markdown("**조화색 (Analogous Colors)**:")
    col1, col2 = st.columns(2)
    with col1:
        st.color_picker("조화색 1", analo[0], label_visibility="collapsed")
    with col2:
        st.color_picker("조화색 2", analo[1], label_visibility="collapsed")
