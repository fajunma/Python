# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

import sqlite3
from random import *
conn=sqlite3.connect('test.db')
cur=conn.cursor()
# try:
#     cur.execute('CREATE TABLE tableTest(field1 numeric, field2 text)')
# except:
#     pass
# t='abcd'
# data=zip([random() for x in range(len(t))],t)
# cur.executemany('INSERT INTO tableTest values(?,?)',data)
#cur.execute('DROP TABLE tableTest')
cur.execute('SELECT * FROM tableTest ORDER BY field2 DESC')
for rec in cur.fetchall():
    print(rec)
