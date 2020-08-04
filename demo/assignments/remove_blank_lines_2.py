import os

file = open("names.txt", "rt")
lines = []
for line in file.readlines():
     if len(line.strip()) > 0:
         lines.append(line)

file.close()

# Write lines from list to file
file = open("names.txt", "wt")
for line in lines:
    file.write(line)

file.close()

