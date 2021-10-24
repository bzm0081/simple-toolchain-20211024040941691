import random
from flask import Flask, request
import json
import re
import json.decoder
import hashlib
from tkinter.constants import NONE
from _random import Random
def specific_string(length, data):
    
    x = random.randint(0,length-8)
    return data[x:x+8]


def hash_string(string):
    hash_val = hashlib.sha256()
    hash_val.update(string.encode())
    print(hash_val.hexdigest())
    return hash_val.hexdigest()


def create_matrix(data: list):
    for d in data:
        if type(d) != int:
            raise  ValueError('error')
    ptr = 0
    print(len(data))
    out = []
    for i in range(0, 15):
        tmp = []
        for j in range(0,15):
            if  (i<6 and j > 8 ) or (i>8 and j<6 ) :
                print('one')
                tmp.append(69)
            else:
                print(ptr)
                tmp.append(data[ptr])
                ptr= ptr+1   
        
        out.append(tmp)
    print( out)
    return out
def reverse_matrix(matrix):
    out = []
    for row in matrix:
        for element in row:
            if element is not 69:
                out.append(element)
    return out


def matrix_transpose_hash(matrix):
    string = ''
    for i in range(0, 15):
        for j in range(0, 15):
            if matrix[j][i] is 69:
                continue
            else:
                string = string + str(matrix[j][i])
    print(string)
    return string
def check_for_insertion(matrix, row: int, col: int, value: int):
    
    flag = True
    if value < 0:
        return {
            'status': 'error: invalid value'
        }
    if (row in range(9, 15) and col in range(0, 6)) or (col in range(9, 15) and col in range(0, 6)):
        return {
            'status': 'error: invalid cell reference'
        }
    if matrix[row][col] is not None and matrix[row][col] < 0:
        return {
            'status': 'error: attempt to change fixed hint'
        }
    for i in range(0, 15):
        if abs(matrix[row][i]) == value or abs(matrix[i][col]) == value:
            flag = False
    
    matrix[row][col] = value       
    if flag:
        return {
            'status': 'ok',
            'grid': reverse_matrix(matrix),
            'integrity': specific_string(8, hash_string(matrix_transpose_hash(matrix)))

        }
    else:
        return {
            'status': 'warning',
            'grid': reverse_matrix(matrix),
            'integrity': specific_string(8, hash_string(matrix_transpose_hash(matrix)))
        }

def _insert(parms):
    data = parms
    if 'cell' not in data.keys():
        return {
            'status': 'error: missing cell reference'
        }
   
    try:
        value = int(data['value'])
    except ValueError:
        return {
            'status': 'error: invalid value'
        }
    cell = data['cell']
    
    
   
    parts = cell.lower().split('c') 
    
    if len(parts) == 1:
        
        return {'status' : 'error: Invalid cell value'} 
    row_pos = int(parts[0][1:])
    col_pos = int(parts[1])
    if not (0<=row_pos<=15 and 0<=col_pos<=15):
        return {'status' : 'error: Invalid cell reference'}  
    try:
        grid = json.loads(data['grid'])
    except json.decoder.JSONDecodeError :
        return {'status' : 'error: Invalid grid'} 
    
    if type(grid) != list:
        return {'status' : 'error: Invalid grid'}
    if len(grid) != 153:
        return 'Grid must be of size 153'
    try:
        matrix = create_matrix(grid)
    except ValueError:
        return {
            'status': 'error: invalid grid value'
        }
    integrity = data['integrity']
    integrityString  = hash_string(matrix_transpose_hash(create_matrix(json.loads(data['grid']))))
    print(integrityString)
    if (integrity not in integrityString) or len(integrity)!=8:
         return {'status' : 'error: Invalid integrity'}
    response = check_for_insertion(matrix, row_pos-1, col_pos-1, value)
    print(grid)
    print(data)
    return response


