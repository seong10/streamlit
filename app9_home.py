import streamlit as st
from PIL import Image
# 홈에서 할일을 함수로 다 적는중
def run_home() :
    st.subheader('홈 화면입니다.')

    st.text('파일 분리 앱 실습하는중')

    img = Image.open('data2/image_03.jpg')

    st.image(img)