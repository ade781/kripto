import streamlit as st
import mysql.connector


# Menambahkan header dengan judul dan gambar


def header():
    st.markdown("""
    <style>
        .header {
            font-size: 32px;
            font-weight: bold;
            color: #4b6e84;
            text-align: center;
            margin-bottom: 20px;
        }
        .header span {
            color: #1f78d1;
        }
    </style>
    <div class="header">
        Kriptografi <span>Login</span> Page
    </div>
    """, unsafe_allow_html=True)

# Membuat dua kolom untuk tombol login dengan desain yang lebih rapi


def home_page():
    header()  # Menampilkan header

    st.write("Pilih jenis login untuk melanjutkan:")

    # Membuat dua kolom untuk tombol login dengan styling
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login as User", key="user_button", help="Login as regular user", use_container_width=True):
            st.session_state.login_type = "User"
    with col2:
        if st.button("Login as Admin", key="admin_button", help="Login as administrator", use_container_width=True):
            st.session_state.login_type = "Admin"

# Halaman login untuk user


def user_login_page():
    import user  # Mengimpor file user.py
    user.login_page()

# Halaman login untuk admin


def admin_login_page():
    import admin  # Mengimpor file admin.py
    admin.login_page()


# Main program
if __name__ == "__main__":
    if "login_type" not in st.session_state:
        # Inisialisasi state awal jika belum ada
        st.session_state.login_type = None

    # Menentukan halaman berdasarkan login_type
    if st.session_state.login_type == "User":
        user_login_page()
    elif st.session_state.login_type == "Admin":
        admin_login_page()
    else:
        home_page()
