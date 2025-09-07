import sys

input = sys.stdin.readline

n = int(input())

if n == 1 or n == 2:
    print(4)
elif n % 2 == 0:
    print(min(n, 10**9))
else:
    print(min(n+1, 10**9))