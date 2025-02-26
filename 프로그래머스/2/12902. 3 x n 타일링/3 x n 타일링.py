def solution(n):
    answer = 0
    MOD =1000000007
    
    d = [0] * (n + 1)
    d[0] = 0
    d[1] = 0
    d[2] = 3
    d[3] = 0
    d[4] = 11
    
    for i in range(5,n+1):
        d[i] = 4*d[i-2] - d[i-4]
        
    return d[n] % MOD
'''
6, 41
8, 153
10, 571
12, 2131
14, 7953
'''
