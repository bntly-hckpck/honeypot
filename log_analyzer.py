def log_analyzer():
    print('[INFO] [ANALYZER] reading "connections.log" file...')
    try:
        with open('connections.log') as connections_log:
            read_data = connections_log.read()
            total_connections = read_data.count("connection established")
            normal_disconnections = read_data.count("[INFO] [DISC] client disconnected")
            empty_connections = read_data.count("[WARNING] [DISC] client disconnected without sending data")
            connection_timeouts = read_data.count("[WARNING] [TIMEOUT] client inactive")
            socket_errors = read_data.count("[ERROR] [SOCKET]")
        
        print("[INFO] [ANALYZER] total connections: " + str(total_connections))
        print("[INFO] [ANALYZER] normal disconnections: " + str(normal_disconnections))
        print("[INFO] [ANALYZER] empty connections: " + str(empty_connections))
        print("[INFO] [ANALYZER] connection timeouts: " + str(connection_timeouts))
        print("[INFO] [ANALYZER] socket errors: " + str(socket_errors))

    except FileNotFoundError:
        print('[ERROR] [ANALYZER] "connections.log" file not found')


if __name__ == "__main__":
    log_analyzer()
