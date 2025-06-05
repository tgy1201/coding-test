import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N, M = map(int, input().split())

dd = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dd[a].append(b)
    dd[b].append(a)

def dfs(x):
    visited.add(x)
    for k in dd[x]:
        if k not in visited:
            dfs(k)

visited = set()
answer = 0
for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        answer += 1

print(answer)