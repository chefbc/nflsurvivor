from dataclasses import dataclass
import streamlit as st
# from supabase import create_client, Client

from nflsurvivor.db import supabase as sb


# @dataclass
# class Auth:



# supabase: Client = create_client(url, key)
# user = supabase.auth.sign_up(
#     email='example@email.com',
#     password='example-password',
# )



# supabase: Client = create_client(url, key)
# user = supabase.auth.sign_in(
#     email='example@email.com',
#     password='example-password'
# )



# https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/streamlit_authenticator/authenticate.py

class Authenticate:
    """
    This class will create login, logout, register user, reset password, forgot password, 
    forgot username, and modify user details widgets.
    """
    def __init__(self):

        self.supabase = sb.init_connection()

        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = None
        if 'username' not in st.session_state:
            st.session_state['username'] = None
        if 'logout' not in st.session_state:
            st.session_state['logout'] = None

    def login(self, form_name: str, location: str='main') -> tuple:
        """
        Creates a login widget.
        Parameters
        ----------
        form_name: str
            The rendered name of the login form.
        location: str
            The location of the login form i.e. main or sidebar.
        Returns
        -------
        str
            Name of the authenticated user.
        bool
            The status of authentication, None: no credentials entered, 
            False: incorrect credentials, True: correct credentials.
        str
            Username of the authenticated user.
        """
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")
        if not st.session_state['authentication_status']:
            # self._check_cookie()
            if st.session_state['authentication_status'] != True:
                if location == 'main':
                    login_form = st.form('Login')
                elif location == 'sidebar':
                    login_form = st.sidebar.form('Login')

                login_form.subheader(form_name)
                self.username = login_form.text_input('Username').lower()
                st.session_state['username'] = self.username
                self.password = login_form.text_input('Password', type='password')

                if login_form.form_submit_button('Login'):
                    self._check_credentials()