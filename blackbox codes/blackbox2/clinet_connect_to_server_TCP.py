import socket

ip = "127.0.0.1"
port = 8543  # מספר שלם, לא מחרוזת

s = socket.socket()
s.connect((ip, port))  #עם שני הערכים tuple שמים
print("Connected!")