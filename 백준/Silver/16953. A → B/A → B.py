from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

dq = deque()
dq.append((A, 0))
answer = -1

while dq:
    a, depth = dq.popleft()

    if a == B:
        answer = depth
        break

    for i in range(2):
        x = a
        if i == 0:
            x *= 2
        else:
            x = int(str(x)+"1")

        if x <= B:
            dq.append((x, depth+1))

if answer == -1:
    print(-1)
else:
    print(answer+1)

