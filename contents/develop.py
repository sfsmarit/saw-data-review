import streamlit as st
import os
import socket

nl = "  "

st.set_page_config("SAW Data Review", page_icon=":star:", layout="wide")


st.subheader("開発")

st.markdown(
    f"""
    :warning: これは SAW Data Review の検証用モックアップです

    ---

    #### 概要
    """
)

st.image("img/sawdr_architecture.png")

st.markdown(
    f"""
    実装済み
    - 工程データをsawdrデータベースに保存する (sfsaw を流用)
    - データベースから工程データを読み込んで表示する (sfsaw を流用)
    
    未実装
    - データサーバから S-parameter を読み込んで表示する
    
    ---
    
    #### ソースコード
    https://github.com/sfsmarit/saw-data-review
    
    - 一部Git管理外のファイルもあります。詳細については担当者に問い合わせてください
    - sfsawを叩いているだけなので public リポジトリにしています。機密情報を直接コードに書き込む場合は private リポジトリにしてください
    - 参考 [sfsaw](https://github.com/sfsmarit/sfsaw)
    

    ---
    
    #### データベース
    https://uw-v-appstm-000.nb-engr.skyworksinc.com/db-editor/

    |||
    |--|--|
    | Host | uw-v-appstm-000.nb-engr.skyworksinc.com |
    | Port | 3306 |
    | Database | sawdr |
    | User | sawdrread |
    | Password | readonly |
    > このアカウントは読み取り専用です{nl}
    > 全権限が必要な場合は担当者に問い合わせてください
    
    ---
    
    #### デプロイ
    ホスト
    ```bash
    {socket.gethostname()}
    ```
    
    ディレクトリ
    ```bash
    {os.getcwd()}
    ```
    
    更新、起動、確認、停止
    ```bash
    git pull
    nohup ../streamlit/bin/streamlit run sawdr.py &
    pgrep -a streamlit
    kill <pid>
    ```

    """
)
