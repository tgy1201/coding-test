import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

dq = deque()
li = []
for j in range(N):
    e = list(map(int, input().split()))
    for index, k in enumerate(e):
        if k == 1:
            dq.append((j,index,0))
    li.append(e)

answer = 0
while dq:
    y,z,depth = dq.popleft()
    answer = max(answer, depth)

    dy = [-1, 1, 0, 0]
    dz = [0, 0, -1, 1]

    for i in range(4):
        yy = y + dy[i]
        zz = z + dz[i]

        if 0 <= yy < N and 0 <= zz < M and li[yy][zz] == 0:
            li[yy][zz] = 1
            dq.append((yy,zz,depth+1))

check = 0
for j in range(N):
    for k in range(M):
        if li[j][k] == 0:
            check = 1
            break

    if check == 1:
        break

if check == 1:
    print(-1)
else:
    print(answer)