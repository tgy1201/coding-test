import sys
N, M = map(int, input().split())

li = list(map(int, sys.stdin.readline().strip().split()))
temp = [0] * (N+1)
temp[0] = 0
temp[1] = li[0]

for i in range(2, N+1):
    temp[i] = temp[i-1] + li[i-1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    total = temp[b] - temp[a-1]

    print(total)