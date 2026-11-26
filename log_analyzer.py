def log_analyzer():
    print("[INFO] [ANALYZER] reading connections.log...")
    try:
        with open('connections.log') as connections_log:
            read_data = connections_log.read()
            total_connections = read_data.count("connection established")
            print("[INFO] [ANALYZER] total connections: " + str(total_connections))
    except FileNotFoundError:
        print('[ERROR] [ANALYZER] "connections.log" not found')


if __name__ == "__main__":
    log_analyzer()
