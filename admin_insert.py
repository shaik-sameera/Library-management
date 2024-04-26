#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages')
form=cgi.FieldStorage()

ad = form.getvalue('admin')
aps = form.getvalue('apassword')

con=pymysql.connect(user='root',password='',host='localhost',
                                database='project')
cur=con.cursor()
sql = "INSERT INTO (admin,apassword) VALUES(%s, %s)"
val = (ad, aps)
cur.execute(sql, val)
con.commit()
con.close()
print("data inserted into table successfully")
