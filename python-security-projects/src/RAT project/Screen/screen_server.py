import socket
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk

host = '0.0.0.0' # listen on all interfaces
port = 12347 # different port than keyboard server and mouse server

BUFFER_SIZE = 65535  # Max UDP datagram size

# Socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))
print(f"UDP server is listening on {host}:{port} for screen capture")

# GUI setup
root = tk.Tk()
root.title('Remote Screen')
label = tk.Label(root)
label.pack()
root.config(cursor='none') #hide current mouse pointer

latest_frame = { 'imgtk': None }

def refresh():
    if latest_frame['imgtk'] is not None:
        label.config(image=latest_frame['imgtk'])
    root.after(16, refresh)  # 60 FPS
def receive_once():
    try:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        img = Image.open(BytesIO(data)).convert('RGB')
        latest_frame['imgtk'] = ImageTk.PhotoImage(img)
    except Exception:
        pass
    finally:
        root.after(16, receive_once)  # 60 FPS

# Start receiving (blocking) and the GUI loop
root.after(0, refresh)
root.after(0, receive_once)
try:
    root.mainloop()
finally:
    server_socket.close()