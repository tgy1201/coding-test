from collections import deque

#1=>N / 2->S / N|T|S
for i in range(10):
    T = int(input())
    
    li = []
    for j in range(T):
        e = list(map(int, input().split()))
        li.append(e)
    
    ll = [[0]*T for _ in range(T)]
    
    for j in range(T):
        for k in range(T):
            ll[j][k] = li[k][j]
    
    answer = 0
    for j in range(T):
        dq = deque()
        for k in range(T):
            if ll[j][k] == 2 and len(dq) == 0:
                continue
            
            if ll[j][k] == 1:
                dq.append(1)
            elif ll[j][k] == 2:
                if dq and dq[-1] == 1:
                    answer += 1
                dq.append(2)
    
    print(f"#{i+1} {answer}")