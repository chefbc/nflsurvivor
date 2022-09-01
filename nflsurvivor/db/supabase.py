# import os

# from sqlmodel import SQLModel

# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv

# if os.path.exists("/vault/secrets/env"):
#   config = load_dotenv("/vault/secrets/env")

# # DATABASE_URL = os.environ.get("DATABASE_URL")

# driver = os.getenv("DB_DRIVER")
# user = os.getenv("APP_OWNER")
# password = os.getenv("APP_OWNER_PASS")
# server = os.getenv("DB_HOST")
# port = os.getenv("DB_PORT")
# db = os.getenv("APP_DATABASE")

# DATABASE_URL =  f"{driver}://{user}:{password}@{server}:{port}/{db}"

# engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(SQLModel.metadata.create_all)

# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with async_session() as session:
#         yield session

import streamlit as st
from supabase import create_client, Client
import os
from streamlit_supabase_auth import login_form, logout_button


# # Initialize connection.
# # Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)


def auth():
    #st.title("Component Gallery")
    #st.header("Login with Supabase Auth")

    os.environ["SUPABASE_URL"] = st.secrets["supabase_url"]
    os.environ["SUPABASE_KEY"] = st.secrets["supabase_key"]

    if 'session' not in st.session_state:
        st.session_state['session'] = None

    with st.sidebar:
        st.session_state['session'] = login_form(
            # url=st.secrets["supabase_url"],
            # apiKey=st.secrets["supabase_key"],
            # providers=[]# "apple", "facebook", "github", "google"],
        )

    # session = login_form(providers=["apple", "facebook", "github", "google"])
    #st.write(session)
    if not st.session_state['session']:
        return
    st.experimental_set_query_params(page=["success"])
    with st.sidebar:
        st.write(f"Welcome {st.session_state['session']['user']['email']}")
        logout_button()








# supabase = init_connection()

# # Perform query.
# # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def run_query():
#     return supabase.table("mytable").select("*").execute()

# rows = run_query()

# # Print results.
# for row in rows.data:
#     st.write(f"{row['name']} has a :{row['pet']}:")