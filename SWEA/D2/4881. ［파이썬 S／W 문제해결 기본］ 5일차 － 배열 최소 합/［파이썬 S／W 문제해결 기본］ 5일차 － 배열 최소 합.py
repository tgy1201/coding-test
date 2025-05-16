T = int(input())

def dfs(n, v, r):
    global min_sum
    if n >= min_sum:
        return
    if r+1 >= len(row):
        min_sum = n
        return
    for index, j in enumerate(li[r+1]):
        if index in v:
            continue
        v.add(index)
        dfs(n+j, v, r+1)
        v.remove(index)

for i in range(T):
    N = int(input())
    li = []
    for j in range(N):
        row = list(map(int, input().split()))
        li.append(row)
    
    r = 0
    min_sum = float('inf')
    for index, j in enumerate(li[0]):
        visit = set()
        visit.add(index)
        dfs(j, visit, r)
    
    print(f"#{i+1} {min_sum}")
    