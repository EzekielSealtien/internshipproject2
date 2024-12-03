import streamlit as st
from Clients.Functions_ import talk_with_server as tws
from Clients.Functions_ import retrieve_content as r_c
from Clients.Functions_ import CNN
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_openai.chat_models import ChatOpenAI



def show_home_page_doctor():
    # Apply custom styles
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
    
    if "check" not in st.session_state:
        st.session_state.check=False
    if "response_model" not in st.session_state:
        st.session_state.response_model=""
    if "report_data" not in st.session_state:
        st.session_state.report_data={}

    
    # User Information
    user_info = st.session_state.get("user_info", None)
    if not user_info:
        st.error("You are not logged in.")
        st.stop()

    # Initialize session state variables
    if "rapport_medical" not in st.session_state:
        st.session_state.rapport_medical = ""
        
    reports_raw=user_info.get('reports')
    
    #Transform reports in text
    text1=""
    for report in reports_raw:
        chaine=f"report's content of {report['title']} :{report['content']}"
        text1+=chaine
    if "context" not in st.session_state:
        st.session_state.context=text1

    
    # Welcome Header
    st.markdown(f"<div class='header'>Welcome, {user_info['name']}</div>", unsafe_allow_html=True)

    # Navigation Buttons
    col1, col2 = st.columns([2, 8])
    with col2:
        nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
        with nav_col1:
            if st.button("Profile", key="profile_button"):
                st.query_params["page"] = "profil_doctor"
                st.rerun()
        with nav_col2:
            if st.button("My Plan", key="upgrade_plan"):
                st.query_params["page"] = "upgrade"
                st.rerun()
        with nav_col3:
            if st.button("Report History", key="report_history"):
                st.query_params["page"] = "report_historic"
                st.rerun()
        with nav_col4:
            if st.button("🔒 Logout", key="logout_button"):
                st.session_state.clear()
                st.session_state["is_logged_in"] = False
                st.success("You are now logged out.")
                st.query_params.update(page="login_doctor")
                st.rerun()

    # File Upload and Report Input Section
    st.markdown("<div class='frame'>", unsafe_allow_html=True)
    st.subheader("Medical Report Analysis")

    name = st.text_input("Patient's Name", placeholder="Enter the patient's name")
    file_uploaded = st.file_uploader("Upload your report (Max size: 1MB)", type=["pdf", "docx"])
    rapport_medical = st.text_area("Enter the medical report text:", value="", placeholder="Type or paste the report text here")

    # Process Text Input
    if rapport_medical:
        st.session_state.rapport_medical = rapport_medical

    # Process Uploaded File
    if file_uploaded:
        if file_uploaded.size > 1 * 1024 * 1024:
            st.error("The file exceeds the 1MB size limit. Please upload a smaller file.")
        else:
            st.session_state.rapport_medical = r_c.retrieve_content_file_uploaded(file_uploaded)



    # Analyze Medical Report Button
    if st.button("Analyze Medical Report", key="analyze_report"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Submitted Medical Report:")
        st.write(st.session_state.rapport_medical)

        # Call Backend to Analyze Report
        response = CNN.analyse_text(st.session_state.rapport_medical)
        st.session_state.response_model=response
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("AI-Analyzed Medical Report:")
        st.session_state.check=True
    st.write(st.session_state.response_model)
    # Save Report Button
    if st.session_state.check:
        if st.button("Save Report", key="save_report"):
            report_name = f"{name}"
            content=f"{st.session_state.response_model}"
            st.session_state.report_data = {
                "doctor_id": user_info.get("doctor_id"),
                "title": report_name,
                "content": content
            }
            response_report_sent = tws.create_report(st.session_state.report_data)

            # get all the reports for a doctor
            all_reports=tws.get_all_reports_from_doctor(user_info.get("doctor_id"))

            if all_reports:    
                #Transform reports in text
                text=""
                for report in all_reports:
                    chaine=f"report's content of {report['title']} :{report['content']}"
                    text+=chaine
            
                st.session_state.context=text
                
            if response_report_sent:
                st.toast("Report saved successfully!")
                st.session_state["user_info"]["reports"].append(st.session_state.report_data)
                st.session_state.check=False
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    current_subscription = user_info['abonnement'] if user_info else "basic"


    #Si jamais l'utilisateur a un compte premuim
    if current_subscription=="premium":
        with st.sidebar:
            # Ensure chat history is initialized
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = [
                    AIMessage(content="Hey there, I am Cassandra. How can I be of service to you?")
                ]

            # Display conversation messages in a container
            chat_container = st.container()

            # User input box at the bottom
            user_query = st.chat_input("How can Cassandra help?")

            # Render chat history inside the container
            with chat_container:
                for message in st.session_state.chat_history:
                    if isinstance(message, AIMessage):
                        with st.chat_message("AI"):
                            st.write(message.content)
                    elif isinstance(message, HumanMessage):
                        with st.chat_message("Human"):
                            st.write(message.content)

            # Handle new user input
            if user_query is not None and user_query != "":
                # Append user message to chat history
                st.session_state.chat_history.append(HumanMessage(content=user_query))
                with chat_container:
                    with st.chat_message("Human"):
                        st.markdown(user_query)

                # Generate AI response and display it
                with chat_container:
                    with st.chat_message("AI"):
                        result = tws.get_response_model(st.session_state.context, user_query)
                        st.session_state.chat_history.append(AIMessage(content=result))
                        st.markdown(result)

                    
