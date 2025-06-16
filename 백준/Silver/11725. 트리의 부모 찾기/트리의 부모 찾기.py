from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

dd = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    dd[a].append(b)
    dd[b].append(a)

visited = [False]*(N+1)
visited[1] = True
temp = [0] * (N+1)

def dfs(n):

    for i in dd[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            temp[i] = n

dfs(1)

for i in range(2, len(temp)):
    print(temp[i])
