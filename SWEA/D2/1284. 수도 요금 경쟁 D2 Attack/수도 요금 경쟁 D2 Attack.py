import math
T = int(input())

for i in range(T):
    P,Q,R,S,W = map(int, input().split())
    
    a = P * W
    
    if W < R:
        b = Q
    else:
        b = Q + (W-R)*S
    
    print(f"#{i+1} {min(a,b)}")        