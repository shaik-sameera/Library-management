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
mycursor.execute("CREATE TABLE book(bookn VARCHAR(25), booka VARCHAR(25), bookid VARCHAR(30))")
mydb.commit()
print("table created successfully")
mydb.close()
