import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
shark = (0, 0)
sp = []

for i in range(N):
    e = list(map(int, input().split()))

    for index, j in enumerate(e):
        if j == 9:
            shark = (i, index)
            break

    sp.append(e)

size = 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ate = 0
answer = 0

while True:
    dq = deque()
    dq.append((shark[0], shark[1], 0))

    fish = []
    visited = [[False]*N for _ in range(N)]
    visited[shark[0]][shark[1]] = True

    while dq:
        x, y, depth = dq.popleft()

        if fish and fish[0][0] < depth:
            break
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N and size >= sp[xx][yy] and not visited[xx][yy]:
                if 0 < sp[xx][yy] < size:
                    fish.append((depth+1,xx,yy))
                visited[xx][yy] = True
                dq.append((xx, yy, depth+1))
    if not fish:
        break
    fish.sort()
    sp[shark[0]][shark[1]] = 0
    shark = (fish[0][1], fish[0][2])
    sp[fish[0][1]][fish[0][2]] = 0
    answer += fish[0][0]
    ate += 1

    if ate == size:
        size += 1
        ate = 0

print(answer)