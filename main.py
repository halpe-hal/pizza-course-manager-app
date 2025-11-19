# main.py

import streamlit as st
from modules import course_master, course_reservation, course_progress_view



def main():
    st.set_page_config(page_title="コース進行管理システム", layout="wide")

    st.markdown(
    """
    <style>
    /* ページ全体の上部余白を縮める */
    .block-container {
        padding-top: 1rem !important;
    }
    /* タイトル周辺の余白も縮める */
    header[data-testid="stHeader"] {
        height: 0rem !important;
        padding: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    menu = st.sidebar.radio(
        "メニュー",
        [
            "1. コース進行ボード",
            "2. 調理済み一覧",
            "3. 配膳済み一覧",
            # "4. コース予約登録",
            # "5. コースマスタ管理",
        ]
    )

    if menu == "1. コース進行ボード":
        course_progress_view.show_board()
    elif menu == "2. 調理済み一覧":
        course_progress_view.show_cooked_list()
    elif menu == "3. 配膳済み一覧":
        course_progress_view.show_served_list()
    # elif menu == "4. コース予約登録":
    #     course_reservation.show()
    # elif menu == "5. コースマスタ管理":
    #     course_master.show()


if __name__ == "__main__":
    main()
