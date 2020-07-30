a = 10
b = 0

try:
    c = a / b
    print(c)
except ValueError:
    print("Invalid value")
else:
    print("Success")
finally:
    print("Done")

print("The End")
