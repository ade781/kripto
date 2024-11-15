import streamlit as st
import base64
import json
from datetime import datetime

# Configure page settings
st.set_page_config(
    page_title="kripto cok",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_css():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            background-color: #f8f9fa;
        }
        
        .stButton>button {
            width: 100%;
            height: 3rem;
            margin: 0.5rem 0;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: #1e3d59;
            text-align: center;
            padding: 1.5rem 0;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 2rem auto;
            max-width: 800px;
        }
        
        .stTextInput>div>div>input {
            border-radius: 5px;
            padding: 0.5rem;
            border: 1px solid #ddd;
        }
        
        .info-box {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
            border-left: 5px solid #2196f3;
        }
        
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            text-align: center;
            padding: 1rem;
            font-size: 0.8rem;
            color: #666;
        }
        </style>
    """, unsafe_allow_html=True)

def home_page():
    load_css()
    
    # Header
    st.title("🔐 welkom fika sayangg")
    
    # Main container
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
  
        # Login columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3 style='text-align: center;'>Pacar</h3>", unsafe_allow_html=True)
            if st.button("sebagai pacar", key="user_btn"):
                st.session_state.login_type = "User"
                st.rerun()
                
        with col2:
            st.markdown("<h3 style='text-align: center;'>teman </h3>", unsafe_allow_html=True)
            if st.button("sebagai musuh", key="admin_btn"):
                st.session_state.login_type = "Admin"
                st.rerun()
        
        # Features section
        st.markdown("""
            <div style='margin-top: 2rem;'>
                <h4>Fitur Utama:</h4>
                <ul>
                    <li>Enkripsi dan Dekripsi File</li>
                    <li>Manajemen Kunci Kriptografi</li>
                    <li>Tanda Tangan Digital</li>
                    <li>Verifikasi Integritas Data</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

def user_login_page():
    load_css()
    st.title("🔒 User Login Portal")
    
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Login form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if username and password:
                # Add your authentication logic here
                st.success("Login berhasil!")
            else:
                st.error("Mohon isi username dan password!")
        
        if st.button("Kembali ke Menu Utama"):
            st.session_state.login_type = None
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

def admin_login_page():
    load_css()
    st.title("👨‍💼 Admin Login Portal")
    
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Admin login form
        username = st.text_input("Admin Username")
        password = st.text_input("Admin Password", type="password")
        
        if st.button("Login"):
            if username and password:
                # Add your admin authentication logic here
                st.success("Admin login berhasil!")
            else:
                st.error("Mohon isi username dan password admin!")
        
        if st.button("Kembali ke Menu Utama"):
            st.session_state.login_type = None
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
def add_footer():
    st.markdown("""
        <div class="footer">
            © 2024 Projek Akhir Kriptografi | Dibuat dengan penuh emosiiiiiiiiiiiiiiiiiiiiiiiiiii titit titit menggunakan Streamlit
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    if 'login_type' not in st.session_state:
        home_page()
    elif st.session_state.login_type == "User":
        user_login_page()
    elif st.session_state.login_type == "Admin":
        admin_login_page()
    
    add_footer()
