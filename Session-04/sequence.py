from pathlib import Path
FILENAME = "ADA.txt"
file_contents = Path(FILENAME).read_text()
seq = file_contents[file_contents.find("\n"):].replace("\n", "")
print(len(seq))
