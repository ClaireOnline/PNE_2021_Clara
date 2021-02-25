import P0.Seq0 as Seq0


GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G"]

print("------| Exercise 8 |------")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    sort_freq = sorted(Seq0.seq_count(seq).items(), key=lambda item: item[1], reverse=True)
    print("Gene " + gene + " most frequent base:", sort_freq[0][0])
