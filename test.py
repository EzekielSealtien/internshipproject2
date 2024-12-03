import streamlit as st

import streamlit as st

# Custom CSS to move the sidebar to the right
st.markdown("""
    <style>
        /* Move the sidebar to the right */
        .stSidebar {
            float: right;
        }
        .stApp {
            direction: rtl;
        }
        .css-1d391kg { /* Adjust the content alignment */
            direction: ltr;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.write("This is a right-aligned sidebar!")

st.write("Main content goes here.")
