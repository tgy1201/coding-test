import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
dd = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    dd[a].append((c,b))
    dd[b].append((c,a))

hq = [(0, 1)]
visited = [False] * (V+1)
answer = 0

while hq:
    cost, p = heapq.heappop(hq)

    if not visited[p]:
        visited[p] = True
        answer += cost
        for u, v in dd[p]:
            heapq.heappush(hq, (u, v))

print(answer)