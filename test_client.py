import socket
import datetime

HOST = "127.0.0.1"
PORT = 8081

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection_status = False
    
    try:
        client.connect((HOST, PORT))
        print("[INFO] [CLIENT] connected to " + HOST + ":" + str(PORT))
        start_time = datetime.datetime.now(datetime.timezone.utc)
        connection_status = True
    except ConnectionRefusedError as error:
        print("[ERROR] [CLIENT] " + str(error))
    except ConnectionError as error:
        print("[ERROR] [CLIENT] " + str(error))
            
    finally:
        client.close()
        if connection_status == True:
            print("[INFO] [CLIENT] disconnected")
            end_time = datetime.datetime.now(datetime.timezone.utc)
            conn_duration = (end_time - start_time)
            print("[INFO] [CLIENT] connection duration: " + str(conn_duration))


if __name__ == "__main__":
    start_client()
