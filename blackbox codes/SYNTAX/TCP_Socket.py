import socket

ip="127.0.0.1"
port=12345

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
s.send(b"hello")  # לשלוח bytes
received_message = s.recv(1024)
print(received_message.decode())  # מומלץ לפענח ל-str