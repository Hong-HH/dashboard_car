import streamlit as st
import pandas as pd
import numpy as np
import os 
import pickle
from eda_app import run_eda_app

def main() :
    st.title('자동차 가격 예측')

    # 사이드바 메뉴
    # eda 는 탐색적 데이터 분석이란 뜻 ml은 머신러닝
    menu = ['Home', 'EDA', 'ML'] 
    choice =st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home' :
        st.write('이 앱은 고객데이터와 자동차 구매 데이터에 대한 내용입니다. 해당 고객의 정보를 입력하면, 얼만정도의 차량을 구매할 수 있는지 예측해 줍니다.')
        st.write('왼쪽의 사이드바에서 선택하세요.')
    elif choice == 'EDA' :
        # 탐색적 데이터 분석이란 우리가 코랩에서 했던것들 같은거인듯
        # run_eda_app을 적으면 알아서 import문을 만들어준다. 난 내가적었는데 ...
        run_eda_app()
    elif choice == 'ML' :
        pass

if __name__ == '__main__' :
    main() 