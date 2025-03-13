import streamlit as st
from Clients.Functions_ import talk_with_server as tws

def upgrade():
    # Get user info from session state
    user_info = st.session_state.get("user_info", None)
    current_subscription = user_info['abonnement'] if user_info else "basic"
    if "response" not in st.session_state:
        st.session_state.response={
            "abonnement":""
        }
     
    # Custom Styles
    st.markdown("""
        <style>
        /* Page Background */
        .stApp {
            background: linear-gradient(135deg, #f8f9fa, #dfe7ee);
            font-family: 'Arial', sans-serif;
        }

        /* Plan Box */
        .plan-box {
            border: 2px solid #007bff;
            border-radius: 10px;
            background-color: #ffffff;
            padding: 15px;
            margin: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .plan-box:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }

        /* Buttons */
        .upgrade-button {
            background-color: #007bff;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s;
        }
        .upgrade-button:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        .disabled-button {
            background-color: #d3d3d3;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: not-allowed;
        }

        /* Headers */
        .header {
            text-align: center;
            font-size: 1.8rem;
            color: #333;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page Header
    st.markdown("<div class='header'>Upgrade Your Plan</div>", unsafe_allow_html=True)
    st.write(f"**Current Plan:** {current_subscription.capitalize()}")

    # Subscription Plans
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='plan-box'>", unsafe_allow_html=True)
        st.subheader("Basic Plan")
        st.write("**Price:** Free")
        st.markdown("""
        - Access to basic features  
        - Standard analysis tools
        """)
        if current_subscription == "basic":
            st.info("Your current subscription")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='plan-box'>", unsafe_allow_html=True)
        st.subheader("Premium Plan")
        st.write("**Price:** $17/month")
        st.markdown("""
        - Access to all basic features  
        - Detailed analysis tools  
        - Chatbot support
        """)
        if current_subscription == "premium":
            st.info("Your current subscription")
        st.markdown("</div>", unsafe_allow_html=True)

    # Action Buttons
    col3, col4, col5 = st.columns([1, 2, 1])
    response=""
    with col4:
        if current_subscription == "basic":
            if st.button("Upgrade to Premium Plan"):
                doctor_data = {
                    "doctor_id": user_info["doctor_id"],
                    "abonnement": "premium"
                }
                response = tws.update_abonnement(doctor_data)
                st.session_state.response['abonnement']="premium"
                st.session_state["user_info"]["abonnement"] = "premium"
                st.rerun()
            if st.session_state.response['abonnement']=='basic':
                st.toast("Subscription successfully downgraded!")



        elif current_subscription == "premium":
            if st.button("Downgrade to Basic Plan"):
                doctor_data = {
                    "doctor_id": user_info["doctor_id"],
                    "abonnement": "basic"
                }
                response = tws.update_abonnement(doctor_data)
                st.session_state["user_info"]["abonnement"] = "basic"
                st.session_state.response['abonnement']='basic'

                st.rerun()
            if st.session_state.response['abonnement']=='premium':
                st.toast("Subscription successfully  upgraded!")



    # Return to Home Page Button
    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("Return to Home Page"):
        st.session_state.page = "home_page_doctor"

        st.rerun()

