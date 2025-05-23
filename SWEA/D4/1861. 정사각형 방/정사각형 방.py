def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1  # 자기 자신 포함
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        xx, yy = x + dx, y + dy
        if 0 <= xx < N and 0 <= yy < N and li[xx][yy] == li[x][y] + 1:
            dp[x][y] = max(dp[x][y], dfs(xx, yy) + 1)

    return dp[x][y]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    dp = [[-1] * N for _ in range(N)]

    max_length = 0
    min_start = float('inf')

    for i in range(N):
        for j in range(N):
            length = dfs(i, j)
            if length > max_length:
                max_length = length
                min_start = li[i][j]
            elif length == max_length:
                min_start = min(min_start, li[i][j])

    print(f"#{test_case} {min_start} {max_length}")