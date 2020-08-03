file = open("names.txt", "rt")

names = {}  # Dict
for name in file.readlines():
    name = name.strip()  # remove whitespace chars
    if len(name) == 0:
        continue    # ignore blank lines

    if name in names:
        names[name] += 1  # increment count by 1
    else:
        names[name] = 1   # insert with count 1

file.close()

for name, count in sorted(names.items()):
    print(f"{name}  {count}")
