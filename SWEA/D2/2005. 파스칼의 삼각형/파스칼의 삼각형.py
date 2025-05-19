T = int(input())

for i in range(T):
    N = int(input())
    
    li = [[0]*(x+1) for x in range(N)]
    
    for j in range(N):
        li[j][0] = 1
    
    for j in range(1, N):
        for k in range(1, j+1):
            if k == j:
                li[j][k] = li[j-1][k-1]
            else:
                li[j][k] = li[j-1][k-1] + li[j-1][k]
    
    print(f"#{i+1}")
    for j in li:
        s = ""
        for k in j:
            s+= str(k) + " "
        print(s)