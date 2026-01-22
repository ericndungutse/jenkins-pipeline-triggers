import socket
import os

def main():
    hostname = socket.gethostname()
    print(f"Name of the server: {hostname}")
    print(f"Current working directory: {os.getcwd()}")

if __name__ == "__main__":
    main()
        