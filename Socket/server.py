#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 8084
BUFSIZ = 1024
ADDR = (HOST, PORT)

sS = socket(AF_INET, SOCK_STREAM)
sS.bind(ADDR)
sS.listen(5)

while True:
	print 'waiting for connecting...'
	cS, addr = sS.accept()
	print '...connected from', addr
	
	while True:
		msg = raw_input('> ')
		cS.send(msg)
		
		msg = cS.recv(BUFSIZ)
		print ('<Son>: ' + msg)
		if not msg:
			break
	
	cS.close()
sS.close()