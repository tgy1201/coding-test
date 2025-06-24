import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
memo = defaultdict(int)
MOD = 1000000007

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]
    else:
        if n % 2 == 0:
            memo[n] = (fib(n//2)*(2*fib(n//2-1) + fib(n//2)))%MOD
            return memo[n]
        else:
            a = (n+1)//2
            memo[n] = (pow(fib(a), 2) + pow(fib(a-1), 2)) % MOD
            return memo[n]

print(fib(n))