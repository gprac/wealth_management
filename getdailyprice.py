#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
tablenames = cursor.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
products = cursor.execute("select id, code, type from product_product").fetchall()
for row in products:
	if row[2] == 'F':
		print(row[1])


tablestruct = cursor.execute('PRAGMA table_info(product_product)').fetchall()
print(tablestruct)