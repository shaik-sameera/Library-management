#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages')
form=cgi.FieldStorage()

fn = form.getvalue('fname')
ln = form.getvalue('lname')
em = form.getvalue('email')
ps = form.getvalue('password')
cps = form.getvalue('conpassword')

con=pymysql.connect(user='root',password='',host='localhost',
                                database='project')
cur=con.cursor()
sql = "INSERT INTO regtable1(fname,lname,email,password,conpassword) VALUES(%s, %s, %s, %s, %s)"
val = (fn, ln, em, ps, cps)
cur.execute(sql, val)
con.commit()
con.close()
print("data inserted into table successfully")



