# count.py
import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
	st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化

increment = st.button('Increment')
decrement = st.button('Decrement')
multiplication = st.button('Multiply')
division = st.button('Division')
reset = st.button('Reset')

if increment:
    st.session_state.count += 1 #値を増やす
if decrement:
    st.session_state.count -= 1 #値を減らす
if multiplication:
    st.session_state.count *= 2 #2倍にする
if division:
    st.session_state.count /= 2 #2で割る
if reset:
    st.session_state.count = 0 #リセット
st.write('Count = ' + str(st.session_state.count))