import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
dd = defaultdict(list)
dl = defaultdict(list)

for _ in range(N-1):
    a, b, c = map(int, input().split())

    dl[a].append((b, c))
    dl[b].append((a, c))

start = 0
answer = 0

def dfs(x, v):
    global answer
    global start
    if len(dl[x]) == 1 and answer < v:
        start = x
        answer = v

    for i, p in dl[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, v+p)

visited = [False] * (N+1)
visited[1] = True
dfs(1, 0)

answer = 0
visited = [False] * (N+1)
visited[start] = True
dfs(start, 0)

print(answer)