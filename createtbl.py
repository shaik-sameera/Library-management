#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages')
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE regtable1(fname VARCHAR(25), lname VARCHAR(25), email VARCHAR(30), password VARCHAR(20), conpassword VARCHAR(20))")
mydb.commit()
print("table created successfully")
mydb.close()
