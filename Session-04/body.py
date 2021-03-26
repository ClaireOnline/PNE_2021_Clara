from pathlib import Path
FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
print(file_contents[file_contents.find("\n"):])
