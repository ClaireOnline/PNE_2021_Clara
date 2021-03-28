from Seq1 import Seq

# Null sequence
s1 = Seq()

# valid sequence
s2 = Seq("ACTGA")

# invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: (Length: " + str(Seq.len(s1)) + ") ", s1)
print("\tBases:", Seq.count(s1))
print("\tRev: ", Seq.reverse(s1))
print("Sequence 2: (Length: " + str(Seq.len(s2)) + ") ", s2)
print("\tBases:", Seq.count(s2))
print("\tRev: ", Seq.reverse(s2))
print("Sequence 3: (Length: " + str(Seq.len(s3)) + ") ", s3)
print("\tBases:", Seq.count(s3))
print("\tRev: ", Seq.reverse(s3))
