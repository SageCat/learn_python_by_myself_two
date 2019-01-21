#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sage Guo
import mysql.connector

if __name__ == '__main__':
	conn = mysql.connector.connect(user='root', password='123456', database='sage_test')
	cursor = conn.cursor()
	cursor.execute('SHOW TABLES')
	print(cursor.fetchall())
	cursor.execute('SELECT * FROM cityCode')
	print(cursor.fetchall())
	print(cursor.column_names)
	print(cursor.with_rows)
	cursor.close()
	conn.close()
