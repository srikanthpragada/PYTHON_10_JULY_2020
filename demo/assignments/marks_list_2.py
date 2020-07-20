students = {}

while True:
    data = input("Enter rollno,marks [end to stop] :")
    if data == 'end':
        break
    rollno, marks  = data.split(',')

    if rollno in students:
        students[rollno] = students[rollno] + int(marks)  # Add to existing total
    else:
        students[rollno] = int(marks)   # Add new entry


for rollno, marks in sorted(students.items()):
    print(f"{rollno:3} {marks:3}")
