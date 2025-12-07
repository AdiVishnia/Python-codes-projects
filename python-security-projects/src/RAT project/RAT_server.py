import threading
import socket


def run_keyboard_server():
    # Copied from Keyboard/keyboard_server.py
    from pynput.keyboard import Listener

    host = '0.0.0.0'  # listen on all interfaces
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

    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    finally:
        try:
            client_socket.close()
        except Exception:
            pass
        try:
            server_socket.close()
        except Exception:
            pass


def run_mouse_server():
    # Copied from Mouse/mouse_server.py
    from pynput.mouse import Listener, Button

    host = '0.0.0.0'  # listen on all interfaces
    port = 12346  # different port than keyboard server and screen server

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

    def on_move(x, y):
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

    try:
        with Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll) as listener:
            listener.join()
    finally:
        try:
            client_socket.close()
        except Exception:
            pass
        try:
            server_socket.close()
        except Exception:
            pass


def run_screen_server():
    # Copied from Screen/screen_server.py
    from io import BytesIO
    from PIL import Image, ImageTk
    import tkinter as tk

    host = '0.0.0.0'  # listen on all interfaces
    port = 12347  # different port than keyboard server and mouse server

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
    root.config(cursor='none')  # hide current mouse pointer

    latest_frame = {'imgtk': None}

    def refresh():
        if latest_frame['imgtk'] is not None:
            label.config(image=latest_frame['imgtk'])
        root.after(16, refresh)  # ~60 FPS

    def receive_once():
        try:
            data, addr = server_socket.recvfrom(BUFFER_SIZE)
            img = Image.open(BytesIO(data)).convert('RGB')
            latest_frame['imgtk'] = ImageTk.PhotoImage(img)
        except Exception:
            pass
        finally:
            root.after(16, receive_once)  # ~60 FPS

    #GUI loop
    root.after(0, refresh)
    root.after(0, receive_once)
    try:
        root.mainloop()
    finally:
        server_socket.close()


def main():
    # Start keyboard and mouse servers in background threads
    keyboard_thread = threading.Thread(target=run_keyboard_server, name='KeyboardServer', daemon=True)
    mouse_thread = threading.Thread(target=run_mouse_server, name='MouseServer', daemon=True)

    keyboard_thread.start()
    mouse_thread.start()

    # Run screen server on the main thread (Tkinter prefers main thread)
    run_screen_server()


if __name__ == '__main__':
    main()


