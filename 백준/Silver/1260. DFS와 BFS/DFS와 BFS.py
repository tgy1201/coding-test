from collections import deque, defaultdict
import sys

def dfs(x):
    visited.add(x)
    answer.append(x)
    for i in dd[x]:
        if i not in visited:
            dfs(i)

def bfs(x):
    dq = deque()
    dq.append(x)
    visited.add(x)
    answer.append(x)
    
    while dq:
        p = dq.popleft()

        for i in dd[p]:
            if i not in visited:
                dq.append(i)
                visited.add(i)
                answer.append(i)
N, M, V = map(int, sys.stdin.readline().split())

dd = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    dd[a].append(b)
    dd[b].append(a)

for i in dd.keys():
    dd[i].sort()

visited = set()
answer = []
dfs(V)
print(' '.join(map(str, answer)))
visited = set()
answer = []
bfs(V)
print(' '.join(map(str, answer)))