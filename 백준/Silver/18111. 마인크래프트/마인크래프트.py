import sys

n, m , b = map(int, sys.stdin.readline().split())
arr = [] * n
for x in range(0, n):
    k = list(map(int, sys.stdin.readline().split()))
    arr.append(k)
t = 0
ub = 0
tb = 0
min = int(1e9)
h = 0

for x in range(0, 257):
    tb = 0
    ub = 0
    for y in range(0, n):
        for z in range(0, m):
            if arr[y][z] < x: #블록쌓기
                ub = ub + ( x - arr[y][z] )  # 사용한 블록
            else:
                tb = tb + (arr[y][z] - x )
    if ub > tb + b:
        continue
    if tb*2 + ub <= min:
        min = tb*2 + ub
        h = x
print(min, h, end=" ")