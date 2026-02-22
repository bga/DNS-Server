#!/usr/bin/env python3
import socket
import argparse

from dns_generator import ClientHandler

# Global variables
IP = "127.0.0.1"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=53)
    args = parser.parse_args()
    port = args.port
     
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, port))
    print("DNS Listening on {0}:{1} ...".format(IP, port))
    while True:
        data, address = sock.recvfrom(650)
        data = bytearray(data)
        client = ClientHandler(address, data, sock)
        client.run()


if __name__ == "__main__":
    main()
