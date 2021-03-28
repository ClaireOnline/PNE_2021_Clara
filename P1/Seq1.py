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