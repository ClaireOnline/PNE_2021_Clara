import P0.Seq0 as Seq0

FOLDER = "./Sequences/"
ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
print("------| Exercise 7 |------\nGene U5:\nFrag:", U5_Seq[0:19], "\nComp:", Seq0.seq_complement(U5_Seq[0:19]))
