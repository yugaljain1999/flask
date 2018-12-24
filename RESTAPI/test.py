# This whole database will be used to store the username,password and contents inside the username,password like get,post requests
import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
# Here name of table that we created is users in which we are creating id,username and password of user
create_table="CREATE TABLE users(id int,username text,password text)"
cursor.execute(create_table)
user=[(1,'abcd','password'),
        (2,'def','pass'),
        (3,'ghi','word')]
insert_query="INSERT INTO users VALUES(?,?,?)"
cursor.executemany(insert_query,user)





# Now we will retrieve the columns from database i.e id,name and password
select_query="SELECT password FROM users"
for i in cursor.execute(select_query): # Here we are printing three rows which contains three columns named id,username and password
    print(i)
connection.commit()
connection.close()
