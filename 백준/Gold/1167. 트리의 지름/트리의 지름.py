import sys
from collections import defaultdict, deque

input = sys.stdin.readline

V = int(input())
dd = defaultdict(list)

for _ in range(V):
    e = list(map(int, input().split()))

    for index, j in enumerate(e[1:-1]):
        if index % 2 == 0:
            dd[e[0]].append((e[index+1], e[index+2]))

def bfs(a):
    dq = deque()
    dq.append((a,0))
    visited = [False]*(V+1)
    dist = [0] * (V+1)
    visited[a] = True

    while dq:
        p, depth = dq.popleft()

        for x, y in dd[p]:
            if not visited[x]:
                visited[x] = True
                dist[x] = depth + y
                dq.append((x, dist[x]))

    return dist

a = bfs(1)
b = a.index(max(a))
c = bfs(b)

print(max(c))