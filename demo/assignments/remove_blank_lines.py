import os

sfile = open("names.txt", "rt")
tfile = open("temp.txt","wt")
for line in sfile.readlines():
     if len(line.strip()) > 0:
         tfile.write(line)

sfile.close()
tfile.close()

# Delete source file and rename target file as source
os.remove("names.txt")
os.rename("temp.txt","names.txt")
