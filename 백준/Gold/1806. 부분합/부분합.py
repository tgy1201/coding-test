import sys
from collections import deque

input = sys.stdin.readline

N, S = map(int, input().split())
li = list(map(int, input().split()))
dq = deque()
answer = 0
m = 1e9

for i in li:
    answer += i
    dq.append(i)

    if answer > S:
        while answer >= S:
            m = min(m, len(dq))
            x = dq.popleft()
            answer -= x
    elif answer < S:
        continue
    else:
        m = min(m, len(dq))

if m == 1e9:
    print(0)
else:
    print(m)
