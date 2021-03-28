import socket


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the Port?")
