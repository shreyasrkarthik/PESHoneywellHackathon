import socket
import sys
import os
import subprocess
import threading
import MySQLdb
def exception_hook(exception_type, value, traceback):
	main()
	
def insertRMAC(u_mac, router_mac):
	flag=0
	conn = MySQLdb.connect(host= "localhost", user="root", passwd="crap", db="Honeywell")
	cursor = conn.cursor()	
	try:
		cursor.execute("""SELECT user_name FROM umac_user_table WHERE u_mac=%s""",(u_mac))
		for (user_name) in cursor:
			username = user_name[0]
		print "username",username
		print "router_mac",router_mac
		cursor.execute("""INSERT INTO user_rmac_table VALUES (%s,%s)""",(username,router_mac))
		conn.commit()
		flag=1
	except:
		conn.rollback()
	conn.close()
	return flag

#main
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 3070)
	print 'starting up on %s port %s' % server_address
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#address reusability
	sock.bind(server_address)
	sock.listen(500)
	while True:
		print 'waiting for a connection'
		connection, client_address = sock.accept()
		print 'connection from', client_address
		print connection
		data = connection.recv(100).strip()
		connection.close()
		if data:
			print "Data",data
			user_mac,router_mac = data.split(",")
			print user_mac,router_mac 
			if(insertRMAC(user_mac, router_mac)==1):
				print("Successfully inserted <username,router_mac>")

sys.excepthook = exception_hook

if __name__ == '__main__':
	main()
