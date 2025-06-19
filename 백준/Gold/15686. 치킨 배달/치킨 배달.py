import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

house = 0
ch = []
ma = []

for i in range(N):
    e = list(map(int, input().split()))

    for index, j in enumerate(e):
        if j == 1:
            house += 1
        elif j == 2:
            ch.append((i, index))
    ma.append(e)

com = list(combinations(ch, M))
answer = 1e9

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(li, cnt):
    visited = [[False]*N for _ in range(N)]

    dq = deque()

    for i in li:
        dq.append((i[0],i[1],0))
        visited[i[0]][i[1]] = True

    while dq:
        x, y, depth = dq.popleft()

        if ma[x][y] == 1:
            cnt += depth

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy]:
                visited[xx][yy] = True
                dq.append((xx, yy, depth+1))

    return cnt

for i in com:
    answer = min(answer, bfs(i, 0))

print(answer)