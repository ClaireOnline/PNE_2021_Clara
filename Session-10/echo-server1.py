import socket

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is up!")
while True:
    print("Awaiting connection...")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg = cs.recv(2048).decode()
        print(f"Received message: {msg}")
        res = "HELLO. I am the Happy Server :)\n"
        cs.send(res.encode())
        cs.close()
