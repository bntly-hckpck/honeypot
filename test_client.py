import socket

HOST = "127.0.0.1"
PORT = 8081

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
        print("[INFO] [CLIENT] connected to " + HOST + ":" + str(PORT))
    except ConnectionRefusedError as error:
        print("[ERROR] [CLIENT] " + str(error))
    except ConnectionError as error:
        print("[ERROR] [CLIENT] " + str(error))
            
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
