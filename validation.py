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

user=form.getvalue('uname')

pass1=form.getvalue('password')




mycursor.execute("select * from regtable1")


result=mycursor.fetchall()


userlist=[]


for row in result:
    userlist.append(row[2])

    

if user in userlist:
    i=userlist.index(user)
    row=result[i]
    
    if (row[3]==pass1):
        print("<h2 style='color:green;margin-left:550px;'>Login Successfully...</h2>")
        print("<h2 style='color:green;margin-left:550px;'>Welcome,"+row[0]+"</h2>")
        print("<h2 style=margin-left:550px;><a href=homepage.html>Click here to go to home page</a></h2>")
    else:
        print("please check you user and password")
      
         
else:
    print("you are not register to our website, please register!")
