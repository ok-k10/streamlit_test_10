<<<<<<< HEAD
# cd "C:\streamlit_test\streamlit_test_10"
# streamlit run FDH_for_BS.py

# C:\streamlit_test\streamlit_test_10\FDH_for_BS.py 

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
st.title('Flexible Data Handling for Business Support')   

def next_button():
    st.button('proceed_to_next')
    st.sesion_state.page += 1 # 次のページへ移動 

def render_status_bar(current_stage):
    stages = ['データアップロード','アップデートデータの確認','抽出・集計条件編集','グラフ表示']
    colors = ["#00bfff", "#00bfff", "#00bfff", "#00bfff"] #初期色設定(灰色)
    colors[current_stage - 1] = "#0000cd" # 現在のステータスを赤色に変更


    # st.markdown('<hr>', unsafe_allow_html=True)

    html_content = "<div style='width: 100%; display: flex; justify-content: center; margin-bottom: 20px;'>"
    for i, stage in enumerate(stages):
        color = colors[i]
        if i > 0:
            html_content += f"<span style='display:inline-block; margin-center:5px; margin-center:5px;'>→</span>"
        html_content += f"<span style='display:inline-block; width:250px; height:25px; background-color:{color}; color: white; text-align:center; line-height:25px; border-radius:5px;'>{stage}</span>"
    html_content += "</div>"    
    st.markdown(html_content, unsafe_allow_html=True)

    # st.markdown("<hr>", unsafe_allow_html=True)

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 1
    
    current_page = st.session_state.page
    # ページナビゲーションを表示
    max_pages = 4  # 最大ページ数
    render_status_bar(current_page)

    page_functions = [page_one, page_two, page_three, page_four]
    page_functions[current_page - 1]()  # 現在のページを表示

    # ページコントロール
    col1, col2 = st.columns(2)
    if current_page > 1:
        with col1:
            if st.button('戻る'):
                st.session_state["page"] -= 1  # 前のページへ
    if current_page < max_pages:
        with col2:
            if st.button('次へ'):
                st.session_state["page"] += 1  # 次のページへ

def page_one():
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

def page_two():
    st.write("This is the data verification step.")


def page_three():
    st.write("This is the conditions editing step.")

def page_four():
    st.write("This is the graph display step.")

if __name__ == "__main__":
    main()
=======
# cd "C:\streamlit_test\streamlit_test_10"
# streamlit run FDH_for_BS.py

# C:\streamlit_test\streamlit_test_10\FDH_for_BS.py 

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

>>>>>>> 0645e6fcc304ade499ca6e1bd96e30e4b127c646
