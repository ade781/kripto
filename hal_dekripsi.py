import streamlit as st
import binascii

# Fungsi RC4 untuk dekripsi


def rc4_decrypt(encrypted_text, key):
    # Inisialisasi array S
    S = list(range(256))
    j = 0

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    cipher = []
    i = j = 0

    # Konversi teks terenkripsi dari hexadecimal ke bytes
    encrypted_bytes = binascii.unhexlify(encrypted_text)

    for byte in encrypted_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        cipher.append(k ^ byte)

    # Konversi hasil dekripsi ke string
    return bytes(cipher).decode('utf-8')

# Form input untuk dekripsi


def decryption_form():
    st.subheader("Form Dekripsi")

    # Input teks terenkripsi dari user
    encrypted_text = st.text_area("Masukkan Teks Terenkripsi (hex):")

    # Input key dari user
    key = st.text_input("Masukkan Key untuk dekripsi:")

    if st.button("Dekripsi"):
        if encrypted_text and key:
            try:
                decrypted_text = rc4_decrypt(encrypted_text, key)
                st.success("Teks berhasil didekripsi:")
                st.text_area("Hasil Dekripsi:", value=decrypted_text,
                             height=100, disabled=True)
            except Exception as e:
                st.error(f"plainttext atau pw nya tidak valid ")
        else:
            if not encrypted_text:
                st.error("Teks terenkripsi tidak boleh kosong!")
            if not key:
                st.error("Key tidak boleh kosong!")

# Halaman utama


def main():
    st.title("Dekripsi RC4")

    decryption_form()


if __name__ == "__main__":
    main()
