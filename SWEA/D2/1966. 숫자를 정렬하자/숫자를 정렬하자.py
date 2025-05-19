import math
T = int(input())

for i in range(T):
    N = int(input())
    
    li = list(map(int, input().split()))
    li.sort()
    li = list(map(lambda x: str(x), li))
    print(f"#{i+1} {' '.join(li)}")