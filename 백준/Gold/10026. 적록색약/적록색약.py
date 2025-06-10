import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N = int(input())

v1 = [[False]*N for _ in range(N)]
v2 = [[False]*N for _ in range(N)]
li = []
for i in range(N):
    s = input().strip()
    temp = []
    for j in s:
        temp.append(j)
    li.append(temp)


def dfs(x, y, c):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < N and 0 <= yy < N:
            if c == 0 and not v1[xx][yy] and li[xx][yy] == li[x][y]:
                v1[xx][yy] = True
                dfs(xx, yy, c)
            elif c == 1 and not v2[xx][yy] and (li[xx][yy] == li[x][y] or (li[xx][yy] in ('G','R') and li[x][y] in ('G','R'))):
                v2[xx][yy] = True
                dfs(xx, yy, c)

c1, c2 = 0, 0
for i in range(N):
    for j in range(N):
        if not v1[i][j]:
            v1[i][j] = True
            dfs(i, j, 0)
            c1 += 1
        if not v2[i][j]:
            v2[i][j] = True
            dfs(i, j, 1)
            c2 += 1
print(f"{c1} {c2}")