import sys
n = int(sys.stdin.readline())
arr = [0] * 10001

for x in range(n):
    a = int(sys.stdin.readline())
    arr[a] = arr[a] + 1

for y in range(10001):
    if arr[y] != 0:
        for z in range(arr[y]):
            print(y)