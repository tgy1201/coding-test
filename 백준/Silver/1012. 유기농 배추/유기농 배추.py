import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    li[x][y] = 2

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0 <= xx < N and 0 <= yy < M and li[xx][yy] == 1:
            dfs(xx, yy)
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    li = [[0]*M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        li[b][a] = 1

    cnt = 0
    for a in range(N):
        for b in range(M):
            if li[a][b] == 1:
                dfs(a,b)
                cnt += 1

    print(cnt)