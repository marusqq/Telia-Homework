#!/usr/bin/env Python
# -*- coding: UTF-8 -*-
__author__ = 'marius'
__email__ = "pozniakovui@gmail.com"
'''useful utility function file'''

import os

def validate_system_argvs(num_of_validation, argv):
    '''checks if system argvs pass various validations,
    if validations are broken, code quits'''
    if num_of_validation == 1:
        if len(argv) < 2:
            quit('[VALIDATION 1] usage python3 <file.py> <mode> (<file> if mode = insert)')

    elif num_of_validation == 2:
        if len(argv) < 3:
            quit('usage python3 <file.py> <mode> <file>')

def collect_python_error(file):
    long_error = ''
    next_line = '!@#$'

    while len(next_line) > 1:
        next_line = file.readline()
        long_error += next_line
    return long_error

def split_line(string, file):
    '''receives a string
    then divides it into a list 
    so that it could be inserted to database
    '''
    #'Unhandled', 'Error\n'
    splitted = []

    #split by spaces
    try_to_split = string.split(' ')
    
    #add date, time, log_status, log_short_text
    for i in range(0,4):
        splitted.append(try_to_split[i])

    for removed in splitted:
        try_to_split.remove(removed)


    for i in range(len(try_to_split)):
        if i != len(try_to_split)-1:
            try_to_split[i] += ' ' 

    try_to_split = ''.join(try_to_split)

    #add log_text
    splitted.append(try_to_split)

    if splitted[len(splitted) - 2] == 'Unhandled':
        splitted[len(splitted) - 2] = splitted[len(splitted) - 2] + ' ' + splitted[len(splitted) - 1]
        splitted[len(splitted) - 1] = ''
        if splitted[len(splitted) - 2] == 'Unhandled Error\n':
            long_error = collect_python_error(file)
            splitted[len(splitted) - 1] = long_error

    return splitted

def error(error_code, free_text = None):
    if error_code == 'file_doesnt_exist':
        print('file', free_text, 'doesnt exist')

    elif error_code == 'failed_insert':
        print('insert failed with line', free_text)
    quit()

def path_exists(path):
    '''returns True if inputted path exists'''
    return os.path.exists(path)

def get_cwd():
    '''returns currect working directory using os module'''
    return os.getcwd()