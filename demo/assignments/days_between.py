from datetime import datetime, date

file = open("dates.txt", "rt")
dates = []
for line in file:
    parts = line.strip().split(",")
    try:
        if len(parts) == 2:
            fd = datetime.strptime(parts[0], "%d-%m-%Y")
            sd = datetime.strptime(parts[1], "%d-%m-%Y")
        elif len(parts) == 1:
            fd = datetime.strptime(parts[0], "%d-%m-%Y")
            sd = datetime.now()

        days = (sd - fd).days
        dates.append((fd, sd, days))  # Add tuple with data to list
    except:
        # print("Invalid line :", line)
        pass

for t in sorted(dates, key=lambda t: t[2]):
    print(f"{t[0].strftime('%d-%m-%Y')} - {t[1].strftime('%d-%m-%Y')} - {t[2]:4}")
