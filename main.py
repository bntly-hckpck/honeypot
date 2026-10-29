import socket

HOST = "127.0.0.1"
PORT = 8081


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(6)
        print(f"listening on {HOST}:{PORT}...")
    except socket.error as error:
        print(f"error:\n{error}")
        return
    finally:
        server.close()


if __name__ == "__main__":
    start_server()
