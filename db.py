#!/usr/bin/env Python
# -*- coding: UTF-8 -*-
__author__ = 'marius'
__email__ = "pozniakovui@gmail.com"
'''database functions file'''

import psycopg2
import util
from sys import argv
import sys

def connect_db(dbname, user, password):
    
    try:
        conn = psycopg2.connect(dbname = dbname, user = user, password = password)
        print('connected to database!')

    except:
        quit('unable to connect to database')

    return conn

def insert_line(data, cursor):

    try: 
        cursor.execute('''INSERT INTO log_entry(log_date, log_time, log_status, log_short_text, log_text) VALUES (%s, %s, %s, %s, %s)''',(data[0], data[1], data[2], data[3], data[4]))
    except:
        e = sys.exc_info()
        print(e) 
        util.error('failed_insert', data)

def insert(connection, cursor):

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

    cursor.execute(query)
    return cursor.fetchall()

def setup(connection, cur):
    '''setups log_entry table'''

    try:
        cur.execute ('''
        CREATE TABLE IF NOT EXISTS log_entry (
            log_id           serial            primary key,
            log_date         date              not null,
            log_time         time              not null,
            log_status       varchar(40)       not null,
            log_short_text   varchar(100)      not null,
            log_text         varchar(4000)     not null
        );      
        ''')

        connection.commit()
        print('log_entry table created')

    except:
        print('log_entry table creation failed')

    return