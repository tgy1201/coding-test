import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
dd = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    dd[a].append((c,b))
    dd[b].append((c,a))

hq = [(0, 1)]
visited = [False] * (N+1)
answer = 0
m = 0

while hq:
    cost, p = heapq.heappop(hq)

    if not visited[p]:
        visited[p] = True
        answer += cost
        if cost > m:
            m = cost
        for u, v in dd[p]:
            if not visited[v]:
                heapq.heappush(hq, (u, v))

print(answer-m)