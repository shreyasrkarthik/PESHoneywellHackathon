import socket
import sys
import os
import subprocess
import threading
import MySQLdb

def insertRMAC(u_mac, router_mac):
	conn = MySQLdb.connect(host= "localhost", user="root", passwd="crap", db="Honeywell")
	cursor = conn.cursor()	
	try:
		cursor.execute("""SELECT user_name FROM umac_user_table WHERE u_mac=%s""",(u_mac))
		for (user_name) in cursor:
			username = user_name[0]
		cursor.execute("""INSERT INTO user_rmac_table VALUES (%s,%s)""",(username,router_mac))
		conn.commit()
	except:
		conn.rollback()
	conn.close()
	return 1

#main
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 3070)
print 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(500)
while True:
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    print 'connection from', client_address
    print connection
    data = connection.recv(100).strip()
    connection.close()    
    if(data is not None):
		user_mac,router_mac = data.split(",")
		print user_mac,router_mac 
		# if(insertRMAC(user_mac, router_mac)==1):
			# print("Successfully inserted <username,router_mac>")
	
