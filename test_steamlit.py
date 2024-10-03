# cd "C:\Users\user\OneDrive\デスクトップ"
# streamlit run test_steamlit.py

import streamlit as st

st.title('test streamlit')

st.header('ヘッダを表示')

st.subheader('サブヘッダを表示')

st.caption('キャプションを表示')

markdown = """ 
# タイトル
## ヘッダ 
以下の数式にしたがって計算する関数を作成する.  
$$y = 2x$$  
   
Pythonコード
```python
def forward(x):
    return 2 * x
```
"""
st.markdown(markdown)
