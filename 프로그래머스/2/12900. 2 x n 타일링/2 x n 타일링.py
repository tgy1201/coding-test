def solution(n):
    MOD = 1000000007
    
    def cal(num):
        if num == 0:
            return 1 
        if num == 1:
            return 1
        
        dp = [0] * (num + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, num + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        
        return dp[num]
    return cal(n)