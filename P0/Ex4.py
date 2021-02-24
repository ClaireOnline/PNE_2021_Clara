import P0.Seq0 as Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G"]

print("------| Exercise 4 |------")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("\nGene " + gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(seq, base))
