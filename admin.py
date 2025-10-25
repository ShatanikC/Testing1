import streamlit as st
import read_data

def check_login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

def show_login_form():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials. Please try again.")

def show_logout_button():
    if st.button("Logout",key='logout'):
        st.session_state.logged_in = False
        st.success("Logged out successfully!")

def main():
    check_login()    
    st.header('Admin Login')
    if st.session_state.logged_in:
        st.title("Welcome to the Dashboard")
        st.write("You are logged in and can access all content.")
        data=read_data.connect_to_gsheet(sheet_name='Sheet1').get_all_records()
        st.dataframe(data)
        show_logout_button()
    else:
        show_login_form()
    
