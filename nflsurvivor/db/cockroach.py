import os

from sqlmodel import SQLModel

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from cockroachdb.sqlalchemy import run_transaction

DATABASE_URL = os.environ.get("DATABASE_URL")

# print(DATABASE_URL)

#engine = create_async_engine(DATABASE_URL, echo=True, future=True)

engine = create_engine(DATABASE_URL, echo=True, future=True)

def init_db():
    with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        conn.run_sync(SQLModel.metadata.create_all)

def get_session() -> Session:
    # async_session = sessionmaker(
    #     engine, class_=Session, expire_on_commit=False
    # )
    # return async_session
    # with Session() as session:
    #     yield session
    yield Session(engine, future=True)


    # yield sessionmaker(
    #     engine, class_=Session, expire_on_commit=False
    # )




    # try:
    #     db_uri = os.path.expandvars(conn_string)
    #     db_uri = urllib.parse.unquote(db_uri)

    #     psycopg_uri = db_uri.replace(
    #         'postgresql://', 'cockroachdb://').replace(
    #             'postgres://', 'cockroachdb://').replace(
    #                 '26257?', '26257/bank?')
    #     # The "cockroachdb://" prefix for the engine URL indicates that we are
    #     # connecting to CockroachDB using the 'cockroachdb' dialect.
    #     # For more information, see
    #     # https://github.com/cockroachdb/sqlalchemy-cockroachdb.

    #     print(psycopg_uri)
    #     engine = create_engine(psycopg_uri)
    # except Exception as e:
    #     print('Failed to connect to database.')
    #     print('{0}'.format(e))

    # seen_account_ids = []

    # run_transaction(sessionmaker(bind=engine),
    #                 lambda s: create_accounts(s, 100))