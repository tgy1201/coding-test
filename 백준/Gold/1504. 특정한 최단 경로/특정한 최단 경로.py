import sys, heapq
from collections import defaultdict
input = sys.stdin.readline


N, E = map(int, input().split())
dd = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    dd[a].append((c,b))
    dd[b].append((c,a))

def dfs(x):
    distance = [1e9] * (N+1)
    distance[x] = 0

    hq = [(0, x)]

    while hq:
        v, u = heapq.heappop(hq)

        if distance[u] < v:
            continue
        for x, y in dd[u]:
            if distance[y] > v + x:
                distance[y] = v + x
                heapq.heappush(hq, (distance[y], y))

    return distance

B, C = map(int, input().split())

if dfs(1)[N] == 1e9:
    print(-1)
else:
    print(min(dfs(1)[B]+dfs(B)[C]+dfs(C)[N], dfs(1)[C]+dfs(C)[B]+dfs(B)[N]))