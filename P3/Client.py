import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "127.0.0.1"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necessary to encode the string into bytes
s.send(str.encode("GENE U5"))

# Receive data from the server
msg = s.recv(2048)
print(msg.decode("utf-8"))

# Closing the socket
s.close()
