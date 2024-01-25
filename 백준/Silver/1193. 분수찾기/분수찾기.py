a = int(input())
cnt = 1
n = 2
index = 1
b = 0

while a > cnt:
    n = n + 1
    index = cnt
    cnt = cnt + (n-1)
b = a - index
c = 1
i =0
j =0
if a == 1:
    print("1/1")
else:
    for x in range(0, b):
        if n%2==0:
            i = n - c
            j = c
        else:
            i = c
            j = n - c
        c = c + 1
    print(f"{i}/{j}")