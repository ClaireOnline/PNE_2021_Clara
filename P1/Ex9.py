from Seq1 import Seq

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s = s.read_fasta("../P0/Sequences/U5.txt")
print("Sequence: (Length: " + str(Seq.count_base(s)) + ")", s)
print("Bases:", Seq.count(s))
print("Rev:", Seq.reverse(s))
print("Comp:", Seq.complement(s))
