students = {}

while True:
    data = input("Enter rollno,marks [end to stop] :")
    if data == 'end':
        break
    rollno, marks = data.split(',')

    if rollno in students:
        students[rollno].append(marks)
    else:
        students[rollno] = [marks]  # Add new entry

for rollno, marks in sorted(students.items()):
    print(f"{rollno:3} {','.join(marks)}")
