#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages')
mydb=pymysql.connect(
	host="localhost",
	user="root",
	password="")

m = mydb.cursor()
m.execute("CREATE DATABASE project")
print("database created successfully")
