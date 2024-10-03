# cd "C:\Users\user\OneDrive\デスクトップ"
# streamlit run app.py

from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
st.title("PyGWalker in Streamlit Demo")

@st.cache_resource
def get_pyg_renderer() -> StreamlitRenderer:
    df = pd.read_csv("C:\\Users\\user\\OneDrive\\デスクトップ\\titanic_train.csv")
    return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")
renderer = get_pyg_renderer()

renderer.explorer(default_tab="vis")