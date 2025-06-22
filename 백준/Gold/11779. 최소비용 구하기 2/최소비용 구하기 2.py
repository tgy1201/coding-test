import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((c,b))

def dijstra(x, y):
    dist = [1e9]*(n+1)
    dist[x] = 0
    visited = [[i] for i in range(n+1)]

    hq = [(0, x)]

    while hq:
        cost, p = heapq.heappop(hq)

        if dist[p] < cost:
            continue

        for v, u in bus[p]:
            if dist[u] > cost + v:
                visited[u] = visited[p][:]
                visited[u].append(u)
                dist[u] = cost + v
                heapq.heappush(hq, (dist[u], u))

    print(dist[y])
    print(len(visited[y]))
    print(' '.join(map(str, visited[y])))

A, B = map(int, input().split())
dijstra(A, B)