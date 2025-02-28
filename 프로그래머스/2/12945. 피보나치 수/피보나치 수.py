def solution(k):
    answer = 0
    MOD = 1234567
    n = [0] * (k+2)
    n[1] = 1
    n[2] = 1
    for i in range(3, k+1):
        n[i] = n[i-1] + n[i-2]
    return n[k] % MOD