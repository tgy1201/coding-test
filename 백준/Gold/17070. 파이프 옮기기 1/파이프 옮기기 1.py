import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

mp = []
for _ in range(N):
    e = list(map(int, input().split()))

    mp.append(e)

if mp[N-1][N-1] == 1:
    print(0)
else:
    answer = 0

    def dfs(x1, y1, x2, y2):
        global answer

        if x2 == N-1 and y2 == N-1:
            answer += 1
            return

        if x1 == x2:
            xx = x2
            yy = y2+1

            if yy < N and mp[xx][yy] != 1:
                dfs(x2, y2, xx, yy)
        elif y1 == y2:
            xx = x2+1
            yy = y2

            if xx < N and mp[xx][yy] != 1:
                dfs(x2, y2, xx, yy)
        else:
            for i in range(2):
                if i == 0:
                    xx = x2
                    yy = y2 + 1

                    if yy < N and mp[xx][yy] != 1:
                        dfs(x2, y2, xx, yy)
                else:
                    xx = x2 + 1
                    yy = y2

                    if xx < N and mp[xx][yy] != 1:
                        dfs(x2, y2, xx, yy)
        xx = x2 + 1
        yy = y2 + 1
        if xx < N and yy < N and mp[xx][yy] != 1 and mp[xx-1][yy] != 1 and mp[xx][yy-1] != 1:
            dfs(x2, y2, xx, yy)

    dfs(0, 0, 0, 1)

    print(answer)