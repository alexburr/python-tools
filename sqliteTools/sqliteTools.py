#!/usr/bin/env python3
import os
import sys
import sqlite3

from config import dbPath, defaultDbFileName
from globals import table_names, column_names


# ------------------------
def GetTableNames(cursor):
    global table_names

    query = "select name from sqlite_master WHERE type='table';"
    cursor.execute(query)
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        table_names.append(table_name)


# --------------------
def PrintTableNames():
    global table_names

    print("")
    print("Tables")
    print("------")
    for table_name in table_names:
        print(table_name)


# -----------------------------
def PrintTableName(table_name):
    name_length = len(table_name)
    print("")
    print(f"{table_name}")


# ------------------------------------------
def GetTableColumnNames(cursor, table_name):
    global column_names

    query = f"select * from {table_name} limit 1"
    cursor.execute(query)
        
    columns = list(map(lambda x: x[0], cursor.description))
    
    for column in columns:
        column_names.append(column)


# --------------------------
def PrintTableColumnNames():
    global column_names

    column_names_string = ""
    column_names_length = len(column_names)

    for i in range(column_names_length):
        if i == column_names_length - 1:
            column_names_string = column_names_string + f"{column_names[i]}"
        else:
            column_names_string = column_names_string + f"{column_names[i]}, "
    
    PrintSeparator("-", column_names_string)
    print(column_names_string)
    PrintSeparator("-", column_names_string)


# ---------------------------------------
def PrintSeparator(character, footprint):
    length = len(footprint)

    terminal_size = os.get_terminal_size()
    column_width = terminal_size.columns

    if length > column_width:
        length = column_width

    for i in range(length):
        print(f"{character}", end="")
    print("")


# -------------------------------------
def PrintTableData(cursor, table_name):
    global table_names
    
    query = f"select * from {table_name}"
    cursor.execute(query)

    rows = cursor.fetchall()
    
    for row in rows:
        PrintTableRow(row)


# ---------------------
def PrintTableRow(row):
    row_length = len(row)

    for i in range(row_length):
        if i == row_length - 1:
            print(f"'{row[i]}'")
        else:            
            print(f"'{row[i]}', ", end="")


# ------------------------
if __name__ == "__main__":

    if sys.platform.startswith('win'):
       os.system('cls')
    else:
       os.system('clear')

    print(f"Looking in folder {dbPath}")
    file_name = input(f"Enter db filename (or press ENTER to use {defaultDbFileName}): ")
    if not file_name:
        file_name = defaultDbFileName
    if len(file_name) == 0:
        file_name = defaultDbFileName
    if not file_name.strip():
        file_name = defaultDbFileName

    db_path_and_file_name = dbPath + "\\" + file_name

    with sqlite3.connect(db_path_and_file_name) as sqliteConnection:
        cursor = sqliteConnection.cursor()
        GetTableNames(cursor)
        PrintTableNames()
        print("")
        table_name = input("Enter table name: ")
        PrintTableName(table_name)
        GetTableColumnNames(cursor, table_name)
        PrintTableColumnNames()        
        PrintTableData(cursor, table_name)

    print("")