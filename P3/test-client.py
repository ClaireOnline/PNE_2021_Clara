from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


PORT = 8080
IP = "127.0.0.1"

seq = ""
c = Client(IP, PORT)
print(c)
print("* Testing PING...")
print(Client.talk(c, "PING"))
print("* Testing GET...")
for i in range(0, 5):
    get = "GET " + str(i)
    print(get + ":", end=" ")
    print(Client.talk(c, get))
    if i == 0:
        seq = Client.talk(c, get)
print("* Testing INFO...")
print(Client.talk(c, "INFO " + seq))
print("* Testing COMP...")
print("COMP " + seq, Client.talk(c, "COMP " + seq))
print("* Testing REV...")
print("REV " + seq, Client.talk(c, "REV " + seq))
print("* Testing GENE...")
print("GENE U5", Client.talk(c, "GENE U5"))
print("GENE ADA", Client.talk(c, "GENE ADA"))
print("GENE FRAT1", Client.talk(c, "GENE FRAT1"))
print("GENE FXN", Client.talk(c, "GENE FXN"))
print("GENE RNU6_269P", Client.talk(c, "GENE RNU6_269P"))
