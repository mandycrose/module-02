# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:04:11 2019

@author: 612436112
"""
## task 2 ## 

import sqlite3
import time
import datetime
import random

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword,value) VALUES (?, ?, ?, ?)', (unix,date, keyword,value))
    conn.commit()
    
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()