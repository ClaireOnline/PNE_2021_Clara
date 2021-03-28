from seq01 import Seq
from Ex2 import print_seqs


def generate_seqs(pattern, n):
    seq_list = []
    seq = ""
    for c in range(0, n):
        seq += pattern
        seq_list.append(Seq(seq))
    return seq_list


# MAIN PROGRAM
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print("\nList 2:")
print_seqs(seq_list2)
