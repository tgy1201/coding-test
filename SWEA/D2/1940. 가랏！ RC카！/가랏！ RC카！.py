import math
T = int(input())

for i in range(T):
    N = int(input())
    d = 0
    s = 0
    
    for j in range(N):
        c = list(map(int, input().split()))
        if c[0] == 0:
            d += s
            continue
        
        if c[0] == 1:
            s += c[1]
            d += s
        else:
            s = max(s-c[1], 0)
            d += s
    print(f"#{i+1} {d}")