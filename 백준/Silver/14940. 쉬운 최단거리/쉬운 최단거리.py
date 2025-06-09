import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())

li = []
x, y = 0, 0
for i in range(M):
    el = list(map(int, input().split()))
    for index, j in enumerate(el):
        if j == 2:
            x, y = i, index
    li.append(el)

temp = [[0]*M for _ in range(N)]
visited = set()
visited.add((x,y))

dq = deque()
dq.append((x,y,0))


while dq:
    a, b, depth = dq.popleft()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        xx = a + dx[i]
        yy = b + dy[i]

        if 0 <= xx < N and 0 <= yy < M and li[xx][yy] == 1:
            visited.add((xx,yy))
            li[xx][yy] = 3
            temp[xx][yy] = depth + 1
            dq.append((xx,yy,depth+1))

for i1, i in enumerate(temp):
    t = []
    for i2, j in enumerate(i):
        if (i1, i2) not in visited and li[i1][i2] != 0:
            t.append(-1)
        else:
            t.append(j)
    print(' '.join(map(str, t)))