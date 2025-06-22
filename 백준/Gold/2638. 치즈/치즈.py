import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
p = []

cz = set()
for i in range(N):
    e = list(map(int, input().split()))

    for index, j in enumerate(e):
        if j == 1:
            cz.add((i,index))
    p.append(e)
p[0][0] = 2

answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while cz:
    dq = deque()
    dq.append((0, 0))
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M and p[xx][yy] != 1 and not visited[xx][yy]:
                visited[xx][yy] = True
                p[xx][yy] = 2
                dq.append((xx, yy))

    rm = set()
    for x, y in cz:
        cnt = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if p[xx][yy] == 2:
                cnt += 1
        if cnt >= 2:
            p[x][y] = 0
            rm.add((x,y))

    cz -= rm
    answer += 1

print(answer)