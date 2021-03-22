## How to make an outgoing network connection
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("www.ucsd.edu", 80))		#Connect
s.send(b"GET / HTTP/1.0\r\n\r\n")	#Send request
data = s.recv(1024)					#Get response
print(data)
s.close()

