import sys

input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print(n+2)
else:
    print(n+3)