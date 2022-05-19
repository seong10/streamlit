# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러리인, 스트림릿은,
# main 함수가 있어야 한다.
# 이것은 이렇게 해야 만들어지게 만든 틀 이다 이해가 아니라 외울부분

def main() :
    st.title('안녕하세요. 웹 대시보드 프로젝트')
    st.title('Hello')

if __name__ == '__main__' :
    main()

# 터미넬에서 +를 누르고 Command prompt 프롬프트로 해야
# 아나콘다가 깔린 프롬프트이다
# cmd 터미널에 streamlit run (파일이름.py)