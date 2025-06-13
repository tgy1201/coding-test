import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())

li = [x+1 for x in range(N)]

e = list(combinations_with_replacement(li, M))

for i in e:
    print(' '.join(map(str, i)))