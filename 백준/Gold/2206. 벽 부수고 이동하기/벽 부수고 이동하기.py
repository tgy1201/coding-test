import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

li = []
for i in range(N):
    e = input().strip()

    temp = []
    for j in e:
        temp.append(int(j))

    li.append(temp)

dp = [[[1e9, 1e9] for _ in range(M)] for _ in range(N)]
dp[0][0][0] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    dq = deque()
    dq.append((a,b,0))

    while dq:
        x, y, wall = dq.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M:
                if li[xx][yy] == 0 and dp[x][y][wall] + 1 < dp[xx][yy][wall]: #빈칸
                    dp[xx][yy][wall] = dp[x][y][wall] + 1

                    dq.append((xx, yy, wall))
                elif li[xx][yy] == 1 and wall == 0 and dp[x][y][wall] + 1 < dp[xx][yy][1]:
                        dp[xx][yy][1] = dp[x][y][wall] + 1
                        dq.append((xx, yy, 1))
bfs(0, 0)

if dp[N-1][M-1][0] == 1e9 and dp[N-1][M-1][1] == 1e9:
    print(-1)
else:
    print(min(dp[N-1][M-1][0]+1, dp[N-1][M-1][1]+1))
