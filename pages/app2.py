# 검색창
# 입력창에서 데이터를 받아서
# 해당 문자열이 일치하는 이미지를 화면에 출력해 보세요

# https://docs.streamlit.io/develop/api-reference


# ani_list = ['짱구는못말려', '몬스터','릭앤모티']
# img_list = ['https://i.imgur.com/t2ewhfH.png', 
#             'https://i.imgur.com/ECROFMC.png', 
#             'https://i.imgur.com/MDKQoDc.jpg']
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

import streamlit as st

title = st.text_input("검색하실 애니메이션을 입력하세요", "짱구는못말려")


for ani_ in ani_list:
    if title in ani_:
        # ani_list에서 특정 문자열을 포함한 인덱스
        img_idx = ani_list.index(ani_)
        st.image(img_list[img_idx])
    
if title != '':
    st.image(img_list[img_idx])
