class Names_Iterator:
    def __init__(self, names):
        self.names = names
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.names):
            raise StopIteration
        value = self.names[self.pos]
        self.pos += 1
        return value


class Names:
    def __init__(self):
        self.names = ["Python", "Java", "C#", "JavaScript", "TypeScript", "Visual Basic.Net"]

    def __iter__(self):
        return Names_Iterator(self.names)


names = Names()  # Iterable
ni = names.__iter__()
ni2 = names.__iter__()
print(ni.__next__())
print(ni2.__next__())

for n in names:
    print(n)

