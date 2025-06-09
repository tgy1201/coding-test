import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N = int(input())

dd = defaultdict(list)
li = [[0]*N for _ in range(N)]

for i in range(N):
    el = list(map(int, input().split()))
    for index, j in enumerate(el):
        if j == 1:
            dd[i].append(index)

dq = deque()

for i in range(N):
    dq.append(i)
    while dq:
        x = dq.popleft()

        for j in dd[x]:
            if li[i][j] == 0:
                li[i][j] = 1
                dq.append(j)

for i in li:
    print(' '.join(map(str, i)))