# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:34:51 2019

@author: 612436112
"""

### SQLite #### 

### Task 1 #### 

import sqlite3 as sql

conn= sql.connect("task1.db") 
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)") 

def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()