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
        print("[INFO] listening on " + HOST + ":" + str(PORT))
        while True:
            client_socket, client_address = server.accept()
            with client_socket:
                print("[INFO] connection established")
                conn_start_ts = timestamp()
                start_time = datetime.datetime.now(datetime.timezone.utc)
                with open("connections.log", "a", encoding="utf-8") as log:
                    log.write(
                        "[INFO] " + conn_start_ts
                        + " connection established | ip: " + client_address[0]
                        + " | port: " + str(client_address[1])
                        + "\n"
                    )
                print("ip: " + client_address[0])
                print("port: " + str(client_address[1]))
                print("timestamp: " + conn_start_ts)
                total_bytes = 0
                while True:
                    data = client_socket.recv(1024)
                    total_bytes += len(data)
                    if not data:
                        conn_end_ts = timestamp()
                        end_time = datetime.datetime.now(datetime.timezone.utc)
                        conn_duration = (end_time - start_time)
                        print("[INFO] client disconnected")
                        with open("connections.log", "a", encoding="utf-8") as log:
                            log.write(
                                "[INFO] " + conn_end_ts
                                + " client disconnected | ip: " + client_address[0]
                                + " | port: " + str(client_address[1])
                                + " | connection duration: " + str(conn_duration).split(".")[0]
                                + " | total bytes received: " + str(total_bytes)
                                + "\n"
                            )
                        print("timestamp: " + conn_end_ts)
                        print("connection duration: " + str(conn_duration).split(".")[0])
                        print("total bytes received: " + str(total_bytes))
                        break
                    print("[INFO] " + str(len(data)) + " bytes received")
                    client_socket.sendall(data)
    except socket.error as error:
        print("[ERROR] " + str(error))
        return
    finally:
        server.close()


def timestamp():
    utc_dt = datetime.datetime.now(datetime.timezone.utc)
    log_dt = utc_dt.strftime("%d-%m-%Y %H:%M:%S UTC+0")
    return log_dt


if __name__ == "__main__":
    start_server()
