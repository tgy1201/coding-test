import sys

n = int(sys.stdin.readline())
arr = [] * n
cnt = 0

for x in range(0, n):
    k = int(input())
    if k == 0:
        arr.pop()
    else:
        arr.append(k)

for x in range(0, len(arr)):
    cnt = cnt + arr[x]

print(cnt)

