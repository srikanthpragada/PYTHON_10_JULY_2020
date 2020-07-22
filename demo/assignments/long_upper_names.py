names = ["Java", "PYTHON", "JavaScript", "TYPESCRIPT", "CPP"]


def isUpperLong(s):
    return len(s) >= 5 and s.isupper()


for n in filter(isUpperLong, names):
    print(n)
