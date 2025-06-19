import sys
input = sys.stdin.readline

N, K = map(int, input().split())


bag = []
for _ in range(N):
    W, V = map(int, input().split())
    bag.append((W,V))

dp = [[0]*(N+1) for _ in range(K+1)]


for i in range(1, K+1):
    for j in range(1, N+1):
        w, v = bag[j-1]

        if i >= w:
            dp[i][j] = max(dp[i][j-1], dp[i-w][j-1] + v)
        else:
            dp[i][j] = dp[i][j-1]
print(dp[K][N])
