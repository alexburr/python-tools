import pyodbc  # requires python -m pip install pyodbc
from dbCreds import dbCreds

class dbConnection():
    def __init__(self, driver: str, server: str, database: str, trusted_connection: str, db_creds: dbCreds):
        self.driver = driver
        self.server = server
        self.database = database
        self.trusted_connection = trusted_connection

        self.uid = db_creds.uid
        self.pwd = db_creds.pwd

        self.connection_string = (
                                    rf'DRIVER={self.driver};'
                                    rf'SERVER={self.server};'
                                    rf'UID={self.uid};'
                                    rf'PWD={self.pwd};'
                                    rf'DATABASE={self.database};'
                                    rf'Trusted_Connection={self.trusted_connection};'
                                 )

    def open_connection(self):
        self.connection = pyodbc.connect(self.connection_string)


    def close_connection(self):
        self.connection.close()

