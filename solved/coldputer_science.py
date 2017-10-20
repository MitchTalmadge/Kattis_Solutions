input()

lessThanZero = 0
for temp in input().split(" "):
    if int(temp) < 0:
        lessThanZero += 1
print(lessThanZero)