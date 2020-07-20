
students = {}

while True:
    data = input("Enter rollno,marks [end to stop] :")
    if data == 'end':
        break
    parts = data.split(',')
    students[parts[0]] = parts[1]


for rollno, marks in sorted(students.items()):
    print(f"{rollno:3} {marks:3}")
