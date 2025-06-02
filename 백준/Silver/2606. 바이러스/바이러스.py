from collections import defaultdict

def dfs(n):
    global visit
    visit.add(n)

    for i in dd[n]:
        if i not in visit:
            dfs(i)
visit = set()
n = int(input())
s = int(input())

dd = defaultdict(list)

for i in range(s):
    a, b = map(int, input().split())
    dd[a].append(b)
    dd[b].append(a)
dfs(1)

print(len(visit)-1)

