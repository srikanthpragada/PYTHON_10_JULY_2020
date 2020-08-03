with open("names.txt", "wt") as file:
    names = []
    while True:
        name = input("Enter name [end to stop] :")
        if name == "end":
            break
        names.append(name)

    for name in sorted(names):
        file.write(name + "\n")
