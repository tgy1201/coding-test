T = int(input())

for k in range(T):
    N = int(input())

    E = list(map(int, input().split()))

    li = []

    dp = [1] * N
    for i in range(1,N):
        for j in range(0, i):
            if E[i] > E[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{k+1} {max(dp)}")