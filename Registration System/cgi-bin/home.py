#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

print """
<html>
<head><title>Registration System</title></head>
<body>
<div align="center">
  <center>
  <table border="3" width="430" height="112">
  <tr><td width="430" height="168">
  <p align="center">
  <b><font color="green" size="6">Registration System</font></b><br>
  </td></tr>
  <tr><td width="430" height="41">
  <p align="center">
  <b><a href="/cgi-bin/regist.py">
     <font color="red" size="5">Start</font>
  </a></b>
  </td></tr>
  </table>
  </center>
</div>
<p align="center">
</body>
</html>"""