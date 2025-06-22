import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
road = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append((c,b))

def dijkstra(x):
    dist = [1e9] * (N+1)

    hq = [(0, x)]

    while hq:
        cost, p = heapq.heappop(hq)

        if dist[p] < cost:
            continue
        for u, v in road[p]:
            if dist[v] > u + cost:
                dist[v] = u + cost
                heapq.heappush(hq, (dist[v], v))
    return dist

answer = 0

x = dijkstra(X)
for i in range(1, N+1):
    if i != X:
        answer = max(answer, dijkstra(i)[X]+x[i])

print(answer)
