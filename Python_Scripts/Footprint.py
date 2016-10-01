import socket
import sys
import os
import subprocess
import threading
import re

s = ""
User_MAC = ""
iswlan = 0
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
	global iswlan
	iswlan = 0
	if sys.platform == 'win32':
<<<<<<< HEAD
		try:
			direct_output = str(subprocess.check_output('netsh wlan show interfaces|findstr SSID', shell = True))
			if(direct_output!=null and direct_output!=None):
				#wlan
				iswlan = 1
				valid_bssid = re.findall( r'(?:[A-Fa-f0-9]{2}[:-]){5}(?:[A-Fa-f0-9]{2})', direct_output)[0]#mac
				valid_ssid = (direct_output.split("\\")[0]).split(':')[1].strip()#wifi name
				MACAddress = valid_ssid
			else: 
				#eth0
				direct_output = str(subprocess.check_output('ipconfig | findstr "Default Gateway"', shell = True))
				valid_ip = ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', direct_output)	
				ARPCommand = "ARP -a "  + valid_ip[0]
				MACAddress  = (subprocess.check_output(ARPCommand, shell=True))
				MACAddress  = re.findall(r'(?<!-)(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?!-)',MACAddress)[0].replace('-',":")							
		except Exception, e:
			pass
		
	else:
		try:
		 	if(str(subprocess.check_output("route | awk 'FNR == 3 {print $8}'", shell = True)).strip() == "wlan0"):
				iswlan = 1
				#User Essid but named as MACAddress
				ESSID = subprocess.check_output('iwlist wlan0 scanning | grep ESSID',shell = True).strip().split()[0]
				MACAddress = ESSID.split(':')[1]

			else:
				direct_output = str(subprocess.check_output("ip route list | awk 'FNR == 1 {print $3}'", shell=True))			
				ARPCommand = "arp "  + direct_output.strip() + " | awk 'FNR == 2 {print $3}'"
				MACAddress  = (subprocess.check_output(ARPCommand, shell=True)).strip()

		except Exception, e:
		 	raise e 
		
=======
		if(subprocess.check_output('', shell = True)== 'wlan0'):
			iswlan = 1
			#Your code here
		else: 
			direct_output = subprocess.check_output('ipconfig | findstr "Default Gateway"', shell = True)
			valid_ip = ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', direct_output)	
			ARPCommand = "ARP -a "  + valid_ip[0]
			MACAddress  = (subprocess.check_output(ARPCommand, shell=True))
			MACAddress  = re.findall(r'(?<!-)(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?!-)',MACAddress)[0].replace('-',":")

	else: 
		if(subprocess.check_output("route | awk 'FNR == 3 {print $8}'", shell = True).strip() == "wlan0"):
			iswlan = 1
			#User Essid but named as MACAddress
			ESSID = subprocess.check_output('iwlist wlan0 scanning | grep ESSID',shell = True).strip().split()[0]
			MACAddress = ESSID.split(':')[1]

		else:
			direct_output = subprocess.check_output("ip route list | awk 'FNR == 1 {print $3}'", shell=True)			
			ARPCommand = "arp "  + direct_output.strip() + " | awk 'FNR == 2 {print $3}'"
			MACAddress  = (subprocess.check_output(ARPCommand, shell=True)).strip()
>>>>>>> f3cbe693e475e7217f7103c1e8273acc2d380b0b
	global User_MAC
	data = User_MAC + "," + MACAddress
	try:
		print 'sending "%s"' % data
		s.sendall(data)
	except Exception as inst:
		print inst
	threading.Timer((60.0 * 1), connect).start()

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
