import sys

for line in sys.stdin:
    numRecords = int(line)
    if numRecords == -1:
        break

    totalDistance = 0
    lastTime = 0
    for record in range(numRecords):
        recordSplit = input().split(" ")
        mph = int(recordSplit[0])
        time = int(recordSplit[1])
        totalDistance += mph * (time - lastTime)
        lastTime = time
    print(str(totalDistance) + " miles")
