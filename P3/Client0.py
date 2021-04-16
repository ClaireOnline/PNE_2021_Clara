import socket
import termcolor


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

#    @staticmethod
#    def ping():
#        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up!")
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the Port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

    def debug_talk(self, ms):
        answer = termcolor.colored(self.talk(termcolor.colored(ms, 'green')), 'green')
        print("To server:", termcolor.colored(ms, 'blue'))
        print(f"From Server: {answer}")
