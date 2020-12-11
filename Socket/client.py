#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 8084
BUFSIZ = 1024
ADDR = (HOST, PORT)

cS = socket(AF_INET, SOCK_STREAM)
cS.connect(ADDR)

while True:

	msg = cS.recv(BUFSIZ)
	if not msg:
		brean
	print ('<Mom>: ' + msg)
	
	msg = raw_input('> ')
	if not msg:
		break
	cS.send(msg)
	
cS.close()