def solution(n):
    dp = [0] * (n+2)
    MOD = 1234567
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % MOD