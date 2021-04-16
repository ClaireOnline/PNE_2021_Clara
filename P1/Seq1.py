from pathlib import Path


class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases=None):
        if not strbases:
            print("NULL Seq created")
            self.strbases = "NULL"
        else:
            c = 0
            for base in strbases:
                if base != "A" and base != "C" and base != "T" and base != "G":
                    print("INVALID Seq!")
                    self.strbases = "ERROR"
                    break
                else:
                    c += 1
            if c == len(strbases):
                self.strbases = strbases
                print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        sequence = self.strbases
        if self.strbases != "NULL" and self.strbases != "ERROR":
            for base in sequence:
                gene_dict[base] += 1
        return gene_dict

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            complement_seq = ""
            complement_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
            for base in self.strbases:
                complement_seq += complement_dict[base]
            return complement_seq

    def read_fasta(self, filename):
        sequence = Path(filename).read_text()
        sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
        self.strbases = sequence
        return sequence
