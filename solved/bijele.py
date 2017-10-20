totals = [1, 1, 2, 2, 2, 8]
results = [""] * 6
actual = input().split(" ")

for i in range(len(totals)):
    results[i] = str(totals[i] - int(actual[i]))

print(" ".join(results))