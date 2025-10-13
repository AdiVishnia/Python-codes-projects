import socket
from pynput.mouse import Listener, Button

host = '0.0.0.0' # listen on all interfaces
port = 12346 #different port than keyboard server and screen server

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"TCP Server is listening on {host}:{port} for mouse capture")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

def on_click(x, y, button, pressed):
    try:
        if pressed and button == Button.left:
            message = "press,left".encode('utf-8')
            client_socket.send(message)
        elif not pressed and button == Button.left:
            message = "release,left".encode('utf-8')
            client_socket.send(message)
        elif pressed and button == Button.right:
            message = "press,right".encode('utf-8')
            client_socket.send(message)
        elif not pressed and button == Button.right:
            message = "release,right".encode('utf-8')
            client_socket.send(message)
    except Exception as e:
        print("Send failed:", e)

def on_move(x,y):
    try:
        message = f"move,{x},{y}".encode('utf-8')
        client_socket.send(message)
    except Exception as e:
        print("Error:", e)

def on_scroll(x, y, dx, dy):
    try:
        if dy != 0:
            message = f"scroll,{dy}".encode('utf-8')
            client_socket.send(message)
    except Exception as e:
        print("Error:", e)

with Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll) as listener:
    listener.join()

client_socket.close()
server_socket.close()
