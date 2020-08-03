import os

allfiles = os.walk(r"c:\classroom\july10")

for (dirname, dirs, files) in allfiles:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
