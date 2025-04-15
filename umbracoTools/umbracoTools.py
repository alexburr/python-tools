# ------------------------------
#  umbracoTools.py
#  
#  A simple tool to list Umbraco users and their groups from a local Umbraco database
#
#  Usage: python umbracoTools.py
# ------------------------------

# -------
# IMPORTS
# -------
import os
import sys
import logging
import datetime
import pyodbc

from lib.umbracoUser import umbracoUser
from lib.umbracoUserGroup import umbracoUserGroup
from lib.queries import GetUmbracoUserGroups as Query_GetUmbracoUserGroups, GetUmbracoUsersWithGroups as Query_GetUmbracoUsersWithGroups
from config import driver, server, uid_file_path, pwd_file_path, database, trusted_connection, log_level

sys.path.append('../lib')

from dbCreds import dbCreds
from dbConnection import dbConnection
from pdfUtils import *
from logUtil import logUtil

# -------
# GLOBALS
# -------
application_name = 'umbracoTools'
db_creds = dbCreds(uid_file_path, pwd_file_path)
db_connection: dbConnection = dbConnection(driver, server, database, trusted_connection, db_creds)
logger = logUtil(log_level)
umbraco_users = []
umbraco_groups = []


# ----------------------------
def select_groups() -> None: 
    global db_connection
    global umbraco_groups
    global Query_GetUmbracoUserGroups
    global logger
    
    logger.method_start_debug()
    
    connection = db_connection.connection
    cursor = connection.cursor()
    query = Query_GetUmbracoUserGroups

    try:
        cursor.execute(query)

        for row in cursor:
            umbraco_usergroup = umbracoUserGroup(row.id, row.userGroupAlias, row.userGroupName)
            umbraco_groups.append(umbraco_usergroup)
            logger.info(f'Found group {umbraco_usergroup.id}: {umbraco_usergroup.userGroupName}')
    except pyodbc.Error as error:
        logger.error(f'A pyodbc error occurred: {str(error)}')
    except:
        logger.error('An error occurred')
    finally:
        cursor.close()

    if len(umbraco_groups) == 0:
        logger.warning('No groups found')
    else:
        logger.info(f'Found {len(umbraco_groups)} groups')
    
    logger.method_end_debug()


# -------------------------
def select_users() -> None:
    global db_connection
    global umbraco_users
    global Query_GetUmbracoUsersWithGroups
    global logger
    
    logger.method_start_debug()
    
    connection = db_connection.connection
    cursor = connection.cursor()

    query = Query_GetUmbracoUsersWithGroups

    try:
        cursor.execute(query)

        for row in cursor:
            umbraco_user = umbracoUser(row.id, row.userDisabled, row.userName, row.userLogin, row.userEmail, row.userLanguage, row.lastLoginDate, row.userGroupIds)
            umbraco_users.append(umbraco_user)
            logger.info(f'Found user {umbraco_user.id}: {umbraco_user.userName}')
    except pyodbc.Error as error:
        logger.error(f'A pyodbc error occurred: {str(error)}')
    except:
        logger.error('An error occurred')
    finally:
        cursor.close()

    if len(umbraco_users) == 0:
        logger.warning('No users found')
    else:
        logger.info(f'Found {len(umbraco_users)} users')
    
    logger.method_end_debug()


# ------------------------
def find_user_groups() -> None:
    global umbraco_groups
    global umbraco_users
    global logger
    
    logger.method_start_debug()

    for user in umbraco_users:
        logger.info(f'Finding {len(user.userGroupIds)} groups for user {user.id}...')
        user_group_ids = user.userGroupIds

        user_groups = []

        for user_group_id in user_group_ids:
            logger.info(f'  Searching {len(umbraco_groups)} groups for group {user_group_id}...')

            for group in umbraco_groups:
                if hasattr(group, 'id'):
                    if int(getattr(group, 'id')) == int(user_group_id):
                        user_groups.append(group)

        user.set_groups(user_groups)

        if len(user.groups) == 0:
            logger.warn(f'Found 0 groups for user {user.id}')
        else:
            logger.info(f'Found {len(user.groups)} groups for user {user.id}')    
    
    logger.method_end_debug()


# ------------------------
def print_users() -> None:
    global umbraco_users
    global logger

    logger.method_start_debug()
    for umbraco_user in umbraco_users:
        umbraco_user.print_user()
    logger.method_end_debug()


# -----------------
def main() -> None:
    global db_connection
    global umbraco_users
    global logger

    logger.method_start_debug()

    os.system('cls')
    db_connection.open_connection()
    select_groups()
    select_users()
    find_user_groups()
    db_connection.close_connection()
    print_users()

    logger.method_end_debug()


# -----
# BEGIN
# -----
if __name__ == '__main__':
    logger.add_file_hander(f'{application_name}.log', log_level)
    main()