#!/usr/bin/env Python
# -*- coding: UTF-8 -*-
__author__ = 'marius'
__email__ = "pozniakovui@gmail.com"
'''useful utility function file'''

import psycopg2
from sys import argv
import util 
import db

#connect to database
connection = db.connect_db(dbname = 'telia_logs', user = 'marius', password = 'default')

util.validate_system_argvs(1, argv = argv)

cur = connection.cursor()

#depending on argvs
if argv[1] == 'select':
    db.select(cur, query = 'select * from log_entry')
    
elif argv[1] == 'insert':
    db.insert(connection, cur)

elif argv[1] == 'setup':
    db.setup(connection, cur)
    


