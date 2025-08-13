import sys
from collections import defaultdict

input = sys.stdin.readline

dd = defaultdict(int)

a, b, c = map(int, input().split())

for i in range(3):
    x, y = map(int, input().split())

    for j in range(x, y):
        dd[j] += 1

answer = 0
for i in dd.keys():
    if dd[i] == 1:
        answer += a
    elif dd[i] == 2:
        answer += 2 * b
    else:
        answer += dd[i] * c

print(answer)