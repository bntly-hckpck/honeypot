import socket
import datetime

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
            print("connection established:")
            print(f"ip: {client_address[0]}")
            print(f"port: {client_address[1]}")
            utc_dt = datetime.datetime.now(datetime.timezone.utc)
            log_dt = utc_dt.strftime("%d-%m-%Y %H:%M:%S UTC+0")
            print("timestamp:", log_dt)
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
