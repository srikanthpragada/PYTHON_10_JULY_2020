import re

file = open(r"c:\classroom\old_man.txt", "rt")
words = re.findall(r"[a-zA-Z0-9]+", file.read().lower())

wordcount = {}

for word in words:
    if word in wordcount:
        wordcount[word] += 1  # increment count
    else:
        wordcount[word] = 1  # add word with count 1

for word, count in sorted(wordcount.items()):
    print(f"{word:15} {count:3}")
