import sys
from collections import defaultdict
N, M = map(int, input().split())

li = []
a = defaultdict(int)
b = defaultdict(str)

for i in range(N):
    s = sys.stdin.readline().strip()
    a[s] = i+1
    b[i+1] = s

for j in range(M):
    s = input()

    if s.isdigit():
        print(b[int(s)])
    else:
        print(a[s])