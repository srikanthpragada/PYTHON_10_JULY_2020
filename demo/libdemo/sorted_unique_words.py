
import re

file = open(r"c:\classroom\old_man.txt","rt")
words = re.findall(r"\w+", file.read().lower())

for word in sorted(set(words)):
     print(word)
