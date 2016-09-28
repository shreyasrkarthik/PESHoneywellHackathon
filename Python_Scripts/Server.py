import socket
import sys
import os
import subprocess
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 3070)
print 'starting up on %s port %s' % server_address

sock.bind(server_address)

sock.listen(1)
while True:
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    print 'connection from', client_address
    print connection
    while True:
        data = connection.recv(100).strip()
        print  'received "%s"' % data