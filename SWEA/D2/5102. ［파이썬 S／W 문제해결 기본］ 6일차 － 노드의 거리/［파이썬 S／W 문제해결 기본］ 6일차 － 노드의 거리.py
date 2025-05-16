from collections import defaultdict, deque
T = int(input())

for i in range(T):
    V, E = map(int, input().split())
    dd = defaultdict(list)
    
    for j in range(E):
        a, b = map(int, input().split())
        dd[a].append(b)
        dd[b].append(a)
    S, G = map(int, input().split())
    q = deque()
    q.append((S, 1))
    visit = set()
    find = False
    
    while q:
        s, l = q.popleft()
        visit.add(s)
        
        for j in dd[s]:
            if j == G:
                find = True
                break
            if j not in visit:
                q.append((j, l+1))

        if find:
            break
    
    if find:
        print(f"#{i+1} {l}")
    else:
        print(f"#{i+1} 0")