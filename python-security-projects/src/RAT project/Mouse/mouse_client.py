import win32api, win32con
import socket

host = '192.168.1.167'  # server IP address
port = 12346 #different port than keyboard server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

while True:
    try:
        data = client_socket.recv(1024)
        if not data:
            break

        command = data.decode('utf-8', errors='ignore')
        parts = command.split(',')
        action = parts[0]

        if action == "move":
            x=int(parts[1].replace("move",""))
            y=int(parts[2].replace("move",""))
            win32api.SetCursorPos((x, y))

        if action == "press":
            button = parts[1]#left or right
            if button == "left":
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            elif button == "right":
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

        if action == "release":
            button = parts[1]#left or right
            if button == "left":
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            elif button == "right":
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

        if action == "scroll":
            dy = int(parts[1].replace("scroll",""))
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,dy*120)

    except Exception as e:
        print("Client error:", e)

client_socket.close()
