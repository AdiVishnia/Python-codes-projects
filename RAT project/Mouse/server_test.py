import socket
from pynput import mouse
#TEST CODE FOR MOUSE
host = '0.0.0.0'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        try:
            message = "click,left".encode('utf-8')
            client_socket.send(message)
        except Exception as e:
            print("Send failed:", e)


# Listen for mouse events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

client_socket.close()
server_socket.close()