a = int(input())

b = bin(a)

c = str(b)[2:][::-1]

d = int(c, base=2)

print(d)