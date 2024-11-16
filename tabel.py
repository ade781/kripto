import streamlit as st
import mysql.connector
import pandas as pd
from db_connection import connect_db


def main():
    st.title("Tabel Data Enkripsi")

    # Cek login
    if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
        st.error("Silakan login terlebih dahulu!")
        return

    # Cek ID user login
    if 'user_id' in st.session_state:
        user_id = st.session_state.user_id

        # Ambil data dari database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, user, isi FROM text WHERE user = %s", (user_id,))
        data = cursor.fetchall()
        conn.close()

        if not data:
            st.info("Tidak ada data untuk ditampilkan.")
            return

        # Tambahkan nomor secara otomatis untuk setiap baris data
        table_data = [{"Nomor": i + 1, "ID": row[0], "ID_User": row[1],
                       "Isi": row[2]} for i, row in enumerate(data)]
        df = pd.DataFrame(table_data)

        # Atur kolom "Isi" agar teks panjang otomatis turun ke baris berikutnya
        # Ubah nilai sesuai kebutuhan
        pd.set_option('display.max_colwidth', 50)
        df["Isi"] = df["Isi"].apply(lambda x: '\n'.join(
            [x[i:i+50] for i in range(0, len(x), 50)]))  # Potong teks per 50 karakter

        # Gunakan st.write agar tidak ada kolom indeks bawaan
        st.write(df.to_html(index=False), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
