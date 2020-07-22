#!/usr/bin/env Python
# -*- coding: UTF-8 -*-
__author__ = 'marius'
__email__ = "pozniakovui@gmail.com"
'''database functions file'''

import psycopg2
import util
from sys import argv, exc_info

def connect_db(dbname, user, password):
    '''function to connect to database,
    input database name, username and password,
    returns connection from psycopg2'''
    
    try:
        conn = psycopg2.connect(dbname = dbname, user = user, password = password)
    except:
        util.error("no_connect_db")

    return conn

def insert_line(data, cursor):
    '''function just to insert inputted data to log_entry
    if any line isnt inserted, the inserted lines aren't committed'''

    try: 
        cursor.execute('''INSERT INTO log_entry(log_timestamp, log_status, log_short_text, log_text) VALUES (%s, %s, %s, %s)''',(str(data[0]) + ' ' + str(data[1]), data[2], data[3], data[4]))
    except:
        e = exc_info()
        print(e) 
        util.error('failed_insert', data)

def insert(connection, cursor):
    '''receives: connection, cursor from psycopg2,
       reads from given file and inserts line by line
        by certain rules
       returns None'''

    util.validate_system_argvs(2, argv = argv)

    if not util.path_exists(util.get_cwd() + '/' + argv[2]):
        util.error('file_doesnt_exist', argv[2])

    else:
        with open(argv[2]) as log_file:
            while True:
                log_file_entry = log_file.readline()
                
                if log_file_entry:
                    data = util.split_line(log_file_entry, log_file)
                    insert_line(data, cursor)
                else:
                    connection.commit()
                    break
    return

def select(cursor, query):
    '''not used but selects a query through a cursor'''

    cursor.execute(query)
    return cursor.fetchall()

def setup(connection, cur):
    '''setups log_entry table'''

    try:
        cur.execute ('''
        CREATE TABLE IF NOT EXISTS log_entry (
            log_id           serial            primary key,
            log_timestamp    timestamp         not null,
            log_status       varchar(40)       not null,
            log_short_text   varchar(100)              ,
            log_text         varchar(4000)     not null
        );      
        ''')

        connection.commit()

    except:
        print('log_entry table creation failed')

    return