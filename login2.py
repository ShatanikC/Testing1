import streamlit as st,gspread,pandas as pd
from supabase import create_client, Client # type: ignore
from oauth2client.service_account import ServiceAccountCredentials
import read_data,admin,stock_register
st.set_page_config(layout='wide')
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

SUPABASE_URL = st.secrets['supabase']['url']  
SUPABASE_KEY = st.secrets['supabase']['key']  
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def sign_in(email, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Login failed: {e}")

def sign_out():
    try:
        supabase.auth.sign_out()
        st.session_state.user_email = None
        st.session_state['authenticated'] = False  
        st.success("Successfully logged out.")
        st.rerun()
    except Exception as e:
        st.error(f"Logout failed: {e}")

def main_app(user_email):
    st.title("🎉 Welcome Page")
    st.success(f"Welcome, {user_email}! 👋")
    tab1,tab2,tab3,tab4=st.tabs(['Production Report','Quality Check','Stock Register','Dashboard'])
    with tab1:
        col1,col2=st.columns(2)
        with col1:
            read_data.production_report()
        with col2:
            read_data.daily_production_report()
        if st.button("Logout",key='logout1'):
            sign_out()
    with tab2:    
        col3,col4=st.columns(2)
        with col3:
            read_data.in_process_and_final_testing_report()
        with col4:
            read_data.pre_operation_checksheet()
        if st.button("Logout",key='logout2'):
            sign_out()
    with tab3:
        stock_register.opening_balance()
        stock_register.raw_material_consumed()
        stock_register.raw_material_received()
        
        if st.button("Logout",key='logout3'):
            sign_out()
    with tab4:
        admin.main()
        if st.button("Logout",key='logout4'):
            sign_out()
    

def auth_screen():
    st.title("🔐 Operations")
    option = st.header("Login")
    with st.form(key='login_form'):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit_button=st.form_submit_button('Submit')
        if submit_button:    
            # if option == "Sign Up":
            #     user = sign_up(email, password)
            #     if user and user.user:
            #         st.success("Registration successful. Please log in.")
            user = sign_in(email, password)
            if user and user.user:
                st.session_state.user_email = user.user.email
                st.session_state['authenticated'] = True
                st.success(f"Welcome back, {email}!")
                st.rerun()
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if st.session_state.user_email and st.session_state['authenticated']:
    main_app(st.session_state.user_email)
else:
    auth_screen()


