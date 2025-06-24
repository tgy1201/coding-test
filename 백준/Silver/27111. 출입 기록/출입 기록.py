import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

dd = defaultdict(int)
visited = set()
answer = 0
for i in range(N):
    a, b = map(int, input().split())

    if b == 1:
        if dd[a] == 0:
            dd[a] = 1
        else:
            answer += 1
    else:
        if dd[a] == 1:
            dd[a] = 0
        else:
            answer += 1

for i in dd.keys():
    if dd[i] == 1:
        answer += 1

print(answer)