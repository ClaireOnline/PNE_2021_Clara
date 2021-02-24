from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    sequence = Path(filename).read_text()
    sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return sequence


def seq_len(sequence):
    return len(sequence)


def seq_count_base(sequence, base):
    return sequence.count(base)


def seq_count(sequence):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in sequence:
        gene_dict[base] += 1
    return gene_dict


def seq_reverse(sequence):
    return sequence[::-1]
