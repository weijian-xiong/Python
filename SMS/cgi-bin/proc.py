#!/usr/bin/python

import cgi, cgitb 
import smtplib
import urllib

form = cgi.FieldStorage() 

addr = form.getvalue('addr')
message  = form.getvalue('msg')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>SMS email program</title>"
print "</head>"
print "<body>"
print "SMS email address = %s" % (addr)
print "</br>"
print "Message = %s" % (message)
print "</br>"
print "</body>"
print "</html>"

decode_msg = urllib.unquote(message)

gmail_user = 'YourEmail@gmail.com'  
gmail_password = 'YourPassword'

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, addr, decode_msg)
server.quit()

print('SMS message: \n', decode_msg)

