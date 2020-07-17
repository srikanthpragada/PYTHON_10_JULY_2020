results = []
for i in range(5):
    n = int(input("Enter a number :"))
    if n % 2 == 0:
        results.append(True)
    else:
        results.append(False)

print(results)
print("No. of evens : ", results.count(True))
print("No. of odds  : ", results.count(False))
