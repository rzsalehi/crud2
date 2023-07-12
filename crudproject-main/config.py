from pydantic import BaseSettings

class Setting(BaseSettings):
    MSSQL_URI = "mssql+pyodbc://tester:1234@DESKTOP-KLVA01I/testdb?driver=SQL+Server&TrustServerCertificate=yes&authentication=ActiveDirectoryIntegrated"

setting = Setting()