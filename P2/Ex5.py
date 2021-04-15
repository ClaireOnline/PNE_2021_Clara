from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
s = Seq()
s.read_fasta("../P0/Sequences/U5.txt")
print(c)
c.debug_talk("Sending the U5 Gene to the server...")
c.debug_talk(s)
