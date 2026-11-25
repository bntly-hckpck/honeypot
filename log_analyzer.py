def log_analyzer():
    print("[INFO] [ANALYZER] reading connections.log...")
    try:
        with open('connections.log') as connections_log:
            read_data = connections_log.read()
            print(read_data)
    except FileNotFoundError:
        print('[ERROR] [ANALYZER] "connections.log" not found')


if __name__ == "__main__":
    log_analyzer()
