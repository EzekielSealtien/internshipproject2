import streamlit as st
from Clients.Functions_ import talk_with_server as tws
from Clients.Functions_ import retrieve_content as r_c

def show_reports_historic():
    
    
    st.markdown("""
    <style>
    /* Overall Background */
    .stApp {
        background: linear-gradient(135deg, #d3d3d3, #a9a9a9); /* Light gray to dark gray gradient */
        font-family: 'Arial', sans-serif;
    }
    
    /* Frames */
    .frame {
        border: 1px solid #ccc;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }
    .frame:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

    /* Buttons */
    .custom-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.2s;
        width: 100%;
    }
    .custom-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .danger-button {
        background-color: #e74c3c;
    }
    .danger-button:hover {
        background-color: #c0392b;
    }

    /* Header Styling */
    .header {
        text-align: center;
        color: #333;
        font-size: 2rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Input Fields */
    input[type="text"], textarea, input[type="file"] {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)

    user_info = st.session_state.get("user_info", None)
    st.header("Medical reports")
    if not user_info:
        st.error("You are not logged in.")
        if st.button("Log in"):
            st.query_params.update(page="login_doctor")
            st.rerun()
        st.stop()    
        
        
    reports = user_info.get('reports')
    if not reports:
        st.info("You do not have any reports !")
    else:
        for report in reports:
            with st.container():
                st.markdown("<div class='patient-frame'>", unsafe_allow_html=True)
                st.write(f"**Name**: {report["title"]}")
                st.write(f"**Content**: {report["content"]}")

    # Return to Home Page Button
    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("Return to Home Page"):
        st.session_state.page = "home_page_doctor"
        st.rerun()
