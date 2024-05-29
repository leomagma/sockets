"""

	author:Bishel
	mail_to:vampirepc2@gmail.com
"""

import socket

HOST= '127.0.0.1'
PORT= 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
	soc.connect((HOST,PORT)) 
	soc.sendall(b"Hello, World!! this is Bishel")
	data = soc.recv(1024)

print ('Recieved : {}'.format(data))

