import sqlite3
from flask import Flask

app = Flask(__name__)

'''
db connection setup for sqlite
connect function will create hospital.db file if not created 
if hospital.db file is created it will just connect to that
for more infomation about sqlite with python refer this
https://www.tutorialspoint.com/sqlite/sqlite_python.htm
'''
def get_db_conection():
    db_conn = sqlite3.connect('hospital.db', check_same_thread=False)
    return db_conn

from views.view import *
