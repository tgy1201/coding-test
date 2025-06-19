import sys, heapq
from collections import defaultdict
input = sys.stdin.readline


N, E = map(int, input().split())
dd = defaultdict(list)
start = int(input())

for _ in range(E):
    a, b, c = map(int, input().split())
    dd[a].append((c,b))

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

for i in dfs(start)[1:]:
    if i == 1e9:
        print("INF")
    else:
        print(i)