import os

folder = input("Enter starting folder :")
pattern = input("Enter search string   :")

allfiles = os.walk(folder)
for (dirname, dirs, files) in allfiles:
    for file in files:
        if pattern in file:   # if pattern is present in filename
              print(dirname + "\\" + file)

