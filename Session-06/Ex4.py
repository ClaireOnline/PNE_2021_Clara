from seq01 import Seq
import termcolor


def print_seqs(seqlist, color):
    for n in range(0, len(seqlist)):
        termcolor.cprint("Sequence " + str(n) + ":", color, end=" ")
        termcolor.cprint("(Length: " + str(Seq.len(seqlist[n])) + ") ", color, end=" ")
        termcolor.cprint(seqlist[n], color, end="\n")


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

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

termcolor.cprint("\nList 2:", "green")
print_seqs(seq_list2, "green")
