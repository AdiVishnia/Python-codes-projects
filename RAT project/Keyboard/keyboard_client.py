import socket
from pynput.keyboard import Controller, Key

host = '192.168.1.167'  # server IP address
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

keyboard = Controller()

while True:
    try:
        data = client_socket.recv(1024)
        if not data:
            break

        text = data.decode('utf-8', errors='ignore')

        if text.startswith("Key."):
            try:
                key = getattr(Key, text.split('.')[1])
                keyboard.press(key)
                keyboard.release(key)
            except AttributeError:
                print(f"Unknown key: {text}")
        else:
            keyboard.type(text)

    except Exception as e:
        print("Client error:", e)
        break

client_socket.close()