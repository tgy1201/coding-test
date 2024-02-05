import sys

n, k = map(int, sys.stdin.readline().split())
arr = [] * n

for x in range(0,n):
    arr.append(x+1)
cnt = 0
str = "<"
t = 0
for y in range(0, n):
    while cnt != k:
        if t >= len(arr):
            t = t % n
        if arr[t] !=0:
            cnt = cnt + 1
            t = t + 1
        elif arr[t] == 0:
            t = t + 1
    cnt = 0
    if y == n-1:
        str += f"{t}>"
    else:
        str += f"{t}, "
    arr[t-1] = 0
print(str)