# streamlit_app.py

from turtle import width
import streamlit as st
# from supabase import create_client, Client
from nflsurvivor.db import supabase as sb

from rich import inspect
from streamlit_option_menu import option_menu


import os

import requests

st.set_page_config(layout="wide")

supabase = sb.init_connection()


#inspect(supabase)

#st.write(supabase)

#email = st.secrets["email"]
#password = st.secrets["password"]

def weeks():
    weeks = st.tabs([f"W{x+1}" for x in range(18)])

    for idx, week in enumerate(weeks):
    #     st.write(week)
        week.write(f"Week {idx+1} Picks")


def teams():
    rows = nfl_teams()

    for row in rows.data:
        st.header(f"{row['City']} {row['Name']}")
        st.image(f"./nflsurvivor/images/2019_{row['Abbreviation']}_wbg.png")



@st.experimental_memo(ttl=10800) # 3 hrs
def odd_data():
    API_KEY = st.secrets['the_odds_api_key']
    SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports
    REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited
    MARKETS = 'h2h,spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited
    ODDS_FORMAT = 'american' # decimal | american
    DATE_FORMAT = 'unix' # iso | unix

    odds_response = requests.get(f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds', 
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )

    if odds_response.status_code != 200:
        st.error(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

    else:
        odds_json = odds_response.json()
        # print('Number of events:', len(odds_json))
        # Check the usage quota
        st.info(f"Remaining requests: {odds_response.headers['x-requests-remaining']}")
        st.info(f"Used requests:  {odds_response.headers['x-requests-used']}")
        return odds_json


def main():
    

    sb.auth()

    st.sidebar.write("[pickdistribution](https://football.fantasysports.yahoo.com/survival/pickdistribution)")
    st.sidebar.write("[fivethirtyeight](https://projects.fivethirtyeight.com/2021-nfl-predictions/games)")
    st.sidebar.write("[espn picks](https://www.espn.com/nfl/picks)")
    st.sidebar.write("[survivorgrid](https://www.survivorgrid.com)")

    # st.write(odd_data())

    USERS = ['Casey', 'Nicole', 'Kam', 'Owen']

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)



    with col1:
        st.multiselect('Home', USERS) # default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)

    with col2:
        col2.metric("Temperature", "70 °F", "1.2 °F")

    with col3:
        #st.header("A cat")
        st.image(f"./nflsurvivor/images/2019_sf_wbg.png") #, width=128)

    with col4:
        #st.header("VS")
        #st.image(f"./nflsurvivor/images/at_sign_icon.png")
        st.header("@")
       #st.image("https://static.streamlit.io/examples/dog.jpg")

    with col5:
        #st.header("An owl")
        st.image(f"./nflsurvivor/images/2019_gb_wbg.png") #, width=128)

    with col6:
        col6.metric("Temperature", "70 °F", "1.2 °F")

    with col7:
        st.multiselect('Away', USERS) # default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)



# chefbc/nflsurvivor/nflsurvivor/images
        #st.write(f"{row['name']} has a :{row['pet']}:")


    # col1, col2, col3 = st.columns(3)
    # col1.metric("Temperature", "70 °F", "1.2 °F")
    # col2.metric("Wind", "9 mph", "-8%")
    # col3.metric("Humidity", "86%", "4%")




        # Print results.
    # for row in rows.data:
    #     st.write(f"{row['name']} has a :{row['pet']}:")



    # st.write




# https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031
# https://github.com/victoryhb/streamlit-option-menu
# https://github.com/mkhorasani/Streamlit-Authenticator

# https://supabase.com/docs/guides/client-libraries
# user = supabase.auth.sign_up(
#     email=email,
#     password=password,
# )

#email="chefbc@icloud.com"
#password='xxAT6BvFApkbTB39'
# user =  None
# try:
#     user = supabase.auth.sign_in(
#         email=email,
#         password=password,
#     )
# except Exception as ex:
#     st.warning(ex)


# # st.write(user.user.id)
# # st.write(user.user.email)
# st.write(user)
# inspect(user)

# del user

#inspect(supabase.auth)



# if 'name' not in st.session_state:
#     st.session_state['name'] = None
# if 'authentication_status' not in st.session_state:
#     st.session_state['authentication_status'] = None
# if 'username' not in st.session_state:
#     st.session_state['username'] = None
# if 'logout' not in st.session_state:
#     st.session_state['logout'] = None


# if 'username' not in st.session_state:
#     st.session_state['username'] = None


# # col1, col2, col3 = st.columns(3)

# # with col1:
# #     st.header("A cat")
# #     st.image("https://static.streamlit.io/examples/cat.jpg")

# # with col2:
# #     st.header("A dog")
# #     st.image("https://static.streamlit.io/examples/dog.jpg")

# # with col3:
# #     st.header("An owl")
# #     st.image("https://static.streamlit.io/examples/owl.jpg")
# # st.session_state['username'] = None

# if not st.session_state['username']:
#     # login
#     with st.form('login', clear_on_submit=True):
#         # sst.write('### Login')

#         selection = option_menu(None, ["Login", "Signup"], 
#         icons=['house', 'cloud-upload'], 
#         menu_icon="cast", default_index=0, orientation="horizontal")
#         # selected2

#         username = st.text_input('Username', value=email).lower()
#         passwd =st.text_input('Password', value=password, type='password')

#         submitted = st.form_submit_button("Submit")   
#         if submitted:      
#             #st.write(username)
#             #st.write(passwd)
#             #st.write(selection)

#             if selection == "Login":
#                 st.session_state['username'] = supabase.auth.sign_in(
#                     email=username,
#                     password=passwd,
#                 )
#             elif selection == "Signup":
#                 st.session_state['username'] = supabase.auth.sign_up(
#                     email=username,
#                     password=passwd,
#                 )

# if st.session_state['username']:
#     # logout
#     with st.form('logout', clear_on_submit=True):
#         st.write(st.session_state['username'].user.email)
#         submitted = st.form_submit_button("Logout")
#         if submitted:  
#              st.session_state['username'] = None



# def check_password():
#     """Returns `True` if the user had a correct password."""

#     def password_entered():
#         """Checks whether a password entered by the user is correct."""
#         if (
#             st.session_state["username"] in st.secrets["passwords"]
#             and st.session_state["password"]
#             == st.secrets["passwords"][st.session_state["username"]]
#         ):
#             st.session_state["password_correct"] = True
#             del st.session_state["password"]  # don't store username + password
#             del st.session_state["username"]
#         else:
#             st.session_state["password_correct"] = False

#     if "password_correct" not in st.session_state:
#         # First run, show inputs for username + password.
#         st.text_input("Username", on_change=password_entered, key="username")
#         st.text_input(
#             "Password", type="password", on_change=password_entered, key="password"
#         )
#         return False
#     elif not st.session_state["password_correct"]:
#         # Password not correct, show input + error.
#         st.text_input("Username", on_change=password_entered, key="username")
#         st.text_input(
#             "Password", type="password", on_change=password_entered, key="password"
#         )
#         st.error("😕 User not known or password incorrect")
#         return False
#     else:
#         # Password correct.
#         return True

# if check_password():
#     st.write("Here goes your normal Streamlit app...")
#     st.button("Click me")



# login, signup = st.tabs(["Login", "Signup"])
    
# with login:
#     with st.form('my_form2'):
#         st.text_input('Username').lower()
#         st.text_input('Password', type='password')
#         submitted = st.form_submit_button("Login")   
#         if submitted:      
#             st.write('Login')

# #     login = st.button('Login')

# with signup:
#     with st.form('my_form3'):
#         st.text_input('Username').lower()
#         st.text_input('Password', type='password')
#         submitted = st.form_submit_button("Create")   
#         if submitted:      
#             st.write('Create')



#with st.sidebar:

# selected2

    # st.text_input('Username').lower()
    # st.text_input('Password', type='password')


    # submitted = st.form_submit_button("Submit")   
    # if submitted:      
    #     st.write('submit')





# def login(form_name: str, location: str='main') -> tuple:
#     if location not in ['main', 'sidebar']:
#         raise ValueError("Location must be one of 'main' or 'sidebar'")
#     if not st.session_state['authentication_status']:
#         # self._check_cookie()
#         if st.session_state['authentication_status'] != True:
#             if location == 'main':
#                 login_form = st.form('Login')
#             elif location == 'sidebar':
#                 login_form = st.sidebar.form('Login')

#             login_form.subheader(form_name)
#             username = login_form.text_input('Username').lower()
#             # st.session_state['username'] = username
#             password = login_form.text_input('Password', type='password')

#             if login_form.form_submit_button('Login'):
#                 # self._check_credentials()
#                 return supabase.auth.sign_in(
#                     email='example@email.com',
#                     password='example-password'
#                 )



# st.session_state['user'] = login("Login", "sidebar")

# st.session_state['user'] = login("Login", "sidebar")

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()

@st.experimental_memo(ttl=600)
def nfl_teams():
    return supabase.table("nfl-teams").select("*").execute()




if __name__ == "__main__":


    main()


    if st.session_state['session']:

        rows = run_query()

        # st.write(rows)

        # Print results.
        for row in rows.data:
            st.write(f"{row['name']} has a :{row['pet']}:")