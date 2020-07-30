lst = []

while True:
    try:
        num = int(input("Enter a number [0 to stop]: "))
        if num == 0:
            break
        lst.append(num)
    except Exception as ex:
        print("Error : ", ex)

print(sorted(lst))
