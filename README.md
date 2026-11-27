# honeypot

A lightweight TCP honeypot written in Python for learning network security, connection monitoring, and threat analysis.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## Features

- [x] TCP server (single-client echo server)
- [x] Connection monitoring (IP, port, timestamps, duration)
- [x] Event logging to `connections.log`
- [x] Client inactivity timeout
- [x] Client socket error handling
- [x] TCP test client (interactive send/receive)
- [x] Basic connection analysis (disconnections, timeouts, errors)
- [ ] Maximum connection duration
- [ ] TCP reset simulation
- [ ] Advanced connection analysis
- [ ] *TBD*

## About

This is a personal learning project to explore TCP networking and basic security monitoring using Python. I'm using GitHub to store and document my progress.

See [`main.py`](main.py), [`test_client.py`](test_client.py), and [`log_analyzer.py`](log_analyzer.py) for the current implementation.
