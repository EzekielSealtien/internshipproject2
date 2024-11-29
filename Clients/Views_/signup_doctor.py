import streamlit as st
import bcrypt
from Clients.Functions_ import talk_with_server as tws


def show_signup_doctor_page():
    # Custom Page Title
    st.markdown("""
        <style>
        .page-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 30px;
        }
        .form-container {
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .register-button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s;
        }
        .register-button:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        .error-message {
            color: red;
            font-weight: bold;
            text-align: center;
        }
        </style>
        <div class="page-title">Doctor Sign Up</div>
    """, unsafe_allow_html=True)

    # Signup Form
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    with st.form("sign_up_form"):
        name = st.text_input("Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter a strong password")
        specialization = st.text_input("Specialization", placeholder="Enter your specialization")
        submit = st.form_submit_button("Register", help="Click to complete your registration")

        if submit:
            # Password Hashing
            if password:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

                # Create user data dictionary
                user_data = {
                    "name": name,
                    "email": email,
                    "password": hashed_password,
                    "specialization": specialization,
                    "abonnement": "basic" 
                }

                # Call backend to register the doctor
                response = tws.create_doctor(user_data)
                if "doctor_id" in response:
                    st.success("Registration successful! Redirecting to login...")
                    st.session_state["email"] = email
                    st.query_params.update(page="login_doctor")
                    st.rerun()
                else:
                    st.markdown("<div class='error-message'>Registration failed. Please try again.</div>", unsafe_allow_html=True)
            else:
                st.error("Password cannot be empty.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer Note
    st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            Already have an account? <a href="?page=login_doctor" style="color: #007bff; text-decoration: none;">Login here</a>
        </div>
    """, unsafe_allow_html=True)
