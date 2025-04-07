# ------------------------------
#  umbracoTools.py
#  Usage: python umbracoTools.py
# ------------------------------

# -------
# IMPORTS
# -------
import os
import sys
import logging
import datetime

from lib.umbracoUser import umbracoUser
from config import driver, server, uid_file_path, pwd_file_path, database, trusted_connection

sys.path.append('../lib')

from dbCreds import dbCreds
from dbConnection import dbConnection
from pdfUtils import *

# -------
# GLOBALS
# -------

db_creds = dbCreds(uid_file_path, pwd_file_path)
db_connection: dbConnection = dbConnection(driver, server, database, trusted_connection, db_creds)
umbraco_users = []


# -------------------------
def select_users() -> None:
    global db_connection
    global umbraco_users
    
    connection = db_connection.connection
    cursor = connection.cursor()

    query = 'SELECT id, userDisabled, userName, userLogin, userEmail, userLanguage, lastLoginDate FROM umbracoUser'
    cursor.execute(query)

    for row in cursor:
        umbraco_user = umbracoUser(row.id, row.userDisabled, row.userName, row.userLogin, row.userEmail, row.userLanguage, row.lastLoginDate)
        umbraco_users.append(umbraco_user)

    cursor.close()


# ------------------------
def print_users() -> None:    
    global umbraco_users

    for umbraco_user in umbraco_users:
        umbraco_user.print_user()


# -----------------
def main() -> None:
    global db_connection
    global umbraco_users

    os.system('cls')
    db_connection.open_connection()
    select_users()
    db_connection.close_connection()
    print_users()



# -----
# BEGIN
# -----
if __name__ == '__main__':
    main()