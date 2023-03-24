import mysql.connector

mydb =  mysql.connector.connect(user='root', password='1234', host='localhost',port=3306, database='details', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
	print(i)
    
    
#####

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

for i in result:
    print(i)
    
######

import mysql.connector

mydb = mysql.connector.connect(user='root', password='1234',database='details', host='localhost',port=3306, auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()
# result = mycursor.fetchone()

for i in result:
	print(i)