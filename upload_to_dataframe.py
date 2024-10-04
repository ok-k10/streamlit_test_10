import streamlit as st
import pandas as pd

# CSVアップロードされたファイルをデータフレームに読み込む
uploaded_file = st.file_uploader('CSVファイルをアップロードしてください。 ※1行目をヘッダーと認識します。', type=['CSV'])

# アップロードされたファイルをデータフレーちゃムに読み込む
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
