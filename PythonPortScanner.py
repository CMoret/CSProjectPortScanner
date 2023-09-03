#This program scans the port entered, successfully registers connections along with ending program if host IP is blocking port 

import socket
import sys
from datetime import datetime

print("Python Port Scanner")

target_ip = input(str("\nTarget IP: "))

print("\nScanning Target: " + target_ip)
print("Scanning Started: " + str(datetime.now()))


try:
#Attemps to find ports
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.10)

#Results for open ports, 0 = successsful connection
        results= s.connect_ex((target_ip, port))
        if results == 0:
            print("[**] Port {} is open" .format(port))
        s.close()

#Program  exiciting
except KeyboardInterrupt:
        print("\n Leaving Program. ")
        sys.exit()

##Unable to receive response from host IP entered
except socket.error:
        print("\n Host IP unable to respond.")
        sys.exit()

print("Scanning Ended: "+ str(datetime.now()))        
print("Program is complete. Goodbye now!")