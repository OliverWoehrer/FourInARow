import socket

HOST = '10.232.11.194'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def main() :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print ('Test')
        s.sendall(b'Hello, world')
        data = s.recv(3)
        print('Received', repr(data))
        exit()


if __name__ == "__main__":
    main()