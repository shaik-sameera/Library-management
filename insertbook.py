#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages')
form=cgi.FieldStorage()

bn = form.getvalue('bookn')
ba = form.getvalue('booka')
bi = form.getvalue('bookid')


con=pymysql.connect(user='root',password='',host='localhost',
                                database='project')
cur=con.cursor()
sql = "INSERT INTO book(bookn,booka,bookid) VALUES(%s, %s, %s)"
val = (bn, ba, bi)
cur.execute(sql, val)
con.commit()
con.close()
print("data inserted into table successfully")




