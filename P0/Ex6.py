import P0.Seq0 as Seq0

FOLDER = "./Sequences/"
ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
print("------| Exercise 6 |------\nGene U5:\nFrag:", U5_Seq[0:19], "\nRev:", Seq0.seq_reverse(U5_Seq[0:19]))
