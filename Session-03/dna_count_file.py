sequences = open("dna.txt", "r")
for line in sequences:
    seq = line.replace("\n", "")
    print("Sequence:", seq)
    a, c, g, t = 0, 0, 0, 0
    for base in seq:
        if base == "A":
            a += 1
        elif base == "C":
            c += 1
        elif base == "T":
            t += 1
        elif base == "G":
            g += 1
        else:
            print("Not a valid sequence")
            break
    print("Total length:", len(seq), "\nA:", a, "\nC:", c, "\nT:", t, "\nG:", g)
