from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)
s = Seq()
s.read_fasta("../P0/Sequences/FRAT1.txt")
# for i in range(0, 50, 10):
#     fragment = s.strbases[i:i+10]
c.debug_talk("Sending the FRAT1 Gene to the server, in fragments of 10 bases...")
count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i:i + 10]
    count += 1
    i += 10
    c.debug_talk("Fragment " + str(count) + ": " + fragment)
