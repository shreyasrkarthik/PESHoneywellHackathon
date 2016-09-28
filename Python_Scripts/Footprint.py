import socket
import sys
import os
import subprocess
import threading
# from apscheduler.scheduler import Scheduler

s = ""
User_MAC = ""
def connect():
	global User_MAC
	global s
	User_MAC = getMacAddress()	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	#host = socket.gethostname()
	server_address = ('localhost', 3070)
	print 'connecting to %s port %s' % server_address
	try:
		s.connect(server_address)
		sendMAC()
	except Exception as inst:
		print inst

def sendMAC():
	# os.system("ip route list | awk 'FNR == 1 {print $3}'")
	direct_output = subprocess.check_output("ip route list | awk 'FNR == 1 {print $3}'", shell=True)	
	ARPCommand = "arp "  + direct_output.strip() + " | awk 'FNR == 2 {print $3}'"
	# print ARPCommand 
	MACAddress  = (subprocess.check_output(ARPCommand, shell=True)).strip()
	# print MACAddress
	global User_MAC
	data = User_MAC + "," + MACAddress
	try:
		print 'sending "%s"' % data
		s.sendall(data)
	except Exception as inst:
		print inst
	threading.Timer((60.0 * 1), sendMAC).start()

def getMacAddress(): 
    if sys.platform == 'win32': 
        for line in os.popen("ipconfig /all"): 
            if line.lstrip().startswith('Physical Address'): 
                mac = line.split(':')[1].strip().replace('-',':') 
                break 
    else: 
        for line in os.popen("/sbin/ifconfig"): 
            if line.find('Ether') > -1: 
                mac = line.split()[4] 
                break 
    return mac    


if __name__ == '__main__':
	connect()
