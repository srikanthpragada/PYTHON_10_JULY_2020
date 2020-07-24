import sys

if len(sys.argv) < 2:
    print("Usage   : python prime.py  <number>")
    print("Example : python prime.py  12345")
    exit()

value = sys.argv[1]
if not value.isdigit():
    print("Please enter a valid number!")
    exit()

num = int(value)

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")
