import streamlit as st
from Clients.Functions_ import talk_with_server as tws

def show_profile_doctor_page():
    # Add custom styles
    st.markdown("""
        <style>
        /* Page Background */
        .stApp {
            background: linear-gradient(135deg, #e0f7da, #d6f5d0);
            font-family: Arial, sans-serif;
        }

        /* Header Styling */
        .page-title {
            text-align: center;
            color: #2d6a4f;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .welcome-message {
            text-align: center;
            color: #40916c;
            font-size: 1.5rem;
            margin-bottom: 30px;
        }

        /* Info Boxes */
        .info-box {
            border: 1px solid #52b788;
            border-radius: 10px;
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .info-header {
            font-size: 1.2rem;
            color: #2d6a4f;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Buttons */
        .custom-button {
            background-color: #40916c;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s;
            text-align: center;
            width: 100%;
        }
        .custom-button:hover {
            background-color: #2d6a4f;
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # Page Title
    st.markdown("<div class='page-title'>📝 Doctor Profile</div>", unsafe_allow_html=True)

    # Retrieve User Information
    user_info = st.session_state.get("user_info", None)
    if not user_info:
        st.error("You are not logged in.")
        st.stop()

    # Welcome Message
    st.markdown(f"<div class='welcome-message'>👤 Welcome, Dr. {user_info['name']}!</div>", unsafe_allow_html=True)

    # Profile Details
    col1, col2 = st.columns([6, 4])

    with col1:
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("<div class='info-header'>Doctor Information</div>", unsafe_allow_html=True)
        st.write(f"**Email**: {user_info['email']}")
        st.write(f"**Specialization**: {user_info['specialization']}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("<div class='info-header'>Subscription Plan</div>", unsafe_allow_html=True)
        st.write(f"**Plan**: {user_info['abonnement'].capitalize()}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Return Button
    st.markdown("<hr>", unsafe_allow_html=True)
    col11, col21, col31 = st.columns([1, 2, 1])
    with col21:
        if st.button("Return to Home Page", key="return_button"):
            st.session_state.page = "home_page_doctor"

            st.rerun()
