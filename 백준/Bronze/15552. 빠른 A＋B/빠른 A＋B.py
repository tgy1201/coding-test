import sys
x = int(input())

for i in range(1, x+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)