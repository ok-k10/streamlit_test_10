# cd "C:\streamlit_test\streamlit_test_10"
# streamlit run FDH_for_BS.py

import streamlit as st
import pandas as pd
import pygwalker as pyg
from sklearn import datasets
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd

st.set_page_config(
    page_title='Flexible Data Handling for Business Support',
    layout='wide'
)

# タイトルを追加
st.title('Flexible Data Handling for Business Support')

uploaded_file_1 = st.file_uploader(label='データファイル1をアップロードして下さい。', type=['csv', 'tsv'], accept_multiple_files=False, key="file_uploader1")
uploaded_file_2 = st.file_uploader(label='データファイル2をアップロードして下さい。', type=['csv', 'tsv'], accept_multiple_files=False, key="file_uploader2")


if st.button('display'):
    if uploaded_file_1:
        #  を読み込み
        df1 = pd.read_csv(uploaded_file_1, comment='1')
        st.write(df1)
    else:
        st.error('データファイル1がアップロードされてません')

    if uploaded_file_2:
        df2 = pd.read_csv(uploaded_file_2, comment='2')
        st.write(df2)
    else:
        st.error('データファイル2がアップロードされてません')