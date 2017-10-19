numTests = int(input())
for i in range(numTests):
    test = int(input())
    print(str(test) + " is " + ("even" if test % 2 == 0 else "odd"))