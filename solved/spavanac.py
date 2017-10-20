time = input().split(" ")
hours = int(time[0])
mins = int(time[1])

if mins < 45:
    hours = (hours - 1) % 24

mins = (mins - 45) % 60

print(str(hours) + " " + str(mins))