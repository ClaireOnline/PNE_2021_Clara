from Seq1 import Seq

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: (Length: " + str(Seq.len(s1)) + ") ", s1)
print("\tA:", Seq.count_base(s1, "A"), end=", ")
print("C:", Seq.count_base(s1, "C"), end=", ")
print("T:", Seq.count_base(s1, "T"), end=", ")
print("G:", Seq.count_base(s1, "G"), end="\n")
print("Sequence 2: (Length: " + str(Seq.len(s2)) + ") ", s2)
print("\tA:", Seq.count_base(s2, "A"), end=", ")
print("C:", Seq.count_base(s2, "C"), end=", ")
print("T:", Seq.count_base(s2, "T"), end=", ")
print("G:", Seq.count_base(s2, "G"), end="\n")
print("Sequence 3: (Length: " + str(Seq.len(s3)) + ") ", s3)
print("\tA:", Seq.count_base(s3, "A"), end=", ")
print("C:", Seq.count_base(s3, "C"), end=", ")
print("T:", Seq.count_base(s3, "T"), end=", ")
print("G:", Seq.count_base(s3, "G"), end="\n")
