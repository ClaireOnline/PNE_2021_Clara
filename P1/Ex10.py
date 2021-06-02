from Seq1 import Seq
from pathlib import Path

file_list = Path("../P0/Sequences").glob('*.txt')
for file in file_list:
    path_in_str = str(file)
    file_name = path_in_str.replace('\\', "/")
    print(file_name)
    s = Seq()
    s = s.read_fasta(file_name)
    gene_name = file_name.split("/")[-1].replace(".txt", "")
    print(gene_name)
    print("Gene " + gene_name + ": Most frequent Base:", Seq.most_freq(Seq.count(s)))
