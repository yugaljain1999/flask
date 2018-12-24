import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
create_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"
create_table="CREATE TABLE IF NOT EXISTS items(name text,price real)" #Here we have created table for items and here real is for decimal numbers
cursor.execute(create_table)
connection.commit()
connection.close()
