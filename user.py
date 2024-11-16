# user.py
import streamlit as st
import mysql.connector
from db_connection import connect_db
from hal_satu import main as hal_satu_main


def login_page():
    if 'is_authenticated' in st.session_state and st.session_state.is_authenticated:
        hal_satu_main()
        return

    st.title("User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s",
                       (username, password))
        user = cursor.fetchone()

        if user:
            st.session_state.user_id = user[0]
            st.session_state.is_authenticated = True
            st.session_state.user_type = 'user'
            st.rerun()  # Ini akan me-refresh halaman dan masuk ke hal_satu
        else:
            st.error("Username atau password salah!")

        conn.close()

    if st.button("Kembali"):
        st.session_state.login_type = None
        st.rerun()
