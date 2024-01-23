a = int(input())

for x in range(2, a+1):
    while a % x == 0:
        if a % x == 0:
            a = a // x
            print(x)