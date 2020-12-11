#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import smtplib
import pymysql

cgitb.enable()
form = cgi.FieldStorage()

name = form.getvalue('name')
email  = form.getvalue('email')
phone_number  = form.getvalue('phone_number')
confirm = form.getvalue('confirm')
ATT_phone_number = phone_number+"@txt.att.net"

if confirm=="Yes":
    print """
    <table ALIGN=CENTER BORDER=1 CELLSPACING=1 CELLPADDING=1>
    <tr VALIGN=TOP><td><pre><font size="5">
    Registration Successful

        Thanks!
    <a href="/cgi-bin/regist.py">Register Another.</a>
    <a href="/cgi-bin/home.py">Back To Home Page</a>
    </font></pre></td></tr></table>"""

    gmail_user = 'im.xwjian@gmail.com'  
    gmail_password = 'Getr1ch$'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, ATT_phone_number, "Registration Successful!")
    server.quit()

    db = pymysql.connect("localhost","root","password","test" )

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    create_table = """CREATE TABLE STUDENT (
    NAME  VARCHAR(30) NOT NULL,
    EMAIL  VARCHAR(30),
    PHONE_NUMBER VARCHAR(15) )"""
    insert_data = "INSERT INTO STUDENT(NAME, EMAIL, PHONE_NUMBER) VALUES ('%s', '%s', '%s')" % (name, email,phone_number)
    try:
    # Execute the SQL command
        cursor.execute(create_table)
        cursor.execute(insert_data)
    # Commit your changes in the database
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

elif confirm=="No":
    print """
    <table ALIGN=CENTER BORDER=1 CELLSPACING=1 CELLPADDING=1 >
    <tr VALIGN=TOP><td><pre>
    <font size="5">
    So, The Information Is Incorrect.

        <a href="/cgi-bin/regist.py">Please Register Again</a>

        <a href="/cgi-bin/home.py">Back To Home Page</a>
    </font></pre></td></tr></table>"""
