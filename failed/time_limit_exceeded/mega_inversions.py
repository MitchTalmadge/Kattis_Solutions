def calculate(seq_len, seq):
    total = 0

    for i in range(seq_len):
        if i < seq_len - 2:
            for j in range(i + 1, seq_len):
                if seq[j] < seq[i] and j < seq_len - 1:
                    for k in range(j + 1, seq_len):
                        if seq[k] < seq[j]:
                            total += 1

    return total

print(calculate(int(input()), [int(x) for x in input().split(" ")]))