import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

dq = deque()
li = []
for i in range(H):
    temp = []
    for j in range(N):
        e = list(map(int, input().split()))
        for index, k in enumerate(e):
            if k == 1:
                dq.append((i,j,index,0))
        temp.append(e)
    li.append(temp)

answer = 0
while dq:
    x,y,z,depth = dq.popleft()
    answer = max(answer, depth)

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0 , -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    for i in range(6):
        xx = x + dx[i]
        yy = y + dy[i]
        zz = z + dz[i]

        if 0 <= xx < H and 0 <= yy < N and 0 <= zz < M and li[xx][yy][zz] == 0:
            li[xx][yy][zz] = 1
            dq.append((xx,yy,zz,depth+1))

check = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if li[i][j][k] == 0:
                check = 1
                break

        if check == 1:
            break
    if check == 1:
        break

if check == 1:
    print(-1)
else:
    print(answer)