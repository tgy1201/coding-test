import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
ss = set(li)

m = max(li)
dd = defaultdict(int)

for i in li:
    cnt = 2
    s = i
    while s*cnt <= m:
        if s*cnt in ss:
            dd[i] += 1
            dd[s*cnt] -= 1
        cnt += 1

answer = []
for i in li:
    answer.append(dd[i])

print(' '.join(map(str, answer)))