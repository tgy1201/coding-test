T = int(input())

def calc(e, li):
    a, b = e[0]//3, e[1]//3
    cnt = 0
    for i in range(3):
        for j in range(3):
            if li[a*3+i][b*3+j] == li[e[0]][e[1]]:
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False
for i in range(T):
    li = []
    
    for j in range(9):
        t = list(map(int, input().split()))
        li.append(t)
        
    ll = [[0] * 9 for _ in range(9)]
    
    for j in range(9):
        for k in range(9):
            ll[j][k] = li[k][j]
    
    flag = 1
    for j in range(9):
        for k in range(9):
            if li[j].count(li[j][k]) != 1 or ll[j].count(ll[j][k]) != 1 or not calc([j,k], li):
                flag = 0
                break
    
    print(f"#{i+1} {flag}")
    