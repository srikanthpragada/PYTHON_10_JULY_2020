def wish(name, message="Hello"):
    print(message, name)


wish("Tom", "Hi")  # Positional
wish("James")
wish(name="Bob", message="Hi")  # Keyword
wish(message="Good Bye", name="Joe")
