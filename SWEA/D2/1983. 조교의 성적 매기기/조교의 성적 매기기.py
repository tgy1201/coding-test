T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    grade = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0" ]
    goal = 0
    li = []
    for j in range(N):
        e = list(map(int, input().split()))
        li.append([e[0]*0.35+e[1]*0.45+e[2]*0.20, j+1])
    ll = sorted(li, reverse=True)
    
    rate =  N // 10
    
    for index, x in enumerate(ll):
        if x[1] == K:
            goal = index
    print(f"#{i+1} {grade[goal//rate]}")
            
    