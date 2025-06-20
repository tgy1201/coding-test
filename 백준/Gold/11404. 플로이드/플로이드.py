import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((c,b))

def dijkstra(x):
    distance = [1e9] * (n+1)
    distance[x] = 0
    hq = [(0, x)]

    while hq:
        cost, p = heapq.heappop(hq)

        if distance[p] < cost:
            continue

        for v, u in bus[p]:
            if distance[u] > cost + v:
                distance[u] = cost + v
                heapq.heappush(hq, (distance[u], u))

    return distance

for i in range(1, n+1):
    result = dijkstra(i)[1:]
    result = list(map(lambda x: x if x != 1e9 else 0, result))
    print(' '.join(map(str, result)))