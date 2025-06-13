import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))

e = list(permutations(li, M))

for i in sorted(e):
    print(' '.join(map(str, i)))