def upper(st):
    for ch in st:
        if ch.isupper():
            yield ch


for c in upper("This Is FINE"):
    print(c)