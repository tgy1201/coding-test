from collections import defaultdict

def dfs(c, d, v):
    v.append(c)
    answer.append(d)
    if len(dd[c]) == 0:
        return
    for k in dd[c]:
        if k not in v:
            dfs(k, d+1, v[:])

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    answer = []
    dd = defaultdict(list)

    for j in range(M):
        x, y = map(int, input().split())
        dd[x].append(y)
        dd[y].append(x)

    for j in dd.keys():
        dfs(j, 1, [])

    if M == 0:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} {max(answer)}")
#shift+F10