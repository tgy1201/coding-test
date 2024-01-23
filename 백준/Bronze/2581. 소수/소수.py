a = int(input())
b = int(input())
n = 0
arr = [] * (a-b)

for x in range(a, b+1):
    cnt = 0
    for y in range(2, x):
        if x % y == 0:
            cnt = cnt + 1
    if cnt == 0 and x != 1:
        n = n + x
        arr.append(x)

if n == 0:
    print(-1)
else:
    print(n)
    print(arr[0])