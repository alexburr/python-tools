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
from lib.umbracoUserGroup import umbracoUserGroup
from lib.queries import GetUmbracoUsers as Query_GetUmbracoUsers, GetUmbracoUser2UserGroup as Query_GetUmbracoUser2UserGroup, GetUmbracoUserGroups as Query_GetUmbracoUserGroups
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
umbraco_groups = []


# ----------------------------
def select_groups() -> None: 
    global db_connection
    global umbraco_groups
    global Query_GetUmbracoUserGroups

    connection = db_connection.connection
    cursor = connection.cursor()

    query = Query_GetUmbracoUserGroups
    cursor.execute(query)

    for row in cursor:
        umbraco_usergroup = umbracoUserGroup(row.id, row.userGroupAlias, row.userGroupName)
        umbraco_groups.append(umbraco_usergroup)

    cursor.close()


# -------------------------
def select_users() -> None:
    global db_connection
    global umbraco_users
    global Query_GetUmbracoUsers
    
    connection = db_connection.connection
    cursor = connection.cursor()

    query = Query_GetUmbracoUsers
    cursor.execute(query)

    for row in cursor:
        umbraco_user = umbracoUser(row.id, row.userDisabled, row.userName, row.userLogin, row.userEmail, row.userLanguage, row.lastLoginDate)
        umbraco_users.append(umbraco_user)

    cursor.close()


# --------------------
def get_user_groups():
    global db_connection
    global umbraco_groups
    global umbraco_users
    global Query_GetUmbracoUser2UserGroup

    group_ids_for_user = []
    groups = []
    
    connection = db_connection.connection
    cursor = connection.cursor()

    for umbraco_user in umbraco_users:
        query = Query_GetUmbracoUser2UserGroup.format(umbraco_user.id)
        cursor.execute(query)

        for row in cursor:
            group = [group for group in umbraco_groups if group.id == row.userGroupId]
            groups.append(group)
        
        umbraco_user.set_groups(groups)
        groups = []

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
    select_groups()
    select_users()
    get_user_groups()
    db_connection.close_connection()
    print_users()



# -----
# BEGIN
# -----
if __name__ == '__main__':
    main()