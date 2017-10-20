megabytes = int(input())
lines = int(input())

remainder = 0
for i in range(lines):
    remainder += megabytes - int(input())

print(remainder + megabytes)