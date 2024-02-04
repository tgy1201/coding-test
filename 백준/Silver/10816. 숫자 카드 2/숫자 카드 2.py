import sys
import collections

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
str = ""
dd = dict()

for x in a:
    if x in dd:
        dd[x] += 1
    else:
        dd[x] = 1
for y in b:
    if y in dd:
        print(dd[y], end= " ")
    else:
        print(0, end=" ")