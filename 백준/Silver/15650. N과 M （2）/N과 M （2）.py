import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

li = [x+1 for x in range(N)]

e = list(combinations(li, M))

for i in e:
    print(' '.join(map(str, i)))