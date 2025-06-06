import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

li = []
user = (0,0)

for i in range(N):
    e = input()

    t = []
    for index, j in enumerate(e):
        if j == "I":
            user = (i, index)
        t.append(j)
    li.append(t)

visited = [[False]*M for _ in range(N)]
dq = deque()
dq.append(user)
answer = 0
visited[user[0]][user[1]] = True

while dq:
    x, y = dq.popleft()

    if li[x][y] == "P":
        answer += 1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy] and li[xx][yy] != "X":
            visited[xx][yy] = True
            dq.append((xx,yy))
            
if answer == 0:
    print("TT")
else:
    print(answer)