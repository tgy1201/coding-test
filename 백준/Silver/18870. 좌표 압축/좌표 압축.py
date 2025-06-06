import sys
from bisect import bisect_left

input = sys.stdin.readline
N = int(input())

li = list(map(int, input().split()))

se = sorted(list(set(li[:])))

answer = []
for i in li:
    index = bisect_left(se, i)
    answer.append(index)

print(' '.join(map(str, answer)))