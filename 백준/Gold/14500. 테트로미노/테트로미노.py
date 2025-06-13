import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())

li = []
for _ in range(N):
    e = list(map(int, input().split()))
    li.append(e)

answer = 0
visited = [[False] * M for _ in range(N)]

def check_t_shape(x, y):
    global answer

    # ㅗ
    if x - 1 >= 0 and y - 1 >= 0 and y + 1 < M:
        temp = li[x][y] + li[x - 1][y] + li[x][y - 1] + li[x][y + 1]
        answer = max(answer, temp)

    # ㅜ
    if x + 1 < N and y - 1 >= 0 and y + 1 < M:
        temp = li[x][y] + li[x + 1][y] + li[x][y - 1] + li[x][y + 1]
        answer = max(answer, temp)

    # ㅓ
    if x - 1 >= 0 and x + 1 < N and y - 1 >= 0:
        temp = li[x][y] + li[x - 1][y] + li[x + 1][y] + li[x][y - 1]
        answer = max(answer, temp)

    # ㅏ
    if x - 1 >= 0 and x + 1 < N and y + 1 < M:
        temp = li[x][y] + li[x - 1][y] + li[x + 1][y] + li[x][y + 1]
        answer = max(answer, temp)

def dfs(x, y, d, cnt):
    global answer

    if d == 4:
        answer = max(answer, cnt)
        return
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy]:
            visited[xx][yy] = True
            dfs(xx, yy, d+1, cnt+li[xx][yy])
            visited[xx][yy] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, li[i][j])
        visited[i][j] = False
        check_t_shape(i, j)

print(answer)