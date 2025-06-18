import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

dd = defaultdict(list)
dist = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    dist[a].append((c, b))

def dijkstra(x, dis):
    d = [1e9] * (N+1)
    d[x] = 0

    hq = [(0, x)]
    while hq:
        cost, p = heapq.heappop(hq)
        if cost > d[p]:
            continue
        for c, w in dis[p]:
            if d[w] > c+cost:
                d[w] = c+cost
                heapq.heappush(hq, (d[w], w))

    return d
a, b = map(int, input().split())

all_distance = dijkstra(a, dist)


print(all_distance[b])
