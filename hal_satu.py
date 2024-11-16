import streamlit as st
import hal_enkripsi  # Mengimpor file hal_enkripsi.py
import tabel


def main():
    menu_options = {
        "Enkripsi": ":lock: Enkripsi",
        "Dekripsi": ":unlock: Dekripsi",
        "Tabel": ":table: Tabel"
    }

    st.title(":rocket: Selamat Datang di Aplikasi Kripto")
    st.markdown("Silakan pilih menu yang Anda inginkan di samping.")

    # Pilihan menu di sidebar
    selected_menu = st.sidebar.selectbox("Menu", list(menu_options.keys()))

    # Routing menu
    if selected_menu == "Enkripsi":
        hal_enkripsi.main()  # Memanggil fungsi main() dari hal_enkripsi.py
    elif selected_menu == "Dekripsi":
        st.header(menu_options["Dekripsi"])
        st.write("Halaman untuk melakukan dekripsi data.")
    elif selected_menu == "Tabel":
        tabel.main()

    st.sidebar.markdown("---")
    st.sidebar.write("Dibuat dengan :heart: oleh Asisten AI")


if __name__ == "__main__":
    main()
