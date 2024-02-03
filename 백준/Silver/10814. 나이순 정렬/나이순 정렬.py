import sys

n = int(sys.stdin.readline())
arr = [] * n

for x in range(0, n):
    a, b= map(str, sys.stdin.readline().split())
    arr.append([int(a), b])

for i in sorted(arr, key= lambda x : x[0]):
    print(i[0], i[1])