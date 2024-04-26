#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\program files (x86)\python38-32\lib\site-packages');
import cgi, cgitb
import pymysql


mydb=pymysql.connect(host="localhost",user="root",password="",database="project")
mycursor=mydb.cursor()
cgitb.enable() 
form=cgi.FieldStorage()
se = form.getvalue('search')
sql="SELECT * FROM regtable1 WHERE fname=%s"
val = (se,)
mycursor.execute(sql, val)
result=mycursor.fetchall()
print(result)

print("<table border='1'>")
for rows in result:
    print("<tr><td>")
    print(rows)
    print("</td></tr>")
print("</table>")
