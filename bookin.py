#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages')
form=cgi.FieldStorage()

bname = form.getvalue('bookname')
aname = form.getvalue('aname')
bid = form.getvalue('bookid')


con=pymysql.connect(user='root',password='',host='localhost',
                                database='project')
cur=con.cursor()
sql = "INSERT INTO addb(bookname,aname,bookid) VALUES(%s, %s, %s)"
val = (bname, aname, bid)
cur.execute(sql, val)
con.commit()
con.close()
print("data inserted into table successfully")

