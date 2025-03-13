import streamlit as st
from Clients.Functions_ import talk_with_server as tws

def show_login_doctor_page():
    # Page Title
    st.markdown("""
        <h1 style='text-align: center; color: #007bff; font-size: 2.5rem;'>Doctor Login</h1>
    """, unsafe_allow_html=True)

    # Login Form
    with st.form("login_form"):
        st.markdown("""
            <div style='text-align: center; margin-bottom: 20px;'>
                <p style='color: #555; font-size: 1rem;'>Please enter your email and password to log in.</p>
            </div>
        """, unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit = st.form_submit_button("Login", type="primary")

        # Form Submit Logic
        if submit:
            user_info = tws.login_doctor(email, password)
            if user_info:
                st.success("Login successful!")
                st.session_state["email"] = email
                st.session_state["user_info"] = user_info
                st.session_state.page = "home_page_doctor"
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")

    # Footer with Sign-up Button
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2 = st.columns([6, 4])
    with col2:
        if st.button("Sign up"):
            st.session_state.page = "signup_doctor"

            st.rerun()
