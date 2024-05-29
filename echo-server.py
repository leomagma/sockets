"""
	A simple Implementation of a socket API server
	This Server echo whatever  it will recieve from the client
	author:Bishel
	mail_to:vampirepc2@gmail.com
	
"""

import socket 

HOST = "127.0.0.1" #Standard loopback interface address
PORT = 65432  # port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
	soc.bind((HOST,PORT))
	soc.listen() #listens for connections
	conn, addr = soc.accept()
	with conn:
		print(f'Connected by:{addr}')
		while True:
			data =  conn.recv(1024)
			if not data:
				break
			conn.sendall(data) # send back the data it recv_d
 
