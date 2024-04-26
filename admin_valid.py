#!C:\Program Files (x86)\Python38-32\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\dell\\appdata\\roaming\\python\\python38\\site-packages')



import cgi, cgitb
import pymysql



cgitb.enable()
mydb=pymysql.connect(user='root',password='',host='localhost',database='project')


mycursor=mydb.cursor()
form=cgi.FieldStorage()

user=form.getvalue('admin')

pass1=form.getvalue('apassword')

if user=='necadmin' and pass1=='shshd':

        print("<h2 style='color:green;margin-left:550px;'>Login Successfully...</h2>")
        #print("<h2 style='color:green;margin-left:550px;'>Welcome,"+row[0]+"</h2>")
        print("<h2 style=margin-left:550px;><a href=admin_home.html>Click here to go to home page</a></h2>")
else:
    print("please check you user and password")
