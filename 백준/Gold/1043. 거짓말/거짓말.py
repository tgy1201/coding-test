import sys
from collections import defaultdict
input = sys.stdin.readline


N, M = map(int, input().split())

E = list(map(int, input().split()))
dd = defaultdict(set)
di = defaultdict(int)
truth = [[] for _ in range(N+1)]
answer = 0

if E[0] == 0:
    print(M)
else:
    ri = set(E[1:])

    P = []
    for i in range(M):
        party = list(map(int, input().split()))

        check = 0
        for j in party[1:]:
            dd[j].update(party[1:])

        P.append(party[1:])

    def dfs(x):
        for i in dd[x]:
            if not visited[i]:
                visited[i] = True
                di[i] = 1
                dfs(i)

    for i in ri:
        visited = [False] * (N + 1)
        visited[i] = True
        di[i] = 1
        dfs(i)

    for i in P:
        check = 0
        for j in i:
            if j in set(di):
                check = 1
                break
        if check == 0:
            answer += 1

    print(answer)