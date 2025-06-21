import sys, copy
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

dom = []
area = []
virus = set()
for i in range(N):
    e = list(map(int, input().split()))

    for j, v in enumerate(e):
        if v == 0:
            area.append((i,j))
        elif v == 2:
            virus.add((i,j))

    dom.append(e)

wall = list(combinations(area, 3))
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global a

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < N and 0 <= yy < M and cdom[xx][yy] == 0:
            cdom[xx][yy] = 2
            a -= 1
            dfs(xx, yy)


for i in wall:
    a = len(area) - 3
    cdom = copy.deepcopy(dom)
    check = 0

    for x, y in i:
        cdom[x][y] = 1

    for x, y in virus:
        dfs(x, y)

        if a < answer:
            check = 1
            break

    if check == 1:
        continue

    answer = max(answer, a)

print(answer)
