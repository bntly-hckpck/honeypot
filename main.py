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
            print("[CONNECTION ESTABLISHED]")
            print("ip: " + client_address[0])
            print("port: " + str(client_address[1]))
            print("timestamp: " + timestamp())
            start_time = datetime.datetime.now(datetime.timezone.utc)
            total_bytes = 0
            while True:
                data = client_socket.recv(1024)
                total_bytes += len(data)
                if not data:
                    print("[CLIENT DISCONNECTED]")
                    print("timestamp: " + timestamp())
                    end_time = datetime.datetime.now(datetime.timezone.utc)
                    conn_duration = (end_time - start_time)
                    print("connection duration: " + str(conn_duration).split(".")[0])
                    print("total bytes received: " + str(total_bytes))
                    break
                print(str(len(data)) + " bytes received")
                client_socket.sendall(data)
    except socket.error as error:
        print("[ERROR]\n" + str(error))
        return
    finally:
        server.close()


def timestamp():
    utc_dt = datetime.datetime.now(datetime.timezone.utc)
    log_dt = utc_dt.strftime("%d-%m-%Y %H:%M:%S UTC+0")
    return log_dt


if __name__ == "__main__":
    start_server()
