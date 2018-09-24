#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import sqlite3
from config import database_name

connection = sqlite3.connect(database_name)
cursor = connection.cursor()


# Cleanup DB
"""
cursor.execute('DROP TABLE IF EXISTS Player')
"""


try:
    # Check if tables already exist
    cursor.execute('SELECT * FROM Player')
    print('Tables already existing')
except:
    # If not, create them
    print('Creating tables')
    cursor.execute('CREATE TABLE Player '
                    '(Id INTEGER PRIMARY KEY, '
                    'Chat_id INTEGER, '
                    'Name String)')


