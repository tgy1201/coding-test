import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

dd = defaultdict(list)

N, R, Q = map(int, input().split())
temp = [-1] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())

    dd[u].append(v)
    dd[v].append(u)

visited = [False] * (N+1)
visited[R] = True

def dfs(x):
    node = 0
    if len(dd[x]) == 1 and x != R:
        temp[x] = 1
        return 1

    for i in dd[x]:
        if not visited[i]:
            visited[i] = True
            node += dfs(i)

    temp[x] = node + 1
    return temp[x]

dfs(R)

for _ in range(Q):
    u = int(input())
    print(temp[u])