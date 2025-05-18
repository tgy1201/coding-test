import copy
T = int(input())

def calc(arr, K):
    total = 0
    
    for i in arr:
        check = 0
        temp = []
        for j in i:
            if j == 1:
                check += 1
            else:
                temp.append(check)
                check = 0
                
        if check != 0:
            temp.append(check)
            
        total += temp.count(K)
    return total
for i in range(T):
    N, K = map(int, input().split())
    
    puz = []
    for j in range(N):
        row = list(map(int, input().split()))
        puz.append(row)
        
    pp = [[0]*N for _ in range(N)]
    
    for j in range(len(puz)):
        for k in range(len(puz[0])):
            pp[j][k] = puz[k][j]
    
    print(f"#{i+1} {calc(puz, K)+ calc(pp, K)}")