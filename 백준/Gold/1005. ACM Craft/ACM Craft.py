import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())


def dfs(x):
    if memo[x] != -1:
        return memo[x]

    m = 0
    for u, v in dd[x]:
        m = max(m, dfs(v))

    memo[x] = m + cost[x-1]
    return memo[x]

for _ in range(T):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))

    dd = defaultdict(list)

    for _ in range(K):
        a, b = map(int, input().split())

        dd[b].append((cost[a-1],a))

    W = int(input())

    memo = [-1] * (N+1)

    print(dfs(W))