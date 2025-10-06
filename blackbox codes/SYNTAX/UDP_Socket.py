import socket

ip="127.0.0.1"
port=12345

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"hello", (ip, port))  # שליחת הודעה לכתובת ופורט מסוימים

received_message, addr = s.recvfrom(1024)
print(received_message.decode())  # פיענוח ל-str
print(addr) # הדפסת הכתובת והפורט של השולח