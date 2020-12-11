#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
email  = form.getvalue('email')
phone_number  = form.getvalue('phone_number')

print """
<html>
<center><font color="red" size ="7">Registration Form</font><br>

<table align=center datasrc="#xmlRegData" border=2>
<tr><td><font color="black" size="5">Name:</font></td>"""
print "<td>%s </td> " %(name)
print """</tr><tr><td><font color="black" size="5">Email:</font></td>"""
print" <td>%s</td>" % (email)
print """</tr><tr><td><font color="black" size="5">ATT Phone Number:</font></td>"""
print" <td>%s</td>" % (phone_number)
print """</tr>
</table><br>

<font size="5">Is this information correct ?</font>

<form action="/cgi-bin/confirm.py" method=GET>
<input type="hidden" id="name" name="name" value="%s">
<input type="hidden" id="email" name="email" value="%s">
<input type="hidden" id="phone_number" name="phone_number" value="%s">
<input type=submit value="Yes" name=confirm>
<input type=submit value="No" name=confirm>  
</form>
</center>
</html>""" % (name,email,phone_number)