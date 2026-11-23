import socket
import datetime

HOST = "127.0.0.1"
PORT = 8081

def start_client():
    test_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection_status = False
    print("[INFO] [CLIENT] client started...")
    try:
        test_client.connect((HOST, PORT))
        print("[INFO] [CONN] client connected to " + HOST + ":" + str(PORT))
        start_time = datetime.datetime.now(datetime.timezone.utc)
        connection_status = True
        user_input = input()
        test_client.sendall(user_input.encode())
        print('[INFO] [SEND] client sent message "' + user_input + '" to server')
        data = test_client.recv(1024)
        message = data.decode(encoding='utf-8', errors='strict')
        print('[INFO] [RECV] client received message "' + message + '" from server')
        
    except ConnectionRefusedError as error:
        print("[ERROR] [CLIENT] " + str(error))
    except ConnectionError as error:
        print("[ERROR] [CLIENT] " + str(error))
            
    finally:
        test_client.close()
        if connection_status == True:
            print("[INFO] [DISC] client disconnected")
            end_time = datetime.datetime.now(datetime.timezone.utc)
            conn_duration = (end_time - start_time)
            print("[INFO] [CLIENT] connection duration: " + str(conn_duration))


if __name__ == "__main__":
    start_client()
