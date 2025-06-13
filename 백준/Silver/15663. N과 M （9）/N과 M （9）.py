import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))

e = set(permutations(li, M))

for i in sorted(list(e)):
    print(' '.join(map(str, i)))