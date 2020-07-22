#!/usr/bin/env Python
# -*- coding: UTF-8 -*-
__author__ = 'marius'
__email__ = "pozniakovui@gmail.com"
'''log generating file'''

from db import insert_line
from datetime import date, datetime
from random import choice
import json
from time import sleep

def generate(conn, cur):
    '''function to random log messages and insert them to database'''

    statuses = import_random_choices('status')
    short_texts = import_random_choices('short_text')
    texts = import_random_choices('text')

    
    while True:
        #we need to randomise
        #date+time, status, short_text, text
        data_to_insert = []    

        #append date
        data_to_insert.append(date.today())

        #append time
        data_to_insert.append(datetime.now().time())

        #status
        data_to_insert.append(choice(statuses['status']))

        #short_text
        data_to_insert.append(choice(short_texts['short_text']))

        #text
        data_to_insert.append(choice(texts['text']))

        #insert line by line
        insert_line(data = data_to_insert, cursor = cur)
        conn.commit()

        #wait for 5 secs
        sleep(5)
        print('inserted', data_to_insert)


def import_random_choices(type_of_json):
    '''function to read from json upload possible random choices'''
    
    with open('random_log_jsons/sample_' + type_of_json + '.json') as json_file:
        data = json.load(json_file)

    return data