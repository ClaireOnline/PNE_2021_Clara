from seq01 import Seq


def print_seqs(seqlist):
    for n in range(0, len(seqlist)):
        print("Sequence", n, end=": ")
        print("(Length:", Seq.len(seqlist[n]), end=") ")
        print(seqlist[n], end="\n")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
