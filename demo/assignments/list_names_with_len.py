
names = []

while True:
    name = input("Enter name : ")
    if name == 'end':
        break

    names.append(name)


for name in names:
    print(f"{name:10} {len(name)}")
