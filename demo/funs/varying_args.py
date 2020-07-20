def wish(*names, message="Hello"):
    for n in names:
        print(message, n)


wish("Bob", "Bill", "Larry", message="Hi")
wish("Steve", "Jason")
