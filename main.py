import socket

HOST = "127.0.0.1"
PORT = 8081


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        client_socket, client_address = server.accept()
        with client_socket:
            print(f"Connected by {client_address}")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                client_socket.sendall(data)
    except socket.error as error:
        print(f"error:\n{error}")
        return
    finally:
        server.close()


if __name__ == "__main__":
    start_server()
