from Seq1 import Seq
from jinja2 import Template
from pathlib import Path


def read_template(filename):
    return Template(Path(filename).read_text())


def print_colored(text, color):
    import termcolor
    print(termcolor.colored(text, color))


def format_command(command):
    return command.replace("\r", "").replace("\n", "")


def list(list_seq, seq_num):
    context = {
        "number": seq_num,
        "sequence": list_seq[int(seq_num)]
    }
    content = read_template("./html/get.html").render(context=context)
    return content


def info(seq):
    s = Seq(seq)
    result = "Sequence: " + str(s)
    length = Seq.len(s)
    result += "\nTotal length: " + str(length)
    a = [Seq.count_base(s, "A"), Seq.count_base(s, "A") * 100 / length]
    result += "\nA: " + str(a[0]) + " (" + str(round(a[1], 1)) + "%)"
    c = [Seq.count_base(s, "C"), Seq.count_base(s, "C") * 100 / length]
    result += "\nC: " + str(c[0]) + " (" + str(round(c[1], 1)) + "%)"
    g = [Seq.count_base(s, "G"), Seq.count_base(s, "G") * 100 / length]
    result += "\nG: " + str(g[0]) + " (" + str(round(g[1], 1)) + "%)"
    t = [Seq.count_base(s, "T"), Seq.count_base(s, "T") * 100 / length]
    result += "\nT: " + str(t[0]) + " (" + str(round(t[1], 1)) + "%)"
    context = {
        "seq": s,
        "op": "Info",
        "res": result
    }
    content = read_template("./html/operation.html").render(context=context)
    return content


def comp(seq):
    s = Seq(seq)
    result = str(Seq.complement(s))
    context = {
        "seq": s,
        "op": "Comp",
        "res": result
    }
    content = read_template("./html/operation.html").render(context=context)
    return content


def rev(seq):
    s = Seq(seq)
    result = str(Seq.reverse(s))
    context = {
        "seq": s,
        "op": "Rev",
        "res": result
    }
    content = read_template("./html/operation.html").render(context=context)
    return content


def gene(gen):
    s = Seq()
    g = "./Sequences/" + gen + ".txt"
    sequence = Seq.read_fasta(s, g)
    context = {
        "gene_seq": gen,
        "gene_contents": sequence
    }
    contents = read_template("./html/gene.html").render(context=context)
    return contents
