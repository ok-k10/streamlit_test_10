# cd "C:\streamlit_test\streamlit_test_10"
# streamlit run test_app.py

# ダッシュボード作成用のStreamlitタブ
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go

# import plotly.figure_factory as ff
# import plotly.graph_objects as go

### ###
## dfのDataFrameを簡易表示

# import streamlit as st
# import pandas as pd

# # ダミーデータ作成
# df = pd.DataFrame({
#     'name': ['Alice', 'Bob'],
#     'age': [25, 30],
#     'gender': ['famale', 'male']
# })

# # DataFrameを表示
# st.write(df)

# # st.dataframe()でも表示可能
# st.dataframe(df)

### ###
## ファイルアップローダー
# import streamlit as st

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     st.write(uploaded_file)

## ボタンの作成 st.button
# if st.button('Say hello'):
#     st.write('Hello World!') 

## チェックボックスの作成
# if st.checkbox('Show/Hide'):
#     st.write('Some text') #チェックするBOX

# # ラジオボタンの表示
# option = st.radio(
#     'Which number do you like best?', 
#     ['1', '2', '3'] #ラジオボタンの値
# )

# # セレクトボックスの表示
# option = st.selectbox(
#     'Which number do you like best?', 
#     ['1', '2', '3'] # セレクトする値
# )


# # マルチセレクトボックスの表示
# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Red', 'Yellow' ,'Blue'], #選択できるcolor
#     default=['Red'] #デフォルトの設定
# )

# # スライダーの表示
# value = st.slider('Select a value', 0, 100, 50) # min, max, default
# # テキスト入力ボックス
# text_input = st.text_input('Input', 'Input some text here.')
# # テキストエリア
# text_area = st.text_area('Text Area', 'Input some text here.')

# import time
# # ボタンの設定を行う
# if st.button('start'):
#     with st.spinner('processiong...'):
#         time.sleep(3) #ライブラリ time
#         st.write('end!')

# # sidebarの選択肢を定義する
# options = ['Option 1', 'Option2', 'Option3']
# choice = st.sidebar.selectbox('Select an option', options)

# # Mainコンテンツの表示を変える
# if choice == 'Option 1':
#     st.write('You selected Option 1')
# elif choice == 'Option 2':
#     st.write('You selected Option 2')
# else:
#     st.write('You selected Option 3')

# # increment の追加
# st.title('Counter Example using Callbacks')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter():
#     st.session_state.count += 1

# st.button('Incre\ment', on_click=increment_counter)
# st.write('Count = ', st.session_state.count)

# # ダミーデータの作成
# df = pd.DataFrame({
#     'name': ['Alice', 'Bob'],
#     'age': [25, 30],
#     'gender': ['female', 'male']
# })

# # 2列のカラムを作成
# col1, col2 = st.columns(2)

# # col1にテキストを表示
# with col1:
#     st.header("Column 1")
#     st.write("This is column 1.")

# # col2にDataFrameを表示
# with col2:
#     st.header("Column 2")
#     # DataFrameを表示
#     st.write(df)

## グラフをボタン押下&表示
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# # Warningの非表示
# # st.set_option('deprecation.showPyplotGlobalUse', False) 

# # グラフを描画する
# def plot_graph():
#     x = np.linspace(0, 10, 100)
#     y = np.sin(x)
#     plt.plot(x, y)
#     st.pyplot()

# # グラフを表示するボタンを表示する
# if st.button('Plot graph'):
#     plot_graph()

# # グラフ押下、Hello,Worldの表示
# st.text_input('Message', key='text_input') #(A)

# def change_value():
#     st.session_state['text_input'] = 'Hello, World' #(B)

# st.button('Click', on_click=change_value) #(C)

# # ※ボタン押下時に例外が発生する　→　エラーの例
# st.text_input("Message", key="text_input")


# if st.button("Click"):
#     st.session_state["text_input"] = "Hello, World"

# # clickで文字変更
# key = 'text_input'

# def change_value():
#     st.session_state[key] = 'World'

# if key not in st.session_state:
#     st.session_state[key] = 'Hello'

# st.text_input('Message', key=key)
# st.button('Click', on_click=change_value)

# # アプリのページ切り替えの流れとページ再読み込みについて
# def main():
#     # １ページ目表示
#     st.sidebar.title("test_streamlit")
#     st.markdown("## ボタンでページを変えましょう")
#     st.sidebar.button("ページ切り替えボタン", on_click=change_page)

# def change_page():
#     # ページ切り替えボタンコールバック
#     st.session_state["page_control"]=1

# def next_page():
#     # ２ページ目表示
#     st.sidebar.title("ページが切り替わりました")
#     st.markdown("## 次のページです")

# # 状態保持する変数を作成して確認
# if ("page_control" in st.session_state and
#    st.session_state["page_control"] == 1):
#     next_page()
# else:
#     st.session_state["page_control"] = 0
#     main()


# # いくつかのデータを読み込む
# data = pd.read_csv("C:\streamlit_test\streamlit_test_10\monitor_tv_log.csv")

# st.title('My Data Visualization Application')
 
# # タブを作成する
# tab_titles = ['棒グラフ', '散布図', 'ヒートマップ']
# tabs = st.tabs(tab_titles)
 
# # 各タブにコンテンツを追加する
# with tabs[0]:
#     st.header('棒グラフ')
#     st.bar_chart(data)
 
# with tabs[1]:
#     st.header('散布図')
#     fig, ax = plt.subplots()
#     ax.scatter(data['monitor'], data['end_time'])
#     st.pyplot(fig)

df = pd.read_csv('data/data_sample.csv')
vars_cat = [var for var in df.columns if var.startswith('cat')]
vars_cont = [var for var in df.columns if var.startswith('cont')]

st.set_page_config(layout="wide")


