import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    dq = deque()
    visited = set()

    dq.append((A, ''))
    visited.add(A)

    while dq:
        x, depth = dq.popleft()

        if x == B:
            print(depth)
            break

        for i in ["D","S","L","R"]:
            if i == "D":
                xx = (x*2) % 10000
            elif i =="S":
                if x == 0:
                    xx = 9999
                else:
                    xx = x-1
            elif i =="L":
                xx = x % 1000 * 10 + x // 1000
            else:
                xx = x // 10 + x % 10 * 1000

            if xx not in visited:
                visited.add(xx)
                dq.append((xx, depth+i))
