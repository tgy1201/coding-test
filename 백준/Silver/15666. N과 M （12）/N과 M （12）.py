import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))

e = set(combinations_with_replacement(sorted(li), M))

for i in sorted(list(e)):
    print(' '.join(map(str, i)))