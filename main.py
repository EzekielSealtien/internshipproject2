import streamlit as st
import Clients.Views_.signup_doctor as show_signup_doctor_page
import Clients.Views_.login_doctor as show_login_doctor_page
import Clients.Views_.profil_doctor as show_profile_doctor_page
import Clients.Views_.home_page_doctor as show_home_page_doctor
import Clients.Views_.upgrade as upgrade
import Clients.Views_.report_historic as report_hist


page =  st.query_params.get("page", ["login"])

if page == "profil_doctor":
    show_profile_doctor_page.show_profile_doctor_page()
elif page == "signup_doctor":
    show_signup_doctor_page.show_signup_doctor_page()
elif page == "login_doctor":
    show_login_doctor_page.show_login_doctor_page() 
elif page == "report_historic":
    report_hist.show_reports_historic() 
elif page == "upgrade":
    upgrade.upgrade() 
elif page == "home_page_doctor":
    show_home_page_doctor.show_home_page_doctor()
else:
    show_login_doctor_page.show_login_doctor_page()

