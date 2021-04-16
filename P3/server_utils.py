from Seq1 import Seq


def print_colored(text, color):
    import termcolor
    print(termcolor.colored(text, color))


def format_command(command):
    return command.replace("\r", "").replace("\n", "")


def ping():
    print_colored("PING command!", "green")


def info(seq):
    s = Seq(seq)
    l = Seq.len(s)
    a = [Seq.count_base(s, "A"), Seq.count_base(s, "A") * 100 / l]
    c = [Seq.count_base(s, "C"), Seq.count_base(s, "C") * 100 / l]
    g = [Seq.count_base(s, "G"), Seq.count_base(s, "G") * 100 / l]
    t = [Seq.count_base(s, "T"), Seq.count_base(s, "T") * 100 / l]
    return "Sequence: " + str(s) + "\nTotal length: " + str(l) + "\nA: " + str(a[0]) + " (" + str(round(a[1],1)) + "%)" + "\nC: " + str(c[0]) + " (" + str(round(c[1],1)) + "%)" + "\nG: " + str(g[0]) + " (" + str(round(g[1],1)) + "%)" + "\nT: " + str(t[0]) + " (" + str(round(t[1],1)) + "%)"


def comp(seq):
    s = Seq(seq)
    return Seq.complement(s)


def rev(seq):
    s = Seq(seq)
    return Seq.reverse(s)


def gene(gen):
    s = Seq()
    g = gen + ".txt"
    return Seq.read_fasta(s, g)
