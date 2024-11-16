import streamlit as st
import hal_enkripsi
import hal_dekripsi
import tabel


def main():
    # Menampilkan nama pengguna yang sedang login
    st.title(
        f":rocket: Selamat Datang di Aplikasi Kripto, {st.session_state.username}")

    st.markdown("Silakan pilih menu yang Anda inginkan di samping.")

    menu_options = {
        "Enkripsi": ":lock: Enkripsi",
        "Dekripsi": ":unlock: Dekripsi",
        "Tabel": ":table: Tabel"
    }

    # Pilihan menu di sidebar
    selected_menu = st.sidebar.selectbox("Menu", list(menu_options.keys()))

    # Routing menu
    if selected_menu == "Enkripsi":
        hal_enkripsi.main()  # Memanggil fungsi main() dari hal_enkripsi.py
    elif selected_menu == "Dekripsi":
        hal_dekripsi.main()
    elif selected_menu == "Tabel":
        tabel.main()

    st.sidebar.markdown("---")
    st.sidebar.write("Dibuat dengan sepenuh hati hihihihihi :heart:")
