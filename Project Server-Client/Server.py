import socket
import os
def recive_one_file():
    try:
        server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host,port))
        server_socket.listen(1)
        print("Waiting for connections...")
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        file_name= client_socket.recv(1024).decode("utf-8").strip()
        print(f"Receiving file: {file_name}")
        file_data = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file_data += data

    except Exception as e:
        print("Error occured while setting up the server:",str(e))
        return None
    finally:
        try:
            client_socket.close()
        except Exception:
            pass

if __name__ =="__main__":
    host="127.0.0.1"
    port=12345
    save_dir = r"D:\python codes\Project Server-Client"