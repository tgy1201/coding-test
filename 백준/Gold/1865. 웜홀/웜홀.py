import sys, heapq
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    road = []
    for _ in range(M):
        S, E, T = map(int, input().split())

        road.append((S, E, T))
        road.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())

        road.append((S, E, -T))

    def bf(x):
        dist = [1e9]*(N+1)
        dist[x] = 0

        for i in range(N+1):
            for j in range((2*M)+W+N):
                start, end, cost = road[j]

                if dist[start] != 1e9 and dist[end] > dist[start] + cost:
                    dist[end] = dist[start] + cost

                    if i == N:
                        return False

        return True

    for i in range(1, N+1):
        road.append((0, i, 0))

    if bf(0):
        print("NO")
    else:
        print("YES")