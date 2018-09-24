#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import sqlite3
from config import database_name

connection = sqlite3.connect(database_name)
cursor = connection.cursor()



def createTable(table, keys):
    try:
        # Check if tables already exist
        cursor.execute('SELECT * FROM '+table)
        print('Table already exists')
    except:
        # If not, create them
        print('Creating table '+table)
        cursor.execute('CREATE TABLE ' +table+ ' '
                        '('+keys+')')


def dropTable(table):
    cursor.execute('DROP TABLE IF EXISTS ' + table)





def init_db():
    # Cleanup DB--------------------------------------------
    # dropTable('Player')
    # dropTable('Messages')
    # dropTable('Settings')


    # Set up DB ------------------------------------------------------
    createTable('Player',   'Id INTEGER PRIMARY KEY,'
                            'Chat_id INTEGER,'
                            'Name String')
                            
    createTable('Messages', 'Message_Id INTEGER PRIMARY KEY,'
                            'Chat_id INTEGER')

    createTable('Settings', 'Id INTEGER PRIMARY KEY,'
                            'Chat_id INTEGER,'
                            'Muted INTEGER,' #boolean
                            'Cleanup INTEGER')
