from Seq1 import Seq

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta("../P0/Sequences/U5.txt")
print(s)
