# cd "C:\Users\user\OneDrive\デスクトップ"
# streamlit run calculation.py
import streamlit as st

default = 0 # デフォルト値を設定
st.title('Calculation Example')
if 'count' not in st.session_state:
	st.session_state.count = default  #countがsession_stateに追加されていない場合，0で初期化

# increment = st.button('Increment')
# decrement = st.button('Decrement')
# multiplication = st.button('Multiply')
# division = st.button('Division')
# reset = st.button('Reset')

if st.button('Increment'):
    st.session_state.count += 1 #値を増やす
if st.button('Decrement'):
    st.session_state.count -= 1 #値を減らす
if st.button('Multiply'):
    st.session_state.count *= 2 #2倍にする
if st.button('Division'):
    st.session_state.count /= 2 #2で割る
if st.button('Reset'):
    st.session_state.count = default #リセット

st.write('Count = ' + str(st.session_state.count))