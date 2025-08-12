import socket

def send_file():
    try:
        client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        #send file name
        client_socket.send(("text.txt"+ "\n").encode("utf-8"))
        #send file data
        with open(file_name, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)
        #shutdown the write side of the socket
        client_socket.shutdown(socket.SHUT_WR)  
        print("File sent successfully.")
        #receive response from server that the file data was received
        response = client_socket.recv(1024).decode("utf-8") 
        print("Server response:", response) 
    except Exception as e:
        print("Error occurred while sending the file:", str(e))
    finally:
        client_socket.close()

if __name__ =="__main__":
    host="127.0.0.1"
    port=12345
    file_name= r"D:\python codes\Project Server-Client\text.txt"
    send_file()