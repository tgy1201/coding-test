import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

x, y = map(int, input().split())

xx = [x]
yy = [y]

a = 0
b = 0
for _ in range(N-1):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)

xx.append(xx[0])
yy.append(yy[0])

for i in range(len(xx)-1):
    a += xx[i]*yy[i+1]
    b += xx[i+1]*yy[i]

print(abs(a-b)/2)