import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())
k = set()
dd= defaultdict(int)
for i in range(N+M):
    a, b = map(int, input().split())
    dd[a] = b
    k.add(a)

distance = [1e9] * 101
distance[1] = 0

dq = deque()
dq.append((1, 0))

while dq:
    x, depth = dq.popleft()

    if x == 100:
        print(depth)
        break

    for i in range(1, 7):
        xx = x + i

        if 0 <= xx <= 100:
            if xx in k:
                xx = dd[xx]

            if distance[xx] > depth+1:
                distance[xx] = depth +1
                dq.append((xx, depth+1))