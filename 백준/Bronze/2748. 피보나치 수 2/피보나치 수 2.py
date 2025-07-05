import sys

input = sys.stdin.readline

N = int(input())
temp = [-1]*(N+1)
def fibo(n):
    if n == 1:
        temp[1] = 1
        return 1
    if n == 2:
        temp[2] = 2
        return 1
    if temp[n] != -1:
        return temp[n]
    temp[n] = fibo(n-1) + fibo(n-2)
    return temp[n]

print(fibo(N))