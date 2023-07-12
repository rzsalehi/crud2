# import pyodbc
# from fastapi import FastAPI
#
# #app = FastAPI()
#
# # Connection string parameters
# server = 'DESKTOP-KLVA01I'
# database = 'testdb'
# username = 'tester'
# password = '1234'
#
# # Create the connection string
# connection_string = f"Driver={{SQL Server}};Server={server};Database={database};UID={username};PWD={password}"
#
# # Connect to the database
# conn = pyodbc.connect(connection_string)
#
# # Test the connection
# cursor = conn.cursor()
# cursor.execute("SELECT * from test")
# row = cursor.fetchone()
# print(row)  # Prints the SQL Server version
#
# # Close the connection
# conn.close()

from sqlmodel import SQLModel, create_engine, Session

from config import setting
engine= create_engine(setting.MSSQL_URI)


def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session (engine) as session:
        yield session
