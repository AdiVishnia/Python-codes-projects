import socket

#TCP
ip="127.0.0.1"
port=8085
sTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sTCP.connect((ip,port))
sTCP.send(b"hello")
data=sTCP.recv(1024)
print(data)  

#UDP
sUDP=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sUDP.sendto(b"hello",(ip,port))

data,addrs=sUDP.recvfrom(1024)
print(data.decode())